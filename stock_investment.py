#Denis Glazer, CS 110A
#Homework 5 -- Stock Simulator 
#Objective: To use a function and random number generation to simulate the performance of money invested in a stock

import random
#This function will return average value
def average (values): return sum (values) / len (values)
#Lines 9 to 37 using user input to define boundaries
initialInvestment = input ("Please enter initial stock investment: ")

if initialInvestment == "":
  initialInvestment = 1000

initialInvestment = float (initialInvestment)

lowestRateOfReturn = input ("Please enter the lowest rate of return you anticipate in a year (as a percentage, for example enter -5 for 5% annual loss): ")

if lowestRateOfReturn == "":
  lowestRateOfReturn = -5

lowestRateOfReturn = float (lowestRateOfReturn)

highestRateOfReturn = input ("Please enter the highest rate of return you anticipate in a year (as a percentage, for example enter 10 for 10% annual increase): ")

if highestRateOfReturn == "":
  highestRateOfReturn = 10

highestRateOfReturn = float (highestRateOfReturn)

yearsToHoldStock = input ("How many years will you keep the investment in these stocks? ")

if yearsToHoldStock == "":
  yearsToHoldStock = 10

yearsToHoldStock = int (yearsToHoldStock)
simulations = 10
endingBalances = []

for i in range (simulations):
  endingBalance = initialInvestment
  #random number generation
  for year in range (yearsToHoldStock):
     randomReturnRate = random.randrange (lowestRateOfReturn, highestRateOfReturn)/100
     endingBalance *= 1 + randomReturnRate
  
  endingBalances.append (endingBalance)


print ("\nHere are", simulations, "illustrations of how much money you might have after", yearsToHoldStock, "years have passed:\n")

for i in range (simulations):
  print ("Illustration #", end="");
  print (1+i, end="");
  print (" shows you might end up with $", end="");
  print (format (endingBalances [i], '.2f'))

#final calculation
averagePerformance = average (endingBalances)
averageGain = ((averagePerformance - initialInvestment)/initialInvestment)*100

print ("\nThe average of all", simulations, "illustrations is $", end="")
print (format (averagePerformance, '.2f'), end="")
print (", a", format (averageGain, '.2f'), end="")
print ("% increase over", yearsToHoldStock, "years.\n")

'''
This function calculates perfromance of money invested in a stock. lowest and highest rate can't both be equal to zero in one run. 
'''