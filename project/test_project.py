import pytest
from project import compute_price_change, compare_to_official_inflation, load_history, save_price


def test_compute_price_change_increase():
    assert compute_price_change(100, 110) == 10.0


def test_compute_price_change_decrease():
    assert compute_price_change(100, 90) == -10.0


def test_compute_price_change_zero_old_price():
    with pytest.raises(ValueError):
        compute_price_change(0, 100)


def test_compare_to_official_inflation_above():
    result = compare_to_official_inflation(10, 4.5)
    assert "plus vite" in result


def test_compare_to_official_inflation_below():
    result = compare_to_official_inflation(2, 4.5)
    assert "moins vite" in result


def test_save_and_load_history(tmp_path):
    filename = tmp_path / "test_history.csv"
    save_price(filename, "huile_1L", 15.0)
    save_price(filename, "huile_1L", 16.5)
    history = load_history(filename, "huile_1L")
    assert len(history) == 2
    assert history[-1][1] == 16.5
