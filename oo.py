#global scope

name = "jenkins the doofus"

#-----------------------------------

class Dog(object):
    
    def __init__(self, name):
        self.name = name

    def bark(self):
        print "woof my name is " + self.name

dog = Dog("sparky")
dog.bark()

print "name is " + name

#other programmer
name = "james and the giant peach"

print "name is " + name