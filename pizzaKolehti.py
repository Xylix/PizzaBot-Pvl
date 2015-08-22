pizzaList = []
velkaList = []
#order = (tilaaja, pizza, hinta)
def addOrder (user, pizza, order):
    paid = False
    pizzaList.append(    (user, pizza, order, paid)    )
addOrder ("xylix", "al-capone", 12)
addOrder ("Ege", "tropicana", 12)
