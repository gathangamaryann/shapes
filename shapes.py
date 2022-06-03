
class Circle:
    # circle="radius"
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        a=3.142*self.radius**2
        return f"The area is {a}"

    def circumfrence(self):
        c=(self.radius+self.radius)*3.142
        return f"The circumfrence is {c}"

class Square:
    def __init__(self,side):
          self.side=side
    def area(self):
        a=self.side+self.side
        return f"The area of the square is{a}"

    def parametre(self):
        p=4*self.side    
        return f"The parameter of the square is{p}"

class Rectangle:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        a=self.w*self.l  
        return f"The area of the rectangle is{a}"

    def parametre(self):
        p=(self.l+self.w)*2 
        return f"The parameter of the rectangle is{p}"   

class Sphere:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
          a=4*3.142*self.radius**2
          return f"The area of the sphere is{a}"

    def volume(self):
        v=1.333(3.142*self.radius**3)   
        return f"The volume of the sphere is{v}"
   
                
  
            

            

        
        

     