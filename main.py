import pprint
from itertools import combinations_with_replacement  

pp = pprint.PrettyPrinter(indent=4)
class Pizzas:
    def __init__(self):
        self.ing = []
        self.pizzas = []
ing = []

def filterIngs(curIng):
    if curIng in ing:
        return False
    else:
        return True

def getPizzas():
    f = open('data/a_example', 'r')
    params = f.readline()
    print(params) 
    pizzas = {}
    pizzaIndex = 0

    for line in f.readlines():
        #print(line)
        key = int(line.split()[:1][0])
        pizza = line.split()[1:]
        filteredIngs = filter(filterIngs, pizza)
        pizzaDict = {
            'pizzaIng': pizza,
            'index': pizzaIndex
        }
        for i in filteredIngs:
            ing.append(i)
        if key in pizzas:
            pizzas[key].append(pizzaDict)
        else:
            pizzas[key] = []
            pizzas[key].append(pizzaDict)
        pizzaIndex = pizzaIndex + 1
    return pizzas, ing, params

if __name__ == '__main__':
    pizzas, ing = getPizzas()
    pp.pprint(pizzas) 
    pp.pprint(ing)

#    pp.pprint(pizzas)
#    print('Num Ing: {}, Ings: {}'.format(len(ing), ing))
#      
#    pizzaSizes = list(pizzas.keys())
#    numIngs = len(ing) 
#    #TODO
#    #Ova nemora da bide range, tuku samo kje gi soberam site keys od pizza dict-ot, za da nemora posle da chistam
#    ings = range(1, numIngs + 1) 
#    print('sizes: {}'.format(pizzaSizes)) 
#
#    allCombs = {}
#    for teams in range(2,5):
#        comb = combinations_with_replacement(ings, teams)
#        for val in comb:
#            flag = False
#            Sum = sum(val)  
#            
#            for i in val:
#                if i not in pizzaSizes:
#                    flag = True
#
#            if not flag:
#                if Sum not in allCombs:
#                    allCombs[Sum] = []
#                allCombs[Sum].append(list(val))
#   
#    print('All combs')
#    pp.pprint(allCombs)
    #Do tuka gi imam izgenerirano site mozhni kombinacii na pici, isfiltrirani, taka da samo mozhnite pici se tuka, i posle ova sleden chekor e dodeluvanjeto na picite
