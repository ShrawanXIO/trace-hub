import pytest
import sys
import os

# Ensure the app can find the engine and core modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from engine.manager import Manager

@pytest.fixture
def manager_instance():
    """Provides a fresh Manager instance for integration tests."""
    return Manager()