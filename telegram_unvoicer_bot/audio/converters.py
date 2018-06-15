from asyncio import subprocess

__all__ = [
    'convert_opus',
]


async def convert_opus(file_path, new_file_path):
    """
    Convert files with .opus extension (using by WhatsApp).
    Depends on unix opus-tools>=0.1.9-1 package.
    """
    process = await subprocess.create_subprocess_exec(
        'opusdec', file_path, new_file_path
    )
    await process.communicate()

    if process.returncode != 0:
        raise FileNotFoundError('Convert file error.')
