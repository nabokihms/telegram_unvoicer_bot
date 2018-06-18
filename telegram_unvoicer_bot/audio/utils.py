from aiofiles import open as async_open


# todo: чистить временное хранилище от файлов после декодирования
async def write_file_to_tmp_dir(path: str, body: bytes):
    async with async_open(path, 'wb+') as f:
        await f.write(body)
