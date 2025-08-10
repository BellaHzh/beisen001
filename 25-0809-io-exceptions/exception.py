# Total with tax with exception handling and loop

def main():
    tax = 0.08875

    while True:
        subtotal = input('Enter subtotal: ').strip('$')
        try:
            subtotal = float(subtotal)
        except ValueError:
            print('Subtotal must be entered numerically.')
        except TypeError:
            print('type error')
        else:
            total = subtotal + subtotal * tax
            print(f'Total: ${total:,.2f}')
            break


main()
