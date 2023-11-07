############################################################################
#Assgn_2 Ryan Murphy
#Prompts user to enter ID
#Prompts Tester to enter either green amber or red for test
#If Amber or green test ends with print statement
#if red is inputted the user is prompoted to enter meter 3 value
#Checks if meter 3 value is less than, equal to, or greater than 50
#if less than code ends
#if greater than or equal to user is prompted to input inlet 2B
#Determining on if the inlet 2B is low, normal, or high code will end with print statement
############################################################################
print("Hello, Welcome to Troubleshooting A Diesel Engine")
TesterID = input("Please Enter A Tester ID: ")

CheckStatusLights = input ("\nInput Status Light Color: ")
CheckStatusLights = CheckStatusLights.lower() #makes input is accepted if the word matches regardless of capitalization for charecters

if CheckStatusLights == 'green':
   print("Restart Procedure") #test ends
  
elif CheckStatusLights == 'amber': #test ends
   print("Check Fuel Line Service Routine")
  
elif CheckStatusLights == 'red':
   print("Shut-off All Input Lines Check Meter #3")
   Meter3Value = input("Input Meter #3 Value: ")
   Meter3Value = int(Meter3Value) #converts to an int so it can run through the future if statements
  
   if Meter3Value < 50: #checks if less than 50
       print("Check Main Line For Test Pressure")
       testPressure = input("Input Test Pressure: ")
       testPressure = testPressure.lower()
       if testPressure == "normal":
           print("Refer To Motor Service Manual")
       elif testPressure == "high" or testPressure == "low":
           print("Refer To Main Line Manual")
  
   elif Meter3Value >= 50: #checks if greater than or equal to 50
       print("Measure Flow Velocity At Inlet 2-B")
       Velocity2BValue = input("Input Flow Velocity For Inlet 2-B: ")
       Velocity2BValue = Velocity2BValue.lower()
       if Velocity2BValue == "normal":
           print("Refer To Inlet Service Manual")
       elif Velocity2BValue == "high" or Velocity2BValue == "low":
           print("Refer Unit For Factory Service")