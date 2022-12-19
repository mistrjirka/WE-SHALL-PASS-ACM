import sys

if __name__ == "__main__":
    keyboard ="`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
    for n in sys.stdin:
        series = n.strip("\n")
        newstring = ""
        for i, character in enumerate(series):
            if(character == " "):
                newstring += " "
            else:
                pos_on_keyboard = keyboard.find(character)
                if pos_on_keyboard == -1:
                    raise ValueError("character "+character+" is missing" )
                newstring += keyboard[pos_on_keyboard - 1]
        print(newstring)
            
