from typing import List, Union, Any, Dict


def final_price(state: str, records: List[Dict]) -> Union[Union[str, int, float], Any]:
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
            return 'We do not provide tax info for this state pleas insert MA, ME, NH.'

        if state == 'MA' \
                and i['price'] > 175 \
                and (i['type'] == 'Clothing' or i['type'] == 'Wic Eligible food'):

            for item in item_prices:
                state_taxes = 0.0625 * (item - 175)
            total_after_tax = total_after_tax + state_taxes + item

        elif state == 'ME':
            for item in item_prices:
                state_taxes = 0.055 * item
            total_after_tax = total_after_tax + state_taxes + item

        elif state == 'NH':
            for item in item_prices:
                state_taxes = item
            total_after_tax = total_after_tax + state_taxes

        else:
            for item in item_prices:
                state_taxes = 0.0625 * item
            total_after_tax = total_after_tax + state_taxes + item

    return total_after_tax


if __name__ == '__main__':
    state = 'MA'
    items = [{'State': state, 'price': 175, 'type': 'Clothing'},
             {'State': state, 'price': 500, 'type': 'Wic Eligible food'},
             {'State': state, 'price': 6, 'type': 'everything else'}]
    total_charge = final_price(state, items)
    if type(total_charge) == float:
        print("{:.2f}".format(final_price(state, items)))
    else:
        print(total_charge)
