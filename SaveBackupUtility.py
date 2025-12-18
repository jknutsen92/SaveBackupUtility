from sys import argv, exit
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from shutil import copyfile
from uuid import uuid4
import time

if __name__ == "__main__":
    if len(argv) < 2:
        raise RuntimeError("Not enough arguments, please provide the path to a save file")

    save_path = Path(argv[1])

    if (not save_path.exists() and not save_path.is_file):
        raise RuntimeError("Invalid path")

    save_dir = save_path.parent
    backup_dir = save_dir.joinpath("backups")
    try:
        backup_dir.mkdir()
        print(f"Created backup directory {backup_dir}")
    except FileExistsError:
        print(f"Backup directory {backup_dir} exists")
    print(f"backing up saves to {backup_dir}")

    print(f"Now watching {save_path} for updates")

    try:
        while True:
            prev_modified_time = save_path.stat().st_mtime
            time.sleep(5)
            if prev_modified_time < save_path.stat().st_mtime:
                unique_name = f"{save_path.name}_{str(uuid4())}"
                copyfile(save_path, f"{backup_dir}/{unique_name}")
                print(f"{save_path.name} updated, making backup {unique_name} in {backup_dir}")
    except KeyboardInterrupt:
        exit()