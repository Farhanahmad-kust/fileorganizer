# Testing Installation

To test your package installation locally before publishing to GitHub:

1. **Create a virtual environment**

   ```bash
   python -m venv test_env
   # Windows
   test_env\Scripts\activate
   # macOS/Linux
   source test_env/bin/activate
   ```

2. **Install from local directory**

   ```bash
   # From the root of your project
   pip install -e .
   ```

3. **Test command-line functionality**

   ```bash
   # Create a test directory with some files
   mkdir test_dir
   # Copy some files to test_dir
   
   # Run the organizer
   fileorganizer organize test_dir --verbose
   
   # Check if files were organized properly
   dir test_dir
   
   # Test undo functionality
   fileorganizer undo test_dir
   ```

4. **Test programmatic usage**

   Create a test script like this:

   ```python
   from pathlib import Path
   from fileorganizer.organizer import FileOrganizer
   
   # Create an organizer instance
   test_dir = Path("./test_dir")
   organizer = FileOrganizer(test_dir)
   
   # Organize files
   organizer.organize()
   
   # Get statistics
   stats = organizer.get_statistics()
   print(f"Files moved: {stats['files_moved']}")
   
   # Undo operations
   organizer.undo_last_operation()
   ```

5. **Verify package structure**

   Make sure the package was installed correctly:

   ```python
   import fileorganizer
   print(fileorganizer.__file__)  # Should point to your installed package
   ```

6. **Cleanup test environment**

   ```bash
   # Deactivate virtual environment
   deactivate
   # Remove test environment
   rm -rf test_env  # Linux/macOS
   rmdir /s /q test_env  # Windows
   ```