#class Namaj:
   # def __init__(self , Time , Oaktho_Name , Date):
     #   self.Time = Time
   #     self.Oaktho_Name = Oaktho_Name
       # self.Date = Date
     
    #def __str__(self):
      #   return "The Salah is the most valuable for all muslims.which time in every weeks at {}pm and its {}.#Today is Fryday on {} has a Jummah.".format(self.Time ,self.Oaktho_Name , self.Date)   
        
##p1= Namaj(12 , 'Jummah' , 12)
#print(p1)
class Person:
    def __init__(self, fname , lname):
        self.firstname = fname
        self.lname = lname
        
        
    def printname(self):
        print(self.firstname , self.lname)
        
#Use the Person class to creat an object, and then execute the printname method:


x = Person("Aminul", "John")
x.printname()