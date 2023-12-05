#!/usr/bin/env python3


def get_y_or_n(prompt):
    while True:
        answer = input(prompt).lower()
        if answer == 'y' or answer == 'n':
            return answer


if __name__ == '__main__':

    MONDAY_DISCOUNT = 10
    MONDAY_DISCOUNT_AMOUNT = 50.0
    APP_DISCOUNT = 5

    try:
        spend = float(input('How much is being spent? '))
        if spend <= 0:
            print('Error: Spend cannot be 0 or lower.')
        else:
            is_monday = get_y_or_n('Is it Monday? (y/n) ')

            if is_monday == 'y' and spend > MONDAY_DISCOUNT_AMOUNT:
                discount = spend / MONDAY_DISCOUNT
                charge = spend - discount
            else:
                charge = spend

            if charge > 10:
                used_app = get_y_or_n('Did they use the app? ')

                if used_app == 'y':
                    charge -= APP_DISCOUNT

            print(f'Amount to Charge: £{charge:.2f}')

    except ValueError:
        print('Error: Spend must be an integer.')
