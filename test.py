from tud_test_base import set_keyboard_input, get_display_output

from main import tip_calculate

from main import get_inputs


def test_case_1_tip_calculate():

    assert round(tip_calculate(124.56, 0.12, 7), 2) == 19.93


def test_case_1_get_input():

    set_keyboard_input(["124.56", "12", "7"])

    assert get_inputs() == (124.56, 0.12, 7)
