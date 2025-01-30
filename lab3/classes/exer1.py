class Uppersymbol:
    def getString(self):
        self.name = input()
    def printString(self):
        print(self.name.upper())
        
stroka = Uppersymbol()

stroka.getString()
stroka.printString()