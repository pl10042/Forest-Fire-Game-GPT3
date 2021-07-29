import random
import time
import os
from dotenv import load_dotenv
import openai

load_dotenv()
completion = openai.Completion()

def gpt3(stext):
    openai.api_key = os.environ.get('OPENAI_KEY')
    response = openai.Completion.create(
        engine="curie-instruct-beta",
        prompt=stext,
        temperature=.25,
        max_tokens=15,
        top_p=1,
        frequency_penalty=.33,
        presence_penalty=.2,
    )
    content = response.choices[0].text.split('.')
    # print(content
    return response.choices[0].text


questionDict = {

    "questionOne": 'How many apples are in the tree if there were originally 10, and 5 are on the ground? Answer with '
                   'one '
                   'number. No letters or words. ',
    "questionThree": 'What is 5+10? Answer with one number. No letters or words.',
    "questionFour": 'What year was the declaration of independence signed? No letters or words.'
}

answerDict = {

    "first": '5',
    "ans4": '15',
    "aiAnswer": [],
    "yearAnsw": '1776',
}

answerList = (list(answerDict.values()))

query = random.choice(list(questionDict.values()))
query2 = "Return a random number that is greater than 51 and less than 100. Do not choose 51 or 100. Return one number. No letters or words."
query3 = "Please type in the letter y or n. Type y to continue putting out the fire, or n if you want to let it burn. Return as a single letter. "
query5 = "Return a random number that is greater than 51 and less than 100. Do not choose 51 or 100. Return one number. No letters or words."
query6 = "Return a random number that is greater than 51 and less than 500. Do not choose 51 or 500. Return one number. No letters or words."

response1 = str(gpt3(query))
response = ''.join(i for i in response1 if i.isdigit())
answerDict["aiAnswer"].append(response)
response21 = (gpt3(query2))
response2 = ''.join(i for i in response21 if i.isdigit())
response3 = (gpt3(query3))
response51 = (gpt3(query5))
response52 = ''.join(i for i in response51 if i.isdigit())
response5 = int(response52)
response61 = gpt3(query6)
response6 = ''.join(i for i in response61 if i.isdigit())


# responseList = list(response.split(" "))

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
                        userResponse = response3

                        if 'y' in userResponse:
                            print('y')
                            print("\nPlease add more water by updating the water capacity: ")
                            # powerUpdate = int(input())
                            powerUpdate = int(response2)
                            print(powerUpdate)
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
                                # powerUpdate2 = int(input())
                                powerUpdate2 = int(response6)
                                print(powerUpdate2)
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

                        if 'n' in userResponse:
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

dryness = random.randint(1, 20)
dryness = dryness
if dryness <= 20:
    print(f"The current humidity is {dryness}%.")
else:
    print(f"{dryness}% humidity is not dry enough, conditions not met..\n")
    exit()

windSpeed = random.randint(10, 35)
windSpeed = windSpeed
if windSpeed >= 10:
    print(f"The current wind speed is {windSpeed}mph.")
else:
    print(f"Only {windSpeed}mph winds, conditions not met..\n")
    exit()

numberOfTrees = random.randint(1001, 5000)
numberOfTrees = numberOfTrees
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
    print("Providing random question...")
    print(query)
    # print("\nAI Answer: ")
    print(response)
    # print()
    # if answer not in response:

    for v in answerDict.values():
        if response in answerDict.values():
            print("\nA fire has started! Use the hose to put it out!")
            fireStarted = True
            if fireStarted:
                print(
                    "\nHow much water do you want to give the fire hose? \n(1 - 100: Normal) (100 - 200: Medium) (200 - "
                    "300: High) (300 - 500: Extreme)")
                # hosePower = int(input())
                hosePower = response5
                print(hosePower)
                hose = FireHose(hosePower)
                hose.putOut(fireStarted)

        # elif answer in response or answer == 'five':
        #     print("\nCongratulations! The fire was successfully prevented...")
        #     exit()
        else:
            print("\nThe answer was incorrect and therefore the game ends...")
            exit()
