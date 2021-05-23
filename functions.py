def discounted (price, discount, max_discount=50):
    price = abs(float(price))
    discount = abs (float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError("Ошибка")
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount/100
    return (price_with_discount)

product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0,
        'discount': 70}

product["with_discount "]= discounted(product['price'], product['discount'], max_discount=80)
print (product)

discounted(100,50,max_discount=100)
