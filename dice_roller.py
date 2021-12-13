"""
This is a dice roller simulator to practice GUI
Wrote by @PedroPassos 12/13/2021 3:25 pm
"""
import random
import PySimpleGUI as sg

class DiceRoller:

    def __init__(self):
        #define range of the die
        self.high = 6
        self.low = 1

        #possible values
        self.values = (1, 2, 3, 4, 5, "None")

        #GUI layout 0
        self.initial_layout = [
            [sg.Text("How many Dice would you like to roll?")],
            [sg.Combo(self.values)],
            [sg.Button("Roll!"), sg.Button("Quit")]
        ]

        #GUI layout 1
        self.main_layout = [
            [sg.Text("Would you like to roll again")],
            [sg.Button("Yes"), sg.Button("No")]
        ]

        self.end_layout = [
            [sg.Text("Thanks for participating!")]
        ]

        self.error_layout = [
            [sg.Text("There was an error")]
        ]

    def choose_dice_count(self):
        
        #create window
        self.window = sg.Window("Dice Roller", layout = self.initial_layout)

        #read values
        self.events, self.values = self.window.Read()

        try: 
            if self.events == "Roll!":
                values_list = list(self.values.values())
                number = values_list[0]
                return number

            elif self.events == "Quit":
                self.window = sg.Window("Thank you", layout = self.end_layout)

        except:
            self.window = sg.Window("Error", self.error_layout)

    def get_rolling(self):

        number = self.choose_dice_count()            
        
        self.window = sg.Window("You just rolled " + str(number) + "dice! The values are: " + str(self.roll(number)), layout = self.main_layout )

        self.events, self.values = self.window.Read()
        #interface probabilities
        try:
            if self.events == "Yes":
                self.get_rolling()

            elif self.events == "No":
                self.window = sg.Window("Thank you", layout = self.end_layout)

        except:
            print("There was an error processing your answer")

    def roll(self, number):
        number_list = list()
        print(type(number))
        for i in range(number):
            number_list[i+1] = str(random.randint(self.low, self.high))
        return number_list

r = DiceRoller()
r.get_rolling()
