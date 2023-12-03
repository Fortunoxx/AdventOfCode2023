import pytest

from src.day01 import solve_part1, solve_part2

day = "01"


@pytest.mark.parametrize("day", [day])
def test_part1(day, expected_value=142):
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample.dat"}
    assert solve_part1(testdata) == expected_value


@pytest.mark.parametrize("day", [day])
def test_part2(day, expected_value=281, has_extra_file=True):
    suffix = ""
    if has_extra_file:
        suffix = "-2"
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample{suffix}.dat"}
    assert solve_part2(testdata) == expected_value
