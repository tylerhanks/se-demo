from se_demo.math import times
import random
import pytest


def test_times():
    assert times(2.2, 3.7) == 8.14
    for _ in range(10):
        x = random.random()
        assert times(x, 1.0) == pytest.approx(x)
    for _ in range(10):
        x = random.random()
        assert times(1.0, x) == pytest.approx(x)
    for _ in range(10):
        x = random.random()
        assert times(x, 0.0) == pytest.approx(0.0)
    for _ in range(10):
        x = random.random()
        assert times(0.0, x) == pytest.approx(0.0)
