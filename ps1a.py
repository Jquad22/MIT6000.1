# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:26:48 2020

@author: john
"""

#variables
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:"))
current_savings = 0.0
portion_down_payment = total_cost * 0.25

r = 0.04/12
months = 0
#calculate savings on monthly basis
while current_savings <= portion_down_payment:
    monthly_salary = annual_salary / 12
    current_savings = (r * current_savings) + current_savings + (monthly_salary * portion_saved)
    months = months + 1
    #calculate semi-annual raise750
    if months % 6 == 0:
         annual_salary = (annual_salary * semi_annual_raise) + annual_salary
          
         
print("Number of months:",months)                    