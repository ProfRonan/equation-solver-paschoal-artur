import builtins
import importlib
import io
import sys

import pytest
from pytest import MonkeyPatch


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ("-1", "Grau inválido"),
        ("-3", "Grau inválido"),
        ("0", "Grau inválido"),
        ("3", "Grau inválido"),
        ("10", "Grau inválido"),
    ],
)
def test_grau_invalido(monkeypatch: MonkeyPatch, test_input: str, expected_output: str):
    mocked_input = lambda prompt="": test_input
    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    assert expected_output in mocked_stdout.getvalue().strip()
