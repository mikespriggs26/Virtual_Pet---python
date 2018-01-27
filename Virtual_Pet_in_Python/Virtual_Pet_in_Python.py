

class VirtualPet():
    def __init__(self, hunger, water, insulin):
        self.hunger = hunger
        self.water = water
        self.insulin = insulin


    def dogInfo(self):
        print("Hunger: " + str(self.hunger))
        print("Thirst: " + str(self.water))
        print("Insulin: " + str(self.insulin) + "\n")

    def feedDog(self):
        self.hunger += 10
        self.water -= 5
        self.insulin -= 4

    def waterDog(self):
        self.water += 10
        self.hunger -= 5
        self.insulin -= 4

    def giveInsulin(self):
        self.insulin += 38
        self.hunger -= 5
        self.water -= 5



def main():
    print("Welcome to the virtual pet.  You are responsible for caring for a diabetic dog.")
    ranger = VirtualPet(40, 30, 30)
    print("Ranger's stats are: ")
    ranger.dogInfo()
   
    def userMenu():
        userChoice = input("Enter 1 to feed, 2 to give water, 3 to give insulin and any other key to quit : ")
   
        if userChoice == "1":
            ranger.feedDog()
            ranger.dogInfo()
            return userMenu()
        elif userChoice == "2":
            ranger.waterDog()
            ranger.dogInfo()
            return userMenu()
        elif userChoice == "3":
            ranger.giveInsulin()
            ranger.dogInfo()
            return userMenu()
        else:
            print("Thank you for playing!")
            raise SystemExit
    userMenu()
if __name__ == "__main__": main()
