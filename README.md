# FileOrganizer

![PyPI Version](https://img.shields.io/pypi/v/fileorganizer-farhan)
![Python Versions](https://img.shields.io/pypi/pyversions/fileorganizer-farhan)
![License](https://img.shields.io/pypi/l/fileorganizer-farhan)

A Python utility that automatically organizes messy files in a folder into categorized subfolders.

## Author

- **Farhan Ahmad** - [GitHub](https://github.com/Farhanahmad-kust)
- Email: farhanbangash091@gmail.com

## Features

- **Automatic Organization**: Sorts files into logical category folders based on file extensions
- **Command Line Interface**: Easy to use CLI for quick file organization
- **Undo Capability**: Revert back to the original file structure if needed
- **Customizable Categories**: Define your own category mapping for file extensions
- **Exclude Patterns**: Keep certain files in place during organization
- **Detailed Logging**: Optional verbose output to see what's happening

## Installation

```bash
pip install fileorganizer-farhan
```

## Usage

### Command Line

```bash
# Basic usage
fileorganizer organize ~/Downloads

# With verbose output
fileorganizer organize ~/Documents/messy_folder --verbose

# Undo the last organization
fileorganizer undo ~/Downloads
```

### Python API

```python
from pathlib import Path
from fileorganizer.organizer import FileOrganizer

# Create an organizer for a specific directory
target_dir = Path("~/Downloads").expanduser()
organizer = FileOrganizer(target_dir)

# Organize files
organizer.organize()

# If needed, undo the organization
organizer.undo_last_operation()
```

## Custom Categories

You can define your own category mapping:

```python
custom_categories = {
    "Work": [".doc", ".docx", ".xls", ".xlsx", ".pdf"],
    "Media": [".jpg", ".png", ".mp3", ".mp4"],
    "Code": [".py", ".js", ".html", ".css"]
}

organizer = FileOrganizer("~/Documents", category_map=custom_categories)
organizer.organize()
```

## Excluding Files

```python
# Files matching these patterns will be left in place
exclude_patterns = ["*.txt", "important.*", "project_*"]
organizer.organize(exclude_patterns=exclude_patterns)
```

## License

MIT License

## Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/amazing-feature`)
3. Commit your Changes (`git commit -m 'Add some amazing feature'`)
4. Push to the Branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
