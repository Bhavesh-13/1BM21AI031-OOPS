class Songs:
    def __init__(self,lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric)
lyrics = ['a',"b",'c','d']
obj = Songs(lyrics)
obj.sing_me_a_song()


class birthdayboy:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def birthday(self):
        self.age+=1
        return self.age
boy1=birthdayboy("ABC",35)
age=boy1.birthday()
print(f"ABC's age after his birthday is {age}")

# create paramteterised constructor that takes two arguments  for a reactangle class,length and breadth and initalises the length breaadth attributes of the object with the values passed as arguments
class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        self.area=self.length*self.breadth
        return self.area

r1 = rectangle(12,34)
area=r1.area()
print(f"area of the reactngle 1 is {area}")


import datetime
class Dog:
    name = 'tom'
    breed = 'pug'
    dob = datetime.datetime(2021,12,31,12,0,0,0)
    def bark(self):
        print("wooooofff!!!?")
        print(self.dob)
    def get_name(self):
        print("dog's name is:",self.name) 
    def set_name(self):
        new_name = input("Enter the new name of the dog: ")
        self.name = new_name
obj = Dog()
obj.set_name()
obj.get_name()
obj.bark()


#create a class car with 3 args brand,year,model .  Initialize a class instance with values supply. The display car details method is invoked using the class object and it is used to show the car's details .