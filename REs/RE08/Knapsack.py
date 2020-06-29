def inner(money, products, wishlist, result={}):
    if len(wishlist) == 0:
        return money, result
    else:
        current, quantity = wishlist.popitem()
        quantity -= 1
        if quantity > 0:
            wishlist[current] = quantity
        price = products[current]

        money1 = money - price
        if money1 >= 0:
            result1 = result.copy()
            result1[current] = result1.get(current, 0) + 1
            wishlist1 = wishlist.copy()
            (money1, result1) = inner(money1, products, wishlist1, result1)

            money2 = money
            result2 = result.copy()
            wishlist2 = wishlist.copy()
            (money2, result2) = inner(money2, products, wishlist2, result2)

            if money1 > money2:
                result = result2
                money = money2
                wishlist = wishlist2
            else:
                result = result1
                money = money1
                wishloist = wishlist1
            print(current)
            return money, result
        else:
            return inner(money, products, wishlist, result)


def knapsack(money, products, wishlist):
    _, result = inner(money, products, wishlist)
    return result