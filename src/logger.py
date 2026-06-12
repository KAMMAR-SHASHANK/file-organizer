from datetime import datetime


class Logger:

    def __init__(self):
        self._log = []
        self._start_time = datetime.now()

    def record(self, result):
        entry = {
            'timestamp': datetime.now().strftime('%H:%M:%S'),
            'file': result['file'],
            'category': result['category'],
            'from': result['from'],
            'to': result['to']
        }
        self._log.append(entry)
        print(f"  ✓  {entry['file']}  →  {entry['category']}")

    def print_summary(self):
        duration = (datetime.now() - self._start_time).seconds

        print("\n" + "=" * 45)
        print("           ORGANIZER SUMMARY")
        print("=" * 45)

        if not self._log:
            print("  No files found to organize.")
        else:
            categories = {}
            for entry in self._log:
                cat = entry['category']
                categories[cat] = categories.get(cat, 0) + 1

            for category, count in sorted(categories.items()):
                print(f"  {category:<20} {count} file(s)")

            print("-" * 45)
            print(f"  Total files organized:  {len(self._log)}")
            print(f"  Time taken:             {duration}s")

        print("=" * 45 + "\n")