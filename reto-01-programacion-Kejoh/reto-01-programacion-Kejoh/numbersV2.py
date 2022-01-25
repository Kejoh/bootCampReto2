class zero:
    top = " __ "
    tal = "|  |"
    mid = "|  |"
    med = "|  |"
    bot = "|__|"

class one:
    top = "    "
    tal = "   |"
    mid = "   |"
    med = "   |"
    bot = "   |"

class two:
    top = " __ "
    tal = "   |"
    mid = " __|"
    med = "|   "
    bot = "|__ "

class three:
    top = " __ "
    tal = "   |"
    mid = " __|"
    med = "   |"
    bot = " __|"

class four:
    top = "   "
    tal = "| |"
    mid = "|_|"
    med = "  |"
    bot = "  |"

class five:
    top = " __ "
    tal = "|   "
    mid = "|__ "
    med = "   |"
    bot = " __|"

class six:
    top = " __ "
    tal = "|   "
    mid = "|__ "
    med = "|  |"
    bot = "|__|"

class seven:
    top = "  __ "
    tal = "    |"
    mid = "    |"
    med = "    |"
    bot = "    |"

class eight:
    top = " __ "
    tal = "|  |"
    mid = "|__|"
    med = "|  |"
    bot = "|__|"

class nine:
    top = " __ "
    tal = "|  |"
    mid = "|__|"
    med = "   |"
    bot = "   |"

def printnum(list):
    chunks = ['top','tal','mid','med','bot']
    for section in chunks:
        string = ''
        for x in list:
            if x == '1':
                string += getattr(one, section)
            elif x == '2':
                string += getattr(two, section)
            elif x == '3':
                string += getattr(three, section)
            elif x == '4':
                string += getattr(four, section)
            elif x == '5':
                string += getattr(five, section)
            elif x == '6':
                string += getattr(six, section)
            elif x == '7':
                string += getattr(seven, section)
            elif x == '8':
                string += getattr(eight, section)
            elif x == '9':
                string += getattr(nine, section)
            elif x == '0':
                string += getattr(zero, section)
            elif x == 'Quit':
                break
            else:
                print("Number not entered")
        print(string)

x = input("Type the number you would like printed: ")
a = list(x)

printnum(a)