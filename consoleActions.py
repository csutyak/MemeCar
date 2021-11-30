class consoleActions:
    def __init__(self):
        self.resetAllFlags()

    def resetAllFlags(self):
        self.exitFlag = False

        self.saveFlag = False
        self.saveName = ""
        self.loadFlag = False
        self.loadName = ""

        self.printEpFlag = False
        self.printHSFlag = False
        self.printGameFlag = False

        self.setEpFlag = False
        self.setEpValue = 0
        
    def parseConsoleActions(self, userInput):
        if userInput == "exit":
            self.exitFlag = True
        #save
        elif userInput == "save":
            userInput = input("Save Name>")
            self.saveName = userInput
            self.saveFlag = True
        #load
        elif userInput == "load":
            userInput = input("load Name>")
            self.loadName = userInput
            self.loadFlag = True
        #print EP
        elif userInput == "print ep":
            self.printEpFlag = True
        #print Highest Score
        elif userInput == "print hs":
            self.printHSFlag = True
        #set EP
        elif userInput == "set ep":
            userInput = input("EP Value>")
            self.setEpValue = float(userInput)
            self.setEpFlag = True
        elif userInput == "print game":
            self.printGameFlag = True
        else:
            print("valid options are:")
            print("  exit")
            print("  save")
            print("  load")
            print("  print ep")
            print("  print hs")
            print("  set ep")
            print("  print game")
    
    def getExitFlag(self):
        return self.exitFlag
    
    def getSaveFlag(self):
        if self.saveFlag == False:
            return False, ""
        else:
            self.saveFlag = False
            print("Saving... ", self.saveName)
            return True, self.saveName
    
    def getLoadFlag(self):
        if self.loadFlag == False:
            return False, ""
        else:
            self.loadFlag = False
            print("Loading... ", self.loadName)
            return True, self.loadName

    #print EP
    def getPrintEpFlag(self):
        if self.printEpFlag == False:
            return False
        else:
            self.printEpFlag = False
            return True
    #print Highest Score
    def getHSFlag(self):
        if self.printHSFlag == False:
            return False
        else:
            self.printHSFlag = False
            return True
    #set EP
    def getSetEpFlag(self):
        if self.setEpFlag == False:
            return False, ""
        else:
            self.setEpFlag = False
            print("Setting EP Value... ", self.setEpValue)
            return True, self.setEpValue
    
    def getPrintGameNumFlag(self):
        if self.printGameFlag == False:
            return False
        else:
            self.printGameFlag = False
            return True

