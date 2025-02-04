class StringUpper:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printSTRING(self):
        print(self.text.upper())


obj = StringUpper()
obj.getString()
obj.printSTRING()
