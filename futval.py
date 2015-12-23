# futval.py
# A program to compute the future value of an investment
# 10 years in the future.

import graphics


def main():
    print("This program will calculate the future value of an investment")

    principal = float(input("Enter the initial investment: "))
    annual = float(input("Enter annual contribution: "))
    apr = float(input("Enter the annual rate: "))
    period = int(input("Enter number of periods per year: "))
    years = int(input("Enter the number of years: "))

    if (apr > 1.0):
        apr = apr / 100.0

    apr = apr / period

    balance = principal
    for i in range(years):
        for j in range(period):
            balance = balance * (1 + apr)
            # print(str(i)+" "+str(j)+" "+str(balance))
        balance = balance + annual

    print ("The value in " + str(years) + " years will be $" +
           "{:0.2f}".format(balance))

main()
