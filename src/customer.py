import tabulate
class Customer:

    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
        #print all with tabulate
        print(tabulate.tabulate([["Name", "Status"], [self.name, self.status]], headers="firstrow")) 
        
        
