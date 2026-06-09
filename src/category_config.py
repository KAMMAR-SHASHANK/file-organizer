class CategoryConfig:

    def __init__(self):
        self._categories = {
            # Images
            '.jpg': 'Images',
            '.jpeg': 'Images',
            '.png': 'Images',
            '.gif': 'Images',
            '.bmp': 'Images',
            '.svg': 'Images',
            '.webp': 'Images',

            # Documents
            '.pdf': 'Documents',
            '.doc': 'Documents',
            '.docx': 'Documents',
            '.txt': 'Documents',
            '.xlsx': 'Documents',
            '.pptx': 'Documents',
            '.csv': 'Documents',

            # Videos
            '.mp4': 'Videos',
            '.mov': 'Videos',
            '.avi': 'Videos',
            '.mkv': 'Videos',
            '.wmv': 'Videos',

            # Music
            '.mp3': 'Music',
            '.wav': 'Music',
            '.flac': 'Music',
            '.aac': 'Music',

            # Code
            '.py': 'Code',
            '.js': 'Code',
            '.html': 'Code',
            '.css': 'Code',
            '.java': 'Code',
            '.json': 'Code',

            # Archives
            '.zip': 'Archives',
            '.tar': 'Archives',
            '.gz': 'Archives',
            '.rar': 'Archives',

            # Applications
            '.dmg': 'Applications',
            '.exe': 'Applications',
            '.pkg': 'Applications',
        }

    def get_category(self, extension):
        return self._categories.get(extension.lower(), 'Others')

    def get_all_categories(self):
        return set(self._categories.values())



    