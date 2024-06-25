class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('Hello', self.name)

    # Equaliy methods
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __eq__(self, person):
        return self.age == person.age

    def __ne__(self, person):
        return self.age != person.age

    def __lt__(self, person):
        return self.age < person.age

    def __gt__(self, person):
        return self.age > person.age

    def __le__(self, person):
        return self.age <= person.age

    def __ge__(self, person):
        return self.age >= person.age 

class Friend(Person): # inheriting Person class -> will have access to variables and methods

  def say_hi(self, extra):
    super().say_hello()
    print('Hello to', extra)

john = Person('John', 23)
john.say_hello()

meg = Friend('Margaret', 25)
meg.say_hi("Josh") # calling overridden say_hi method of Friend class


joe = Person('Joe', 23)
jill = Person('Jill', 25)

print('== result:', joe == jill)
print('!= result:', joe != jill)
print('< result:', joe < jill)
print('> result:', joe > jill)
print('<= result:', joe <= jill)
print('>= result:', joe >= jill)