class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_information(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Super Power:", self.super_power)
        print("Weapon:", self.weapon)
        print()

    def is_leader(self):
        return self.name == "Captain America"


avengers = [
    Avenger("Captain America", 100, "Male", "Super Strength", "Shield"),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 45, "Male", "Unlimited Strength", "None"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjolnir"),
    Avenger("Hawkeye", 40, "Male", "Fighting Skills", "Bow and Arrows"),
]

for hero in avengers:
    hero.get_information()
    if hero.is_leader():
        print(hero.name, "is the leader.")
    else:
        print(hero.name, "is not the leader.")
    print("-" * 30)
