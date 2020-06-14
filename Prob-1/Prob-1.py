# Module 8
#   Programming Assignment 11
#     Prob-1.py

# Your code below
class car:
    def __init__(self,make,model,year):
        self._make = make
        self._model = model
        self._year = year

    def set_make(self,make):
        self._make = make
    def get_make(self):
        return self._make
    def set_model(self,model):
        self._model = model
    def get_model(self):
        return self._model
    def set_year(self,year):
        self._year = year
    def get_year(self):
        return self._year

    
 
def Testcar():
   carlot = []
   carlot.append(car("toyota","tacoma","1994"))
   carlot.append(car("ford","f150","2008"))
   carlot.append(car("honda","accord","1990"))
   carlot.append(car("toyota","corolla","2005"))
   carlot.append(car("gmc","sierra","1999")) 
   print("Make---Model---Year")
   for vehicle in carlot:
      
       print(vehicle.get_make(),vehicle.get_model(),vehicle.get_year())
       print()
       
   for vehicle in carlot:
       vehicle.set_make(input("enter a make: "))
       vehicle.set_model(input("enter a model: "))
       vehicle.set_year(input("enter a year: "))
    
   for vehicle in carlot:
       print(vehicle.get_make(),vehicle.get_model(),vehicle.get_year())
       print()
    

Testcar()

if __name__ == "__main__":
    Testcar()