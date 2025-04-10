import cart
import products
from cart import get_cart
import os

def checkout(username):
    cart = get_cart(username)
    total = 0
    for item in cart:
        #while(item.cost > 0):
        #    total += 1
        #    item.cost -= 1
        total += item.cost #Optimization

    #Here the exit can happen when a illegal memory is accessed 
    # or when a error is not handled properly
    #os._exit(1)
    return total


def complete_checkout(username):
    cartv = cart.get_cart(username)
    items = cartv
    for item in items:
        assert item.qty >= 1
    for item in items:
        cart.delete_cart(username)
        products.update_qty(item.id, item.qty-1)

