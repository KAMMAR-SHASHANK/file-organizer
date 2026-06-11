import shutil
from pathlib import Path
from category_config import CategoryConfig
from scanner import FileScanner


class FileOrganizer:

    def __init__(self, folder_path):
        self._folder_path = Path(folder_path)
        self._scanner = FileScanner(folder_path)
        self._config = CategoryConfig()

    def organize(self):
        files = self._scanner.scan()
        results = []

        for file in files:
            category = self._config.get_category(file['extension'])
            destination_folder = self._folder_path / category

            destination_folder.mkdir(exist_ok=True)

            source = Path(file['path'])
            destination = destination_folder / file['name']

            if destination.exists():
                destination = self._resolve_duplicate(destination)

            shutil.move(str(source), str(destination))

            results.append({
                'file': file['name'],
                'from': file['path'],
                'to': str(destination),
                'category': category
            })

        return results

    def _resolve_duplicate(self, path):
        counter = 1
        stem = path.stem
        suffix = path.suffix
        parent = path.parent

        while path.exists():
            path = parent / f"{stem}_{counter}{suffix}"
            counter += 1

        return path


