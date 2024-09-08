"""
This is the initialization file for the 'app' package.

The 'app' package contains the core application logic including
task definitions, configuration, and the main entry point.
"""

# Optionally, you can define package version here
__version__ = "1.0.0"

# Optionally, you can import functions or classes to simplify access
from .tasks import load_csv_from_queue, analyze_data_task
