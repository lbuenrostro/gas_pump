import gas_core

def test_cal_money():
    assert gas_core.cal_money(1, 2.07) == 2.07
    assert gas_core.cal_money(20, 2.07) == 41.4
    assert gas_core.cal_money(10, 2.07) == 20.7
