def getMultipleInputs(num_of_inputs, question):
    result = []
    valid = False
    while len(result) != num_of_inputs and not valid:
        #stolen from https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
        result = [int(x) for x in input(question).split()]
    return result

def find_index_of(arr, item, key):
    for i, it in enumerate(arr):
        if it[key] == item:
            return i
    return -1

def isCheapest(prices, city):
    index = find_index_of(prices, city, 1)
    if index == 0:
        return (True, index)
    elif index != 0 and prices[0][0] == prices[index][0]:
        return (True, index)
    return (False, index)

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

def calculatePriceOfWay(way,cities_prices, fueltank, start_city_index, goal_city_index):
    price = 0
    fuel_to_burn = 0
    cities = []
    for ind,road in enumerate(way):
        fuel_to_burn += road[2]
        cities.append((cities_prices[road[start_city_index]], road[start_city_index]))

    cities.sort(key=lambda x: x[1])
    
    fuel_left = 0
    
    for ind, road in enumerate(way):
        (cheapest_city, city_position) = isCheapest(cities,road[start_city_index])
        fuel_to_buy = 0
        if cheapest_city:
            fuel_to_buy = clamp(fuel_to_burn-fuel_left, 0, fueltank - fuel_left)
            price += cities[city_position][0]*fuel_to_buy
        elif fuel_left < road[2]:
            #we have to buy
            fuel_to_buy = road[2]
            if len(cities)-1 > city_position and fuel_to_buy <= fueltank:
                for i in range(len(cities)):
                    fuel_to_buy += way[ind+1][2]
                    fuel_to_buy = clamp(fuel_to_burn, 0, fueltank - fuel_left)
                    price += (cities[city_position][0]- fuel_left)*fuel_to_buy

        fuel_left += fuel_to_buy - road[2]
        fuel_to_burn -= road[2]
        cities.pop(city_position)
    return price

def find_cheapest_road(start, end, roads, fueltank, cities_prices):
    goal_city_index = 1 if start < end else 0
    start_city_index = 0 if start < end else 1
    way_levels = []
    ways = []
    roads_remaining = list(roads)
    runned_out_of_lower = False
    found_start_road = False
    found_road_level = False
    max_cycles = 10
    cycle = 0
    to_remove = []
    for ind, road in enumerate(roads): #removing roads we don't have fuel for
        if road[2] > fueltank:
            to_remove.append(ind)
            
    for ind in sorted(to_remove, reverse=True):
        del roads_remaining[ind]
    
    searching_for_cities = [start]
    
    while len(searching_for_cities) > 0 and cycle < max_cycles and len(roads_remaining) > 0 and not (end in searching_for_cities and len(searching_for_cities) == 1):
        level = []
        newsearch = []
        for i,road in enumerate(roads_remaining):
            if(road[start_city_index] in searching_for_cities):
                level.append(road)
                newsearch.append(road[goal_city_index])
        searching_for_cities = list(newsearch)
        if(len(level) > 0):
            way_levels.append(list(level))
        cycle+= 1
    
    to_keep = [end]
    for i in range(len(way_levels)-1,-1, -1):
        new_to_keep = []
        for ind,road in enumerate(way_levels[i]):
            if road[goal_city_index] in to_keep:
                foundOldWay = False
                for way in ways:
                    if way[0][start_city_index] == road[1]:
                        way.insert(0,road)
                        foundOldWay = True
                if not foundOldWay:
                    ways.append([road])
                new_to_keep.append(road[start_city_index])
        new_to_keep.append(end)
        to_keep = list(new_to_keep)
    
    if len(ways) == 0: # no way found
        return -1
    #calculating price of ways
    lowestPrice = [calculatePriceOfWay(ways[0],cities_prices, fueltank, start_city_index, goal_city_index), ways[0]]
    for way in ways:
        calculatedPrice = calculatePriceOfWay(way,cities_prices, fueltank, start_city_index, goal_city_index)
        if(calculatedPrice < lowestPrice[0]):
            lowestPrice = [calculatedPrice, way]
    return lowestPrice[0]

if __name__ == '__main__':
    num_of_roads = 0
    num_of_cities = 0
    to_solve = 0
    cities_prices = [] # (city1, city2, price)
    roads_cost = []
    queries = []

    (num_of_cities, num_of_roads) = getMultipleInputs(2, "")
    cities_prices = getMultipleInputs(num_of_cities, "")
    
    for i in range(num_of_roads):
        roads_cost.append(getMultipleInputs(3, ""))
    
    to_solve = int(input())

    for i in range(to_solve):
        queries.append(getMultipleInputs(3, ""))

    for query in queries:
        fueltank = query[0]
        start = query[1]
        end   = query[2]
        cheapest = find_cheapest_road(start,end,roads_cost,fueltank,cities_prices)
        if cheapest == -1:
            print("impossible")
        else:
            print(cheapest)