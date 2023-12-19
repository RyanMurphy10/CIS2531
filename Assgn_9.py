#######################################################################################
#Assgn_9 Ryan Murphy 
#imports pickle and os
#creates load data function to load the data that the user will enter 
#saves data so the data will be saved to the file
#displays menu to the user with options 
#prompts the user to add, delete, change, look up, and exit
#user then enters a name with an ID to data
# The user can then add more names, delete previous names, and change names
#when user is done entering names they can exit the program
#######################################################################################
import pickle #import the pickle
import os

def load_data(file_name): #Function to load data from file
    if os.path.exists(file_name): #if file exists
        with open(file_name, 'rb') as file: #open file
            data = pickle.load(file)
            return data #returns data
    return {}

def save_data(file_name, data): #Function to save data to file
    with open(file_name, 'wb') as file: #open file
        pickle.dump(data, file) #save data

def display_menu(): #Function to display menu
    print("1. Look up ID") #searchs for the ID
    print("2. Add new name and ID") #adds a new ID
    print("3. Change existing name and ID") #changes the ID
    print("4. Delete existing name and ID") #deletes ID
    print("5. Exit") #stops code
  
    choice = input("\nEnter your choice: ") #prompts user to choose from menu
    return choice #returns choice

# Main program
file_name = "data.pkl"  # File to store data

data = load_data(file_name)

while True: #makes code cycle correctly
    user_choice = display_menu() #displays the menu

    if user_choice == '1':  #Look up ID
        name = input("Enter name to look up: ") #asks user to look up a name
        if name in data: #checks if the name is in the data
            print(f"The ID for {name} is {data[name]}") #formatted print so output prints correctly
        else:
            print(f"No record found for {name}") #prints if name is not in data

    elif user_choice == '2':  # Add new name and ID
        name = input("Enter new name: ") #asks user to enter a new name
        id_number = input("Enter ID for the new name: ") #asks user to enter a new ID
        data[name] = id_number #adds new name and ID to data
        print(f"{name} with ID {id_number} added.") #prints if name and ID is added

    elif user_choice == '3':  # Change existing name and ID
        name = input("Enter name to update: ") #asks user to enter a name to update
        if name in data: #checks if name is in data
            new_id = input("Enter new ID: ")
            data[name] = new_id
            print(f"{name}'s ID updated to {new_id}.")
        else:
            print(f"No record found for {name}")

    elif user_choice == '4':  # Delete existing name and ID
        name = input("Enter name to delete: ") #prompts user to delete name
        if name in data: #checks if name is in data
            del data[name]
            print(f"{name}'s record deleted.")
        else:
            print(f"No record found for {name}") #prints name is not found

    elif user_choice == '5':  # Exit and save data
        save_data(file_name, data) #saves data
        print("Data saved. Exiting the program.")
        break #exits code

    else:
        print("Invalid choice. Please enter a valid option.") #repeats if name is invalid