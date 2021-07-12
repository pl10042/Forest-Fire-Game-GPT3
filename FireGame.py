import random
import time

"""
Guess a random number between 1 and 10, if you get it wrong, the forest catches on fire. Your goal is to extinguish
it using the provided fire hose.
"""

"""A future implementation would be to start the problem by initializing a random problem for the user to solve. They 
enter an answer, if the answer is correct, more water is added to the fire. If the water capacity every decreases 
below 10 percent of the fire potency, the user loses. The goal is to continuously add water until the fire is 
completely put out. 
"""

qaDict = {

    "questionOne": "How many apples are in the tree if there were originally 10, and 5 are on the ground?"
}

# Firehose object that uses check statements to put out the fire
class FireHose:

    # Initialize water capacity
    def __init__(self, power):
        self.power = power

    # Function used to put out the fire
    def putOut(self, fireCheck):

        firePotency = 100
        if self.power > 50 and fireCheck:
            print()
            while firePotency >= 0:
                newPower = self.power
                if 100 <= self.power <= 200:
                    while newPower >= firePotency:
                        print("\r", "Fire potency:", firePotency, "%", "   ", "Water Capacity:", self.power, "%",
                              end="")
                        firePotency -= 1
                        self.power -= 1
                        time.sleep(.15)
                        if firePotency <= 0:
                            print()
                            print("\nThe fire was put out in 8 hours!")
                            exit()
                if 201 <= self.power <= 300:
                    while newPower >= firePotency:
                        print("\r", "Fire potency:", firePotency, "%", "   ", "Water Capacity:", self.power, "%",
                              end="")
                        firePotency -= 1
                        self.power -= 1
                        time.sleep(.10)
                        if firePotency <= 0:
                            print()
                            print("\nThe fire was put out in 4 hours!")
                            exit()
                if 301 <= self.power <= 500:
                    while newPower >= firePotency:
                        print("\r", "Fire potency:", firePotency, "%", "   ", "Water Capacity:", self.power, "%",
                              end="")
                        firePotency -= 1
                        self.power -= 1
                        time.sleep(.05)
                        if firePotency <= 0:
                            print()
                            print("\nThe fire was put out in 1 hour!")
                            exit()
                if self.power < 100:
                    print("\r", "Fire potency:", firePotency, "%", "   ", "Water Capacity:", self.power, "%", end="")
                    firePotency -= 1
                    self.power -= 1
                    time.sleep(.25)
                    if firePotency == 50:
                        print()
                        print("\n(12 hours later) The hose is running low on water!")
                        print("Would you like to update the Water Capacity?(y or n)")
                        userResponse = str(input())

                        if userResponse == 'y':
                            print("\nPlease add more water by updating the water capacity: ")
                            powerUpdate = int(input())
                            self.power = powerUpdate
                            print()
                            if self.power > firePotency:
                                print("\r", "Fire potency:", firePotency, "%", "   ", "Water Capacity:", self.power,
                                      "%", end="")
                                firePotency -= 1
                                self.power -= 1
                                time.sleep(.25)
                                if firePotency < 1:
                                    print()
                                    print("\nThe fire was put out in 1 hour!")
                                    exit()
                            if powerUpdate < firePotency:
                                print()
                                print(f"Please add an amount of water that is higher than {firePotency}%!")
                                powerUpdate2 = int(input())
                                self.power = powerUpdate2
                                print()
                                if self.power >= firePotency:
                                    print()
                                    print("\r", "Fire potency:", firePotency, "%", "   ", "Water Capacity:", self.power,
                                          "%", end="")
                                    firePotency -= 1
                                    self.power -= 1
                                    time.sleep(.25)
                                    if firePotency < 1:
                                        print()
                                        print("\nFire has been extinguished!")
                                        break
                                if powerUpdate2 <= firePotency:
                                    while firePotency <= 100:
                                        print("\r", "Fire potency:", firePotency, "%", "   ", "Water Capacity:",
                                              self.power, "%", end="")
                                        firePotency += 1
                                        self.power -= 1
                                        time.sleep(.05)
                                        if firePotency > 100 or self.power == 0:
                                            print("\nYour hose ran out of water and the entire forest is burned "
                                                  "down...")
                                            exit()
                                            break

                        if userResponse == 'n':
                            print()
                            while firePotency <= 100:
                                print("\r", "Fire potency:", firePotency, "%", "   ", "Water Capacity:", self.power,
                                      "%", end="")
                                firePotency += 1
                                self.power -= 1
                                time.sleep(.25)
                                if firePotency > 100 or self.power == -1:
                                    print()
                                    print("\nThe hose ran out of water and the entire forest is burned down...")
                                    exit()
                                    break
            if firePotency < 1:
                print()
                print("\nThe fire has been extinguished!")
                exit()

        if self.power < 50 and fireCheck:
            print()
            print("Not enough water to put out the fire!")
            print("The fire overwhelms the hose and the entire forest burned down...")


fireStarted = False
print("Now starting fire simulation...\n")

dryness = random.randint(1, 35)
if dryness <= 20:
    print(f"The current humidity is {dryness}%.")
else:
    print(f"{dryness}% humidity is not dry enough, conditions not met..\n")
    exit()

windSpeed = random.randint(8, 35)
if windSpeed >= 10:
    print(f"The current wind speed is {windSpeed}mph.")
else:
    print(f"Only {windSpeed}mph winds, conditions not met..\n")
    exit()

numberOfTrees = random.randint(100, 5000)
if numberOfTrees > 1000:
    print(f"There are a total of {numberOfTrees} trees in the vicinity.\n")
else:
    print(f"Only {numberOfTrees} trees around, conditions not met..\n")
    exit()

if (dryness <= 20) and windSpeed >= 10 and numberOfTrees > 1000:
    # print("Do you wish to start a bonfire? (y or n)")
    # answer = str(input(""))
    # randNumb = random.randint(1, 10)
    """
    Now testing question/answering implementation.
    """
    print("Providing first question...")
    print()
    print(qaDict["questionOne"])
    qaDict["questionOne"] = 5
    answer = int(input())
    if answer != 5:
        print("\nA fire has started! Use the hose to put it out!")
        fireStarted = True
        if fireStarted:
            print("\nHow much water do you want to give the fire hose? \n(1 - 100: Normal) (100 - 200: Medium) (200 - "
                  "300: High) (300 - 500: Extreme)")
            hosePower = int(input())
            hose = FireHose(hosePower)
            hose.putOut(fireStarted)

    elif answer == 5:
        print("\nCongratulations! The fire was successfully prevented...")
        exit()
