

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
        if ( topping == 'napolitana' ):
            print('Me encanta la de napolitana!')


