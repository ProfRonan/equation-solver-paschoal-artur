import builtins
import importlib
import io
import sys

import pytest
from pytest import MonkeyPatch


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        (["2", "0"], ["A equação é do segundo grau", "Valor de a inválido"]),
    ],
)
def test_grau_2_a_0(monkeypatch: MonkeyPatch, test_input: list[str], expected_output: list[str]):
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
        (["2", "1", "0", "0"], ["A equação é do segundo grau",
                                "A equação possui uma raiz real", "0.00"]),
        (["2", "1", "0", "1"], ["A equação é do segundo grau",
                                "A equação não possui raízes reais"]),
        (["2", "1", "0", "-1"], ["A equação é do segundo grau",
                                 "A equação possui duas raízes reais", "-1.00", "1.00"]),
        (["2", "1", "1", "0"], ["A equação é do segundo grau",
                                "A equação possui duas raízes reais", "-1.00", "0.00"]),
        (["2", "1", "1", "1"], ["A equação é do segundo grau",
                                "A equação não possui raízes reais"]),
        (["2", "1", "2", "0"], ["A equação é do segundo grau",
                                "A equação possui duas raízes reais", "-2.00", "0.00"]),
        (["2", "2", "0", "0"], ["A equação é do segundo grau",
                                "A equação possui uma raiz real", "0.00"]),
    ]
)
def test_grau_2(monkeypatch: MonkeyPatch, test_input: list[str], expected_output: list[str]):
    mocked_input = lambda prompt="": test_input.pop(0)

    mocked_stdout = io.StringIO()

    with monkeypatch.context() as m:
        m.setattr(builtins, "input", mocked_input)
        m.setattr(sys, "stdout", mocked_stdout)

        sys.modules.pop("main", None)
        importlib.import_module(name="main", package="files")

    for output in expected_output:
        assert output in mocked_stdout.getvalue().strip()
