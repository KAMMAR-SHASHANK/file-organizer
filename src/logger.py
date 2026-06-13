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

    def print_summary(self, skipped=None):
        duration = (datetime.now() - self._start_time).seconds
        skipped = skipped or []

        print("\n" + "=" * 45)
        print("           ORGANIZER SUMMARY")
        print("=" * 45)

        if not self._log and not skipped:
            print("  No files found to organize.")
        else:
            if self._log:
                categories = {}
                for entry in self._log:
                    cat = entry['category']
                    categories[cat] = categories.get(cat, 0) + 1

                for category, count in sorted(categories.items()):
                    print(f"  {category:<20} {count} file(s)")

                print("-" * 45)
                print(f"  Total organized:        {len(self._log)}")

            if skipped:
                print(f"  Already in place:       {len(skipped)}")

            print(f"  Time taken:             {duration}s")

        print("=" * 45 + "\n")