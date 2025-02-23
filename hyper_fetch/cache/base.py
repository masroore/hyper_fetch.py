from abc import ABC, abstractmethod
from typing import Optional


class CacheBackend(ABC):
    @abstractmethod
    async def get(self, key: str) -> Optional[bytes]: ...

    @abstractmethod
    async def set(self, key: str, value: bytes, ttl: Optional[int] = None) -> None: ...

    @abstractmethod
    async def delete(self, key: str) -> None: ...

    @abstractmethod
    async def clear(self) -> None: ...
