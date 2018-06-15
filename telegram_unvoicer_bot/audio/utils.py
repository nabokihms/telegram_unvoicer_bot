from aiofiles import open as async_open


# todo: clear tmp directory
async def write_file_to_tmp_dir(path, body):
    async with async_open(path, 'wb+') as f:
        await f.write(body)
