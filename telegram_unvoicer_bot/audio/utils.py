from asyncio import subprocess

from aiofiles import open as async_open

__all__ = [
    'write_file_to_tmp_dir',
    'delete_file_from_tmp_dir',
]


async def write_file_to_tmp_dir(path: str, body: bytes):
    async with async_open(path, 'wb+') as f:
        await f.write(body)


async def delete_file_from_tmp_dir(path: str):
    await subprocess.create_subprocess_exec('rm', path)
