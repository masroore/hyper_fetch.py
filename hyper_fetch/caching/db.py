import sqlite3
from typing import Optional
from datetime import datetime

from hyper_fetch.caching.base import CacheBackend


class SQLiteCache(CacheBackend):
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cache (
                    key TEXT PRIMARY KEY,
                    value BLOB,
                    expiry INTEGER
                )
            """)
            conn.commit()

    async def get(self, key: str) -> Optional[bytes]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT value, expiry FROM cache WHERE key = ?", (key,))
            row = cursor.fetchone()
            if row:
                value, expiry = row
                if expiry > datetime.now().timestamp():
                    return value
                else:
                    await self.delete(key)
        return None

    async def set(self, key: str, value: bytes, ttl: Optional[int] = None) -> None:
        expiry = datetime.now().timestamp() + (ttl or 3600)
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT OR REPLACE INTO cache (key, value, expiry)
                VALUES (?, ?, ?)
            """,
                (key, value, expiry),
            )
            conn.commit()

    async def delete(self, key: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cache WHERE key = ?", (key,))
            conn.commit()

    async def clear(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM cache")
            conn.commit()
