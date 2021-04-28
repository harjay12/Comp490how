from typing import List, Union, Any, Dict


def final_price(state: str, records: List[Dict]) -> Union[Union[str, int, float], Any]:
    item_prices = []
    total_after_tax = 0
    state_taxes = 0
    item = 0
    state_abb = ['NH','MA','ME']

    for i in records:
        if i['price'] < 0:
            return 'No Returned allowed'
        if state not in state_abb:
            return 'We do not provide tax info for this state pleas insert MA, ME, NH.'
        elif i['State'] == state \
                and state == 'MA' \
                and i['price'] >= 175 \
                and (i['type'] == 'Clothing' or i['type'] == 'Wic Eligible food'):
            item_prices.append(i['price'])
            for item in item_prices:
                state_taxes = 0.0625 * (item-175)
            total_after_tax = total_after_tax + state_taxes + item

        elif i['State'] == state \
                and state == 'ME':
            item_prices.append(i['price'])
            for item in item_prices:
                state_taxes = 0.055 * item
            total_after_tax = total_after_tax + state_taxes + item

        else:
            item_prices.append(i['price'])
            for item in item_prices:
                state_taxes = item
            total_after_tax = total_after_tax + state_taxes

    return total_after_tax


if __name__ == '__main__':
    state = 'MA'
    items = [{'State': state, 'price': 400, 'type': 'Clothing'},
             {'State': state, 'price': 2, 'type': 'Wic Eligible food'},
             {'State': state, 'price': 800, 'type': 'everything else'}]
    print(final_price(state, items))
