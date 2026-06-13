# File Organizer

A command-line tool that automatically scans a folder and organizes
files into subfolders based on their type. Built with Python using
Object-Oriented Programming principles.

---

## What It Does

Point it at any folder — Downloads, Desktop, anywhere — and it:

- Scans every file inside
- Identifies the file type by extension
- Creates category subfolders automatically
- Moves each file into the right folder
- Skips hidden files, system files, and files already organized
- Handles duplicate filenames without overwriting anything
- Prints a live summary of everything it did

---

## Categories

| Folder       | Extensions                            |
| ------------ | ------------------------------------- |
| Images       | .jpg .jpeg .png .gif .bmp .svg .webp  |
| Documents    | .pdf .doc .docx .txt .xlsx .pptx .csv |
| Videos       | .mp4 .mov .avi .mkv .wmv              |
| Music        | .mp3 .wav .flac .aac                  |
| Code         | .py .js .html .css .java .json        |
| Archives     | .zip .tar .gz .rar                    |
| Applications | .dmg .exe .pkg                        |
| Others       | anything not in the list above        |

---

## Setup

**Requirements:** Python 3.x — no external libraries needed.

```bash
git clone https://github.com/KAMMAR-SHASHANK/file-organizer.git
cd file-organizer
```

No `pip install` needed. Only Python standard library is used.

---

## How to Use

```bash
python3 main.py <folder_path>
```

**Examples:**

```bash
# Organize your Downloads folder
python3 main.py ~/Downloads

# Organize your Desktop
python3 main.py ~/Desktop

# Organize any specific folder
python3 main.py /path/to/any/folder
```

---

## Example Output

```
Scanning:  /Users/shashank/Downloads
Starting organization...

  ✓  photo.jpg          →  Images
  ✓  report.pdf         →  Documents
  ✓  song.mp3           →  Music
  ✓  project.zip        →  Archives
  ✓  notes.txt          →  Documents
  ✓  video.mp4          →  Videos
  ✓  script.py          →  Code
  ✓  unknown.xyz        →  Others

=============================================
           ORGANIZER SUMMARY
=============================================
  Archives              1 file(s)
  Code                  1 file(s)
  Documents             2 file(s)
  Images                1 file(s)
  Music                 1 file(s)
  Others                1 file(s)
  Videos                1 file(s)
---------------------------------------------
  Total organized:        8
  Already in place:       0
  Time taken:             0s
=============================================
```

---

## Edge Cases Handled

| Situation                           | What happens                                     |
| ----------------------------------- | ------------------------------------------------ |
| Folder is empty                     | Prints "No files found to organize." cleanly     |
| File has no extension               | Skipped automatically                            |
| Hidden files (.DS_Store etc.)       | Detected and skipped                             |
| File already in correct folder      | Counted as "already in place", not moved again   |
| Duplicate filename at destination   | Renamed automatically (photo_1.jpg, photo_2.jpg) |
| Permission denied on a file         | Prints a warning, continues with remaining files |
| Folder path does not exist          | Prints a clear error message, exits cleanly      |
| A file path given instead of folder | Prints a clear error message, exits cleanly      |
| Program run twice on same folder    | Safe — already organized files are skipped       |

---

## Project Structure

```
file-organizer/
├── main.py                    ← run this from terminal
├── src/
│   ├── category_config.py     ← extension to folder mapping
│   ├── scanner.py             ← reads files from a folder
│   ├── organizer.py           ← moves files to correct folders
│   └── logger.py              ← tracks and reports results
├── requirements.txt
└── README.md
```

---

## OOP Architecture

This project is built around four classes, each with a single responsibility.

**`CategoryConfig`** — holds a private dictionary mapping every file
extension to a category folder name. Nothing outside this class
touches the mapping directly. Demonstrates **encapsulation**.

**`FileScanner`** — takes a folder path and returns a list of all
valid files inside. Skips hidden files and files with no extension.
The caller never knows how the scanning works internally.
Demonstrates **abstraction**.

**`FileOrganizer`** — the main class. It _has_ a `FileScanner` and
_has_ a `CategoryConfig`. It does not inherit from either. It uses
both as tools to do its job. Demonstrates **composition over inheritance**.

**`Logger`** — records every file move and prints a formatted summary.
Keeps all logging logic in one place, completely separate from the
organizing logic. Demonstrates **single responsibility**.

```
main.py
  └── FileOrganizer
        ├── FileScanner       (finds the files)
        ├── CategoryConfig    (decides where they go)
        └── Logger            (records what happened)
```

---

## Roadmap

- [x] CLI tool — scan and organize by file extension
- [x] Skip hidden and system files
- [x] Handle duplicate filenames safely
- [x] Handle permission errors gracefully
- [x] Safe to run multiple times on same folder
- [ ] Frontend — drag and drop web interface
- [ ] Undo — restore files to their original location
- [ ] Watch mode — auto-organize as new files are added
- [ ] Local AI — group photos by people using on-device face recognition
      (no data sent to any server)

---

## What I Learned

- Structuring a Python project using OOP principles
- Using `pathlib` for file system operations
- Using `shutil` to move files safely
- Handling real-world edge cases — empty folders, hidden files,
  duplicate names, permission errors
- Building a CLI tool using `sys.argv`
- Daily Git workflow — committing and pushing every day

---

_Built as a structured week-long learning project._
