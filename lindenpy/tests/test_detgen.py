from lindenpy.detgen import DetGen
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (0, "A"),
        (1, "AB"),
        (2, "ABA"),
        (3, "ABAAB"),
        (4, "ABAABABA"),
        (5, "ABAABABAABAAB"),
        (6, "ABAABABAABAABABAABABA"),
        (7, "ABAABABAABAABABAABABAABAABABAABAAB"),
    ],
)
def test_gen_returns_correct_string(test_input, expected):
    g = DetGen("A", {"A": "AB", "B": "A"})
    assert g.gen(test_input) == expected
