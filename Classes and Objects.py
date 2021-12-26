#A Class is a piece of code that defines what an object is
#An object is a thing that can have attached variable and methods,variable with other variables inside, can also have methods


class Person:
  def __init__(self,gender,height,weight):
    self.gender = gender
    self.aliveness = True 
    self.height = height
    self.weight = weight
  
  def getGender(self):
    return self.gender
   
  def setGender(self,gender):
    self.gender = gender

  def setHeight(self):
    return self.height

  def setHeight(self):
    return self.Height

  def getWeight(self):
    return self.weight

  def setWeight(self):
    return self.weight   

p1 = Person('nonb',150,150)
#p1 = Person.__init__('nonb',150,150)

print(p1.gender)