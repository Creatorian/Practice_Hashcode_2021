from main import getPizzas
import pprint

pp = pprint.PrettyPrinter(indent=4)
pizzas, ing, params= getPizzas()

pizzaNum = int(params.split()[0])
dvajca = int(params.split()[1])
trojca = int(params.split()[2])
chetvorica = int(params.split()[3])

team2 = []
team3 = []
team4 = []
numPizzas = 0
pp.pprint(pizzas)
pp.pprint(ing)
teamPizzas = {
    2: [],
    3: [],
    4: []
}

pizzaSizes = list(pizzas.keys())
teamNumbers = 0
while pizzaNum != 0:
    print(pizzaNum)
    print('dvajca: {} trojca: {} 4ica: {}'.format(dvajca, trojca, chetvorica))
    if pizzaNum % 2 != 0 and trojca != 0:
        teamSize = 3
        trojca = trojca - 1
    elif chetvorica != 0:
        teamSize = 4
        chetvorica = chetvorica - 1
    elif dvajca != 0:
        teamSize = 2 
        dvajca = dvajca - 1
    elif trojca !=0:
        teamSize = 3 
        trojca = trojca - 1
    else:
        break
    tempPizzas = []
    najgolemBroj = pizzas[pizzaSizes[0]]

    #print("Najgolem Broj")
    #pp.pprint(najgolemBroj)
    for i in range(teamSize):
        print(i)
        if not najgolemBroj:
            print('Nema vekje pici')
            #print(pizzaSizes)
            pizzaSizes.pop(0)
            if not pizzaSizes:
                break
            najgolemBroj = pizzas[pizzaSizes[0]]
        tempPizzas.append(najgolemBroj[0]['index'])
        najgolemBroj.pop(0)
        numPizzas = numPizzas + 1

    if not pizzaSizes:
        break
    pizzaNum = pizzaNum - teamSize
    
    teamNumbers = teamNumbers + 1
    teamPizzas[teamSize].append(tempPizzas)


pp.pprint(teamPizzas)

f = open('a_reshenie.txt', 'w')

f.write('{} \n'.format(teamNumbers))
for key in teamPizzas:
    for pizza in teamPizzas[key]:
        convertedPizza = [str(elem) for elem in pizza]
        convertedPizza.append('\n') 
        saveString = " "
        saveString = saveString.join(convertedPizza)
        f.write('{} {}'.format(key, saveString))
