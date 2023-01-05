import sys


def load_input(plain_text_arr):
    text_arr = []
    for tempInput in sys.stdin:
        dictionary = {}
        line = tempInput.replace("\n", "").split(" ")
        text_arr.append(line)
        if tempInput == "\n":
            successful_texts = decode(plain_text_arr, text_arr)
            for text in successful_texts:
                for i in range(len(text)):
                    for j in range(len(text[i])):
                        if text[i][j] in dictionary:
                            if dictionary[text[i][j]] != plain_text_arr[i][j]:
                                dictionary = {}
                                break
                        else:
                            dictionary[text[i][j]] = plain_text_arr[i][j]
                if len(dictionary) == 26:
                    break
            if dictionary:
                no_solution = False
                for text in text_arr:
                    strings = []
                    for word in text:
                        string = ""
                        for letter in word:
                            if letter in dictionary:
                                string = dictionary[letter] + string
                            else:
                                print("No solution.")
                                print("")
                                no_solution = True
                                break
                        strings.append(string[::-1])
                        if no_solution == True:
                            break
                    if no_solution == False:
                        for i in range(len(strings)):
                            if i != 0:
                                print(" ", end="")
                            print(strings[i], end="")
                        print("")
                    else:
                        break
            else:
                print("No solution.")
                print("")
            text_arr = []
    return text_arr


def verify_size_of_words_in_arrays(text, plain_text_arr):
    idx = 0
    for word in text:
        if len(word) == len(plain_text_arr[idx]):
            idx += 1
        else:
            return False
    return True

def decode(plain_text_arr, text_arr):
    successful_texts = []
    for text in text_arr:
        if len(text) == len(plain_text_arr):
            if verify_size_of_words_in_arrays(text, plain_text_arr) == True:
                successful_texts.append(text)
    return successful_texts

def main():
    plain_text = "the quick brown fox jumps over the lazy dog"
    plain_text_arr = plain_text.split(" ")
    idx = 0
    num_of_cases = int(input())
    empty = input()
    dictionary = {}

    text_arr = load_input(plain_text_arr)
    successful_texts = decode(plain_text_arr, text_arr)

    for text in successful_texts:
        for i in range(len(text)):
            for j in range(len(text[i])):
                if text[i][j] in dictionary:
                    if dictionary[text[i][j]] != plain_text_arr[i][j]:
                        dictionary = {}
                        break
                else:
                    dictionary[text[i][j]] = plain_text_arr[i][j]
        if len(dictionary) == 26:
            break
    if dictionary:
        no_solution = False
        for text in text_arr:
            strings = []
            for word in text:
                string = ""
                for letter in word:
                    if letter in dictionary:
                        string = dictionary[letter] + string
                    else:
                        print("No solution.")
                        no_solution = True
                        break
                strings.append(string[::-1])
                if no_solution == True:
                    break
            if no_solution == False:
                for i in range(len(strings)):
                    if i != 0:
                        print(" ", end="")
                    print(strings[i], end="")
                print("")
            else:
                break
    else:
        print("No solution.")

if __name__ == "__main__":
    main()