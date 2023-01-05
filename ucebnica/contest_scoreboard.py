import sys

def main():
    number_of_cases = int(input())
    empty_space = input()
    array_of_contestants = []

    for tempInput in sys.stdin:
        counter = 0
        dictionary = {
            "id": 0,
            "number_of_problems": 0,
            "time": 0,
            "problems": [],
            "solved_problems": []
        }

        if tempInput == "\n":
            newlist = sorted(array_of_contestants, key=lambda d: (d['number_of_problems'], -d['time'], -d["id"]), reverse=True)
            for contestant in newlist:
                print(str(contestant["id"]) + " " + str(contestant["number_of_problems"]) + " " + str(contestant["time"]))
            print("")
            array_of_contestants = []

        if tempInput != "\n":
            line = tempInput.split(" ")
            if len(array_of_contestants) != 0:
                for contestant in array_of_contestants:
                    counter += 1
                    if int(line[0]) == contestant["id"]:
                        if line[3].replace("\n", "") == "C":
                            if line[1] in contestant["problems"] and line[1] not in contestant["solved_problems"]:
                                    contestant["time"] += 20
                            if line[1] not in contestant["solved_problems"]:
                                contestant["number_of_problems"] += 1
                                contestant["solved_problems"].append(line[1])
                                contestant["time"] += int(line[2])
                        elif line[3].replace("\n", "") == "I":
                            contestant["problems"].append(line[1])
                        counter = 0
                        break
                    if counter == len(array_of_contestants):
                        dictionary["id"] = int(line[0])
                        if line[3].replace("\n", "") == "C":
                            if line[1] not in contestant["solved_problems"]:
                                dictionary["number_of_problems"] += 1
                                dictionary["solved_problems"].append(line[1])
                                dictionary["time"] += int(line[2])
                        elif line[3].replace("\n", "") == "I":
                            dictionary["problems"].append(line[1])
                        array_of_contestants.append(dictionary)
                        counter = 0
                        break
            else:
                dictionary["id"] = int(line[0])
                if line[3].replace("\n", "") == "C":
                    dictionary["number_of_problems"] += 1
                    dictionary["solved_problems"].append(line[1])
                    dictionary["time"] += int(line[2])
                elif line[3].replace("\n", "") == "I":
                    dictionary["problems"].append(line[1])
                array_of_contestants.append(dictionary)

    newlist = sorted(array_of_contestants, key=lambda d: (d['number_of_problems'], -d['time'], -d["id"]), reverse=True)
    for contestant in newlist:
        print(str(contestant["id"]) + " " + str(contestant["number_of_problems"]) + " " + str(contestant["time"]))

if __name__ == "__main__":
    main()