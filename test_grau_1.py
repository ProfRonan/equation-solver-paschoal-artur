import builtins
import importlib
import io
import sys

import pytest
from pytest import MonkeyPatch


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        (["1", "0"], ["A equação é do primeiro grau", "Valor de a inválido"]),
    ],
)
def test_grau_1_a_0(monkeypatch: MonkeyPatch, test_input: list[str], expected_output: str):
    mocked_input = lambda prompt="": test_input.pop(0)

    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    for output in expected_output:
        assert output in mocked_stdout.getvalue().strip()


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        (["1", "1", "0"], ["A equação é do primeiro grau", "0.00"]),
        (["1", "2", "0"], ["A equação é do primeiro grau", "0.00"]),
        (["1", "10", "0"], ["A equação é do primeiro grau", "0.00"]),
        (["1", "1", "-5"], ["A equação é do primeiro grau", "5.00"]),
        (["1", "2", "4"], ["A equação é do primeiro grau", "-2.00"]),
        (["1", "2", "-4"], ["A equação é do primeiro grau", "2.00"]),
    ],
)
def test_grau_1(monkeypatch: MonkeyPatch, test_input: list[str], expected_output: list[str]):
    mocked_input = lambda prompt="": test_input.pop(0)

    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    for output in expected_output:
        assert output in mocked_stdout.getvalue().strip()
