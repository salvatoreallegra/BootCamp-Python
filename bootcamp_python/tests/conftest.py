# -------------------------------------------------------
# conftest.py
# PURPOSE: Fixtures available to all test files.
# Demonstrates yield-fixtures (setup + teardown).
# -------------------------------------------------------
import pytest
from pathlib import Path
import tempfile
import shutil

@pytest.fixture(scope="session")
def temp_data_dir():
    """Create a temp data directory for all tests in the session."""
    path = Path(tempfile.mkdtemp(prefix="bootcamp_pydata_"))
    yield path
    # teardown runs after tests finish
    shutil.rmtree(path)
