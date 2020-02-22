class CocaCola(): 
    def type(self): 
        print("This is a soda. ") 
  
    def slogan(self): 
        print("Taste the Feeling") 
  
    def popularity(self): 
        print("This is a popular soda world-wide.") 
  
class Skittles(): 
    def type(self): 
        print("This is a candy.") 
  
    def slogan(self): 
        print("Taste the rainbow") 
  
    def popularity(self): 
        print("This is a popular candy in the US.") 
  
obj_ind = CocaCola() 
obj_usa = Skittles() 
for country in (obj_CC, obj_SK): 
    country.type() 
    country.slogan() 
    country.popularity() 
