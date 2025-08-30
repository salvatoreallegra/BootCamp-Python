# -------------------------------------------------------
# test_models_package.py
# PURPOSE: Show using a session-scoped fixture across files.
# -------------------------------------------------------
from bootcamp_python.models.task import Task

def test_task_to_dict_and_back(temp_data_dir):
    t = Task("Pkg test")
    d = t.to_dict()
    assert d["title"] == "Pkg test"
    assert d["is_done"] is False
    # here we could save to temp_data_dir if needed
