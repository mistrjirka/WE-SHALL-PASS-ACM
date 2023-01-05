import sys

def main():
    words = []
    for tmpInput in sys.stdin:
        word = tmpInput
        words.append("".join(sorted(word.replace("\n", ""))))
    for i in range(0, len(words), 2):
        word1 = words[i]
        word2 = words[i + 1]

        #word1 = longer
        #word2 = shorter        
        if len(word1) < len(word2):
            word1 = words[i + 1]
            word2 = words[i]
        word1_dic = {}
        word2_dic = {}
        for k in range(len(word1)):
            word1_dic[word1[k]] = word1_dic.get(word1[k], 0) + 1
        for k in range(len(word2)):
            word2_dic[word2[k]] = word2_dic.get(word2[k], 0) + 1

        for element in word1_dic:
            if element in word2_dic:
                value = word1_dic.get(element)
                if word1_dic.get(element) > word2_dic.get(element):
                    value = word2_dic.get(element)
                for j in range(value):
                    if element != " ":
                        print(element, end="")
        print("")

if __name__ == "__main__":
    main()