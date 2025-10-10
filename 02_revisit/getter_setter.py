
class Employee:

    def __init__(self, age):
      self._age = age
    
    @property
    def age(self):
       return self._age

    
    @age.setter
    def age(self, age):
        if age <= 0 or age > 110 :
          raise ValueError('incorrect value of age')
        self._age = age



e = Employee(9)
e.age = 2
print(e.age)