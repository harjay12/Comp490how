import os
import sys
import pytest
file_path = os.path.abspath(__file__)
cur_path = os.path.dirname(file_path)
project_path = os.path.dirname(cur_path)
sys.path.append(project_path)


@pytest.fixture
def main():
    import main
    return main


def test_ma_final_price(main):
    state = 'MA'
    a = [{'State': state, 'price': 175, 'type': 'Clothing'},
         {'State': state, 'price': 500, 'type': 'Wic Eligible food'},
         {'State': state, 'price': 6, 'type': 'everything else'}]
    assert main.final_price(state, a) == 701.3125


def test_me_final_price(main):
    state = 'ME'
    a = [{'State': state, 'price': 175, 'type': 'Clothing'},
         {'State': state, 'price': 500, 'type': 'Wic Eligible food'},
         {'State': state, 'price': 6, 'type': 'everything else'}]
    assert main.final_price(state, a) == 718.455


def test_all_and_nh_final_price(main):
    state = 'NH'
    a = [{'State': state, 'price': 175, 'type': 'Clothing'},
         {'State': state, 'price': 50, 'type': 'Wic Eligible food'},
         {'State': state, 'price': 6, 'type': 'everything else'}]
    assert main.final_price(state, a) == (175 + 50 + 6)
