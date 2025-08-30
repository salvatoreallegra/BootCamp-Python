import os
import importlib

def test_env_override(monkeypatch):
    monkeypatch.setenv("API_KEY", "from-env")
    import bootcamp_python.config as config
    importlib.reload(config)  # reload to re-evaluate
    assert config.API_KEY == "from-env"
