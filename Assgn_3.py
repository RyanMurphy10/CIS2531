############################################################################
#Assgn_3 Ryan Murphy
#Prompts user to enter requested generators
#Prompts Tester to enter either green amber or red for test
#takes users request and then makes a range that will average data
#creates an empty list to input the data
#user inputs the 3 voltage readings in the generator
#an average voltage reading for the generator is produced
#then program repeats steps for the other number of inputted generators
#finally the average number for each generator is then added and divided by the number of generators to find the main average
############################################################################
print("Welcome! This program will calculate the output voltage average of your generators.") #opening print statement
generatorcount = int(input("\nHow many generators would you like to average?: ")) #input statement to get the number of generators tested

total = 0 #constant set to zero 

for count in range(generatorcount): #checks for the count in generatorcount
    print("Please enter three test voltages:\n") #print statement
    voltages = [] #empty list
    voltagesum = 0 #sets sum to zero
    for x in range(3): #makes a range of 3 for the voltage readings
        voltage = float(input(f"Voltage reading {x+1}: "))
        voltages.append(voltage) #appends voltage to voltages
        voltagesum += voltage
    sampleaverage = voltagesum / 3 #divides to find the average since the range is 3
    total += sampleaverage
    print(f"\nThe average output voltage for generator {count+1} is: {round(sampleaverage,2)}")

Average = total / generatorcount #checks the averages of the voltages and then finds the main average
print(f"\nThe total average of all {count+1} generators is: {round(Average,2)}") 