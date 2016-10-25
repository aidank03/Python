def item_order(order):
    
    new_order = order.split ( )

    numsalad = 0
    numburger = 0
    numwater = 0
    for i in new_order:
        if i == 'salad':
            numsalad += 1

        elif i == 'hamburger':
            numburger += 1

        elif i == 'water':
            numwater += 1
    
    return "salad:" + str(numsalad) + " hamburger:" + str(numburger) + " water:" + str(numwater)

