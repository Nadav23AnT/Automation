import os
from pathlib import Path
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}


def pick_directory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'


print(pick_directory('.pdf'))


def organize_directory():
    for item in os.scandir():
        if item.is_dir():
            continue
        filepath = Path(item)
        filetype = filepath.suffix.lower()
        directory = pick_directory(filetype)
        directorypath = Path(directory)
        if not directorypath.is_dir():
            directorypath.mkdir()
        filepath.rename(directorypath.joinpath(filepath))


organize_directory()

