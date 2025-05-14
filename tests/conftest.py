import sys
import os

# Add the project root directory to sys.path
# This allows pytest to find modules in the 'src' directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)