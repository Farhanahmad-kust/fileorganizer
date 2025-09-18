"""
This is a simple redirect file to the main fileorganizer package.
"""

import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from fileorganizer import FileOrganizer, main
    
    if __name__ == "__main__":
        sys.exit(main())
        
except ImportError:
    print("FileOrganizer package not found.")
    print("Please install it using:")
    print("pip install -e fileorganizer/")
    sys.exit(1)