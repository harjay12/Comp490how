from typing import List, Any, Dict


def ma_taxes(ma_tax):
    total_after_tax = 0
    for item in ma_tax:
        state_taxes = 0.0625 * (item - 175)
        total_after_tax = total_after_tax + state_taxes + item
    return total_after_tax


def me_taxes(me_tax):
    total_after_tax = 0
    for item in me_tax:
        state_taxes = 0.055 * item
        total_after_tax = total_after_tax + state_taxes + item
    return total_after_tax


def nh_taxes(nh_tax):
    total_after_tax = 0
    for item in nh_tax:
        state_taxes = item
        total_after_tax = total_after_tax + state_taxes
    return total_after_tax


def final_price(state: str, records: List[Dict]) -> Any:
    item_prices = []
    total_after_tax = 0
    state_taxes = 0
    item = 0
    state_abb = ['NH', 'MA', 'ME']

    for i in records:
        item_prices.append(i['price'])
        if i['price'] < 0:
            return 'No Returned allowed'
        if state not in state_abb:
            return 'We do not provide tax info for this ' \
                   'state please insert MA, ME, or NH.'

        if state == 'MA' and i['price'] > 175 and (
                i['type'] == 'Clothing' or i['type'] == 'Wic Eligible food'):
            total_after_tax = ma_taxes(item_prices)
        else:
            for item in item_prices:
                state_taxes = 0.0625 * item
            total_after_tax = total_after_tax + state_taxes + item

        if state == 'ME':
            total_after_tax = me_taxes(item_prices)

        elif state == 'NH':
            total_after_tax = nh_taxes(item_prices)

    return total_after_tax


if __name__ == '__main__':
    state = 'MA'
    items = [{'State': state, 'price': 400, 'type': 'Clothing'},
             {'State': state, 'price': 2, 'type': 'Wic Eligible food'},
             {'State': state, 'price': 800, 'type': 'everything else'}]
    total_charge = final_price(state, items)
    if isinstance(total_charge, float):
        print("{:.2f}".format(final_price(state, items)))
    else:
        print(total_charge)
