from pathlib import Path


class FileScanner:

    def __init__(self, folder_path):
        self._folder_path = Path(folder_path)

    def scan(self):
        if not self._folder_path.exists():
            raise FileNotFoundError(
                f"Folder not found: {self._folder_path}"
            )

        if not self._folder_path.is_dir():
            raise NotADirectoryError(
                f"This is not a folder: {self._folder_path}"
            )

        files = []

        for item in self._folder_path.iterdir():
            if item.is_file():
                files.append({
                    'name': item.name,
                    'path': str(item),
                    'extension': item.suffix.lower(),
                    'size': item.stat().st_size
                })

        return files
      
