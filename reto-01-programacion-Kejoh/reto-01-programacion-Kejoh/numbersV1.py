class cero:
    top = " _ "
    mid = "| |"
    bot = "|_|"

class uno:
    top = "  "
    mid = " |"
    bot = " |"

class dos:
    top = " _ "
    mid = " _|"
    bot = "|_ "

class tres:
    top = " _ "
    mid = " _|"
    bot = " _|"

class cuatro:
    top = "   "
    mid = "|_|"
    bot = "  |"

class cinco:
    top = " _ "
    mid = "|_ "
    bot = " _|"

class seis:
    top = " _ "
    mid = "|_ "
    bot = "|_|"

class siete:
    top = " _ "
    mid = "  |"
    bot = "  |"

class ocho:
    top = " _ "
    mid = "|_|"
    bot = "|_|"

class nueve:
    top = " _ "
    mid = "|_|"
    bot = "  |"

def printnum(list):
    chunks = ['top','mid','bot']
    for section in chunks:
        string = ''
        for x in list:
            if x == '1':
                string += getattr(uno, section)
            elif x == '2':
                string += getattr(dos, section)
            elif x == '3':
                string += getattr(tres, section)
            elif x == '4':
                string += getattr(cuatro, section)
            elif x == '5':
                string += getattr(cinco, section)
            elif x == '6':
                string += getattr(seis, section)
            elif x == '7':
                string += getattr(siete, section)
            elif x == '8':
                string += getattr(ocho, section)
            elif x == '9':
                string += getattr(nueve, section)
            elif x == '0':
                string += getattr(cero, section)
            elif x == 'Quit':
                break
            else:
                print("Number not entered")
        print(string)

x = input("Type the number you would like printed: ")
a = list(x)

printnum(a)