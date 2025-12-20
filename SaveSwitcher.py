from sys import argv, exit
from pathlib import Path
from shutil import copyfile

if __name__ == "__main__": 
    if len(argv) != 3:
        raise RuntimeError("Not enough arguments")

    backups_path = Path(argv[1])
    if not backups_path.exists():
        raise FileExistsError(f"No backup saves at {backups_path}")

    target_path = Path(argv[2])
    if not target_path.exists() or not target_path.is_file:
        raise FileExistsError(f"{target_path} target save file not found")

    save_file_name = target_path.name
    # Load save directories, order by name
    try:
        for backup_dir in backups_path.iterdir(): 
            print(f"Next file to swap: {backup_dir}/{save_file_name}")
            input("Press enter to continue..")
            print(f"Backing up {target_path}.prev")
            copyfile(target_path, f"{target_path}.prev")
            print(f"Now swapping {target_path} with {backup_dir}/{save_file_name}")
            copyfile(f"{backup_dir}/{save_file_name}", target_path)
            print("Files swapped")
    except KeyboardInterrupt:
        exit()
