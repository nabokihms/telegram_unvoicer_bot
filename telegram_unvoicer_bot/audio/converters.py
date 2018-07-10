from asyncio import subprocess

__all__ = [
    'convert_opus',
]


async def convert_opus(file_path: str, new_file_path: str):
    """
    Конвертирует файл с расширением .opus (используется WhatsApp).
    Зависит от внешнего пакета opus-tools>=0.1.9-1.
    """
    process = await subprocess.create_subprocess_exec(
        'opusdec', file_path, new_file_path
    )
    await process.wait()

    if process.returncode != 0:
        raise FileNotFoundError('Convert file error.')
