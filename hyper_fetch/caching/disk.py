import asyncio
import hashlib
import pickle
from abc import ABC
from datetime import datetime
from pathlib import Path
from typing import Optional

import aiofiles

from hyper_fetch.caching.base import CacheBackend


class DiskCache(CacheBackend, ABC):
    def __init__(self, cache_dir: Path, max_size: int):
        self.cache_dir = cache_dir
        self.max_size = max_size
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._lock = asyncio.Lock()

    @staticmethod
    def _encode_key(key: str) -> str:
        return hashlib.sha256(key.encode()).hexdigest()

    async def get(self, key: str) -> Optional[bytes]:
        file_path = self.cache_dir / self._encode_key(key)
        try:
            async with aiofiles.open(file_path, "rb") as f:
                metadata = pickle.loads(await f.read())
                if metadata["expiry"] > datetime.now().timestamp():
                    return metadata["data"]
                await self.delete(key)
        except (FileNotFoundError, pickle.PickleError):
            return None
        return None

    async def set(self, key: str, value: bytes, ttl: Optional[int] = None) -> None:
        async with self._lock:
            # Check and enforce size limit
            current_size = sum(f.stat().st_size for f in self.cache_dir.glob("*"))
            while current_size + len(value) > self.max_size:
                # Remove oldest file
                files = sorted(
                    self.cache_dir.glob("*"), key=lambda x: x.stat().st_mtime
                )
                if not files:
                    return
                files[0].unlink()
                current_size = sum(f.stat().st_size for f in self.cache_dir.glob("*"))

            file_path = self.cache_dir / self._encode_key(key)
            metadata = {
                "data": value,
                "expiry": datetime.now().timestamp() + (ttl or 3600),
            }
            async with aiofiles.open(file_path, "wb") as f:
                await f.write(pickle.dumps(metadata))
