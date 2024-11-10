

# class cat :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def intro(self):
#         print("hello i am a cat and my name is ",self.name ,"and i am ",self.age,"years old")
#     def sounds(self):
#         print("i make meow sound")

# class dog :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def intro(self):
#         print("hello i am a dog and my name is ",self.name ,"and i am ",self.age,"years old")
#     def sounds(self):
#         print("i make bark sound")

# cat1=cat("pussy",4)
# dog1=dog("bunny",5)


# for animal in (cat1,dog1):
#     animal.intro()
#     animal.sounds()


#activity 2

class drone:
    def __init__(self):
        self.__maxprice = 12000

    def sell(self):
        print("The selling price of the drone is:",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice = price 

d = drone()


d.__maxprice = 15000
d.setmaxprice(15000)
d.sell()

        