# Development Guide for FileOrganizer

This guide will help you set up the development environment for contributing to the FileOrganizer package.

## Setting Up Development Environment

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fileorganizer.git
cd fileorganizer
```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Development Dependencies

```bash
pip install -e ".[dev]"
```

This will install the package in development mode along with development dependencies.

## Running Tests

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=fileorganizer

# Generate HTML coverage report
pytest --cov=fileorganizer --cov-report=html
```

## Code Style

This project follows PEP 8 style guidelines. You can check your code style with:

```bash
# Check style
flake8 fileorganizer

# Auto-format code
black fileorganizer
```

## Building the Package

```bash
# Build source and wheel distribution
python -m build
```

## Making a Pull Request

1. Create a branch for your feature or bugfix
   ```bash
   git checkout -b feature-name
   ```

2. Make your changes and commit them
   ```bash
   git add .
   git commit -m "Description of changes"
   ```

3. Push your branch
   ```bash
   git push origin feature-name
   ```

4. Open a pull request on GitHub

## Project Structure

```
fileorganizer/
├── fileorganizer/
│   ├── __init__.py
│   ├── cli.py         # Command line interface
│   ├── organizer.py   # Core functionality
│   └── utils.py       # Helper functions
├── tests/
│   ├── __init__.py
│   ├── test_cli.py
│   └── test_organizer.py
├── pyproject.toml     # Project configuration
├── setup.py           # Setup script
└── README.md          # Project documentation
```

## Common Tasks

### Adding a New Feature

1. Implement the feature in the appropriate module
2. Add tests for the feature
3. Update documentation if necessary
4. Run tests and ensure code style compliance

### Fixing a Bug

1. Add a test that reproduces the bug
2. Fix the bug
3. Ensure all tests pass

## Release Process

1. Update version in `pyproject.toml` and `fileorganizer/__init__.py`
2. Update CHANGELOG.md
3. Create a git tag
4. Build the package
5. Upload to PyPI

```bash
python -m build
twine upload dist/*
```