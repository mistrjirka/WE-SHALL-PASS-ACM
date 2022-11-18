def getMultipleInputs(num_of_inputs, question):
    result = []
    while len(result) != num_of_inputs:
        # stolen from https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
        result = [int(x) for x in input(question).split()]
    return result


elements = [(3, 2), (-20, 5), (-5, -10)]


def whereCanGo(h, a, cur_element):
    results = []
    for ind, element in enumerate(elements):
        if ind != cur_element:
            if h+element[0] > 0 and a+element[1] > 0:
                results.append(ind)
    return results


def apply_damage(h, a, el):
    return (h-el[0], a - el[1])


def heuristic(h, a, element):
    pass


memoize = [[[None for i in range(2100)]for i in range(2100)]for i in range(4)]


def future_search(options, h, a, el=3, survived=0):
    best_value = -1
    # if memoize[el][h][a] is not None:
    #    return memoize[el][h][a]

    if len(options) == 0:
        return survived

    for option in options:
        h_tmp = h+elements[option][0]
        a_tmp = a+elements[option][1]
        value = future_search(whereCanGo(h_tmp, a_tmp, option),
                              h_tmp, a_tmp, el=option, survived=survived+1)
        if value > best_value:
            best_value = value
    #memoize[el][h][a] = best_value
    return best_value


health_targeted = 2
armor_targeted = 1


def target(h, a, option, itteration=0):
    availible_options = whereCanGo(h, a, option)
    if len(availible_options) == 0:
        return itteration
    if len(availible_options) == 1:
        return target(h+elements[availible_options[0]][0], a+elements[availible_options[0]][1], availible_options[0], itteration+1)
    if 0 in availible_options:
        return target(h+elements[0][0], a+elements[0][1], 0, itteration+1)
    else:
        proportion_of_health = h/a
        if proportion_of_health < 4-0.3:
            return target(h+elements[health_targeted][0], a+elements[health_targeted][1], health_targeted, itteration+1)
        elif proportion_of_health > 4+0.3:
            return target(h+elements[armor_targeted][0], a+elements[armor_targeted][1], armor_targeted, itteration+1)
        else:
            return target(h+elements[health_targeted][0], a+elements[health_targeted][1], health_targeted, itteration+1)
    return itteration


if __name__ == '__main__':
    num_of_inputs = int(input())
    cases = []
    results = []
    for i in range(num_of_inputs):
        cases.append(getMultipleInputs(2, ""))

    for case in cases:
        health = case[0]
        armor = case[1]
        possible_moves = whereCanGo(health, armor, 3)
        result = target(health, armor, 3)
        #result = future_search(possible_moves, health, armor)

        results.append(result)

    for result in results:
        print(result)
