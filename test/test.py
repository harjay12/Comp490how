import main


def test_ma_final_price():
    state = 'MA'
    a = [{'State': state, 'price': 175, 'type': 'Clothing'},
         {'State': state, 'price': 500, 'type': 'Wic Eligible food'},
         {'State': state, 'price': 6, 'type': 'everything else'}]
    assert main.final_price(state, a) == 723.1875


def test_me_final_price():
    state = 'ME'
    a = [{'State': state, 'price': 175, 'type': 'Clothing'},
         {'State': state, 'price': 500, 'type': 'Wic Eligible food'},
         {'State': state, 'price': 6, 'type': 'everything else'}]
    assert main.final_price(state, a) == 718.455


def test_all_and_nh_final_price():
    state = 'VA'
    a = [{'State': state, 'price': 175, 'type': 'Clothing'},
         {'State': state, 'price': 50, 'type': 'Wic Eligible food'},
         {'State': state, 'price': 6, 'type': 'everything else'}]
    assert main.final_price(state, a) == (175+50+6)
