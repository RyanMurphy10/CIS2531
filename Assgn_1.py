#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 02:11:17 2023

@author: ryanmurphy
"""

print("Welcome to Imperial to Metric Units Conversion System Calculator")


print("\nMass Conversion Calculator")

print("\nPounds to Kilograms Conversion")
Pounds = (input("Input Number of Pounds: "))
while Pounds.isnumeric() == False:
  print("Invalid Data")
  Pounds = (input("Input Number of Pounds: "))
Kilogram = float(Pounds) * 0.453592
print(f'{int(Pounds)}lbs = {round(Kilogram,2)}kg')  
  
print("\nPounds to Grams Conversion")
Pounds = input("Input Number of Pounds: ")
while Pounds.isnumeric() == False:
  print("Invalid Data")
  Pounds = (input("Input Number of Pounds: "))
Gram = float(Pounds) * 453.592
print(f'{int(Pounds)}lbs = {round(Gram,2)}g')
  
  
print("\nDistance Conversion Calculator")

print("\nMiles to Kilometers Conversion")
Miles = input("Input Number of Miles: ")
while Miles.isnumeric() == False:
  print("Invalid Data")
  Miles = input("Input Number of Miles: ")
Kilometer = float(Miles) * 1.60934
print(f'{int(Miles)}mi = {round(Kilometer,2)}km')
  
print("\nFeet to Meters Conversion")
Feet = input("Input Number of Feet: ")
while Feet.isnumeric() == False:
  print("Invalid Data")
  Feet = input("Input Number of Feet: ")
Meter = float(Feet) * 0.3048
print(f'{int(Feet)}ft = {round(Meter,2)}m')
  
  
print("\nVolume Conversion Calculator")
  
print("\nGallons to Liters Conversion")
Gallons = input("Input Number of Gallons: ")
while Gallons.isnumeric() == False:
  print("Invalid Data")
  Gallons = input("Input Number of Gallons: ")
Liter = float(Gallons) * 3.78541
print(f'{int(Gallons)}G = {round(Liter,2)}L')
  
print("\nPints to Milliliter Conversion")
Pints = input("Input Number of Pints: ")
while Pints.isnumeric() == False:
  print("Invalid Data")
  Pints = input("Input Number of Pints: ")
Milliliter = float(Pints) * 473.176
print(f'{int(Pints)}pt = {round(Milliliter,2)}ml')

print("\nThanks for Converting")