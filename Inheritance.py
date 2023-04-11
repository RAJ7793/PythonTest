

class Computer:
    
    def __init__(self, ram, processor, memory):
        self.ram = ram
        self.processor = processor
        self.memory = memory

    def getspecs(self):
        print("please enter the details")
        self.ram = input("Enter ram size :")
        self.processor = input("Enter processor size :")
        self.memory = input("Enter the memory size :")




    def displayspaces(self):
        print("Here are the display spaces")
        print(f'Ram size is {self.ram}, Processor size is {self.processor}, Memory size is {self.memory}')





class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor
    def get_case_color_details(self):
        self.casecolor = input("Enter the case color :")

    def put_case_details(self):
        print(f'Case color is {self.casecolor}')

class Laptop(Computer):

    def __int__(self, weight):
        self.weight = weight

    def get_weight(self):
        self.weight = input("Enter weight :")
    def displayweight(self):
        print(f"Weight is : {self.weight}")

comp = Laptop('', '', '')
comp.getspecs()
comp.get_weight()
comp.displayspaces()
comp.displayweight()

