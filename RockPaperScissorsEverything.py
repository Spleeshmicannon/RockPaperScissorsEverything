import json
# defining the options class
# (i.e. the object for rock/paper etc.)
class Option:
    def __init__(self, _option, _win, _lose):
        self.option = _option
        self.win = _win
        self.lose = _lose

# reads the JSON file and spits out contents from 'filename'
def readFile(filename):
    with open(filename, 'r') as jsonFile:
        jsonData = json.load(jsonFile)
        options = []
        for i in range(len(jsonData) - 1):
            options.append(Option(jsonData["options"][i], jsonData[jsonData["options"][i]]["win"], jsonData[jsonData["options"][i]]["lose"]))

        return options

Data = readFile("options.JSON")

def readUserInput(userInput):
    if(userInput == "help"):
        print("commands:\n\thelp - prints the help message\n\tfindVictor [option0] [option1]; - finds the victor\n\tprintwl [option]; - prints relavent wins and losses")

    chars = ""
    fv = False
    printwl = False
    whichOption = 0
    option0 = ""
    option1 = ""
    for char in userInput:
        if(chars == "findVictor "):
            fv = True
            chars = ""
        if(chars == "printwl "):
            printwl = True
            chars = ""

        if((printwl) and (char == ";")):
            for item in Data:
                if(item.option == chars):
                    print("wins: ", item.win)
                    print("Loses: ", item.lose)

        if((fv) and ((char == " ") or (char == ";"))):
            if(whichOption == 1):
                option1 = chars
                for option in Data:
                    if(option.option == option0):
                        for win in option.win:
                            if(win == option1):
                                print(option0, "is the victor")
                                return
                        print(option1, "is the victor")
                        return
                break
            else:
                option0 = chars
                chars = ""
                whichOption += 1
                continue
        chars += char


programRunning = True
while programRunning:
    userInput = input("> ")
    readUserInput(userInput)
