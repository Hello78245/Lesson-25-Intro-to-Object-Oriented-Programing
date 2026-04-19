class Parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
Mike=Parrot("Mike",10)
Molly=Parrot("Molly",15)
print("Mike is a {}".format(Mike.species))
print("Molly is also a {}".format(Molly.species))
print("{} is {} years old".format(Mike.name,Mike.age))
print("{} is {} years old".format(Molly.name,Molly.age))