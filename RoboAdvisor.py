import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class RoboAdvisor:  # class name
    def __init__(self):
        self._user_name = ''  # class variable
        self._annual_income = 0
        self._annual_expenses = 0
        self._risk_score = 3
        self._projected_return_list = []
        self._net_income = 0
        self.no_of_child = 0
        self._investible_amount = 0
        self._annual_return_rate = 0.0
        self._product_list = {"Product A": 500, "Product B": 100, "Product C": 50, "Product D": 10}

    def greeting(self):  # method
        print("hi {}, I am robo advisor".format(self._user_name))

    def ask_name(self):
        self._user_name = input("What is your name?")

    def get_net_income(self):
        self._annual_income = float(input("What is your estimated annual income?"))
        self._annual_expenses = float(input("What is your estimated annual expenses?"))
        self._net_income = self._annual_income - self._annual_expenses
        if self._net_income > 1000000:
            self._risk_score = 10
        elif self._net_income > 100000:
            self._risk_score = 8
        elif self._net_income > 10000:
            self._risk_score = 5

    def get_children(self):
        self.no_of_child = int(input("How many children do you have?"))
        if self.no_of_child > 5:
            self._risk_score *= 0.5
        elif self.no_of_child > 3:
            self._risk_score *= 0.8
        elif self.no_of_child > 0:
            self._risk_score *= 0.9

    def get_investible_amt(self):
        self._investible_amount = int(input("How much investible amount will you set aside?"))

    def display_recommended_portfolio(self):
        if self._risk_score > 9:
            self._annual_return_rate = float(self._product_list["Product A"] / 100)
            print("You may invest Product A, expected return {} per annum".format(self._product_list["Product A"]))
        elif self._risk_score > 6:
            self._annual_return_rate = float(self._product_list["Product B"] / 100)
            print("You may invest Product B, expected return {} per annum".format(self._product_list["Product B"]))
        elif self._risk_score > 3:
            self._annual_return_rate = float(self._product_list["Product C"] / 100)
            print("You may invest Product C, expected return {} per annum".format(self._product_list["Product C"]))
        else:
            self._annual_return_rate = float(self._product_list["Product D"] / 100)
            print("You may invest Product D, expected return {} per annum".format(self._product_list["Product D"]))

    def calculate_projected_return(self):
        investment = self._investible_amount
        for year in range(5):
            investment = investment * (1 + self._annual_return_rate)
            self._projected_return_list.append(investment)

    def display_chart(self):
        plt.plot(range(1, 6), self._projected_return_list, label='linear')

        # fixed the scale become 1,2,3,4,5
        plt.xticks([1, 2, 3, 4, 5])
        # Add a legend
        plt.legend()
        # Show the plot
        plt.show()

    def export(self):
        df = pd.DataFrame(self._projected_return_list)
        df.to_csv('projected_return.csv')


my_robo = RoboAdvisor()
my_robo.greeting()
my_robo.ask_name()
my_robo.get_net_income()
my_robo.get_children()
my_robo.display_recommended_portfolio()
my_robo.get_investible_amt()
my_robo.calculate_projected_return()
my_robo.display_chart()