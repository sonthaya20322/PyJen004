import subprocess
import sys

from calculator import add


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-4, -6) == -10


def test_add_zero():
    assert add(0, 7) == 7


def test_add_floats():
    assert abs(add(0.1, 0.2) - 0.3) < 1e-9


def test_program_runs_and_prints_result():
    result = subprocess.run(
        [sys.executable, "calculator.py", "10", "20"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "10 + 20 = 30" in result.stdout


def test_program_shows_decimals_when_needed():
    result = subprocess.run(
        [sys.executable, "calculator.py", "1.5", "2"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "1.5 + 2 = 3.5" in result.stdout
