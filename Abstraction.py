from abc import ABC, abstractmethod 
  
class aTOb(ABC): 
  
    # abstract method 
    def capacity(self): 
        pass
  
class train(transportation): 
  
    # overriding abstract method 
    def capacity(self): 
        print("I have a capacity of 270 passengers") 
  
class car(transportation): 
  
    # overriding abstract method 
    def capacity(self): 
        print("I have a capacity of 5 passengers") 
  
class airplane(transportation): 
  
    # overriding abstract method 
    def capacity(self): 
        print("I have a capacity of 91 passengers") 
  
class bus(transportation): 
  
    # overriding abstract method 
    def capacity(self): 
        print("I have a capacity of 50 passengers") 
  

R = train() 
R.capacity() 
  
K = car() 
K.capacity() 
  
R = airplane() 
R.capacity() 
  
K = bus() 
K.capacity()
