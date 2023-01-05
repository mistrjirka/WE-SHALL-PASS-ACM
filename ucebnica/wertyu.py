import sys

def translate(c):
	if c == '1':
		return '`'
	elif c ==  '2':
		return '1'
	elif c == '3':
		return '2'
	elif c == '4':
		return '3'
	elif c == '5':
		return '4'
	elif c == '6':
		return '5'
	elif c == '7':
		return '6'
	elif c == '8':
		return '7'
	elif c == '9':
		return '8'
	elif c == '0':
		return '9'
	elif c == '-':
		return '0'
	elif c == '=':
		return '-'
	elif c == 'W':
		return 'Q'
	elif c == 'E':
		return 'W'
	elif c == 'R':
		return 'E'
	elif c == 'T':
		return 'R'
	elif c == 'Y':
		return 'T'
	elif c == 'U':
		return 'Y'
	elif c == 'I':
		return 'U'
	elif c == 'O':
		return 'I'
	elif c == 'P':
		return 'O'
	elif c == '[':
		return 'P'
	elif c == ']':
		return '['
	elif c == '\\':
		return ']'
	elif c == 'S':
		return 'A'
	elif c == 'D':
		return 'S'
	elif c == 'F':
		return 'D'
	elif c == 'G':
		return 'F'
	elif c == 'H':
		return 'G'
	elif c == 'J':
		return 'H'
	elif c == 'K':
		return 'J'
	elif c == 'L':
		return 'K'
	elif c == ';':
		return 'L'
	elif c == '\'':
		return ';'
	elif c == 'X':
		return 'Z'
	elif c == 'C':
		return 'X'
	elif c == 'V':
		return 'C'
	elif c == 'B':
		return 'V'
	elif c == 'N':
		return 'B'
	elif c == 'M':
		return 'N'
	elif c == ',':
		return 'M'
	elif c == '.':
		return ','
	elif c == '/':
		return '.'
	elif c == ' ':
		return ' '
	elif c == '\n':
		return '\n'
	elif c == " ":
		return " "

if __name__ == "__main__":
    for tempInput in sys.stdin:
        line = list(tempInput)
        for element in line:
            for char in element:
                encoded_char = translate(char)
                print(encoded_char, end="")