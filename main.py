import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from organizer import FileOrganizer
from logger import Logger


def main():
    if len(sys.argv) < 2:
        print("\nUsage:   python3 main.py <folder_path>")
        print("Example: python3 main.py ~/Downloads\n")
        sys.exit(1)

    folder_path = os.path.expanduser(sys.argv[1])

    print(f"\nScanning:  {folder_path}")
    print("Starting organization...\n")

    try:
        organizer = FileOrganizer(folder_path)
        logger = Logger()

        results, skipped = organizer.organize()

        for result in results:
            logger.record(result)

        logger.print_summary(skipped)

    except FileNotFoundError as e:
        print(f"\nError: {e}\n")
        sys.exit(1)
    except Exception as e:
        print(f"\nSomething went wrong: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()