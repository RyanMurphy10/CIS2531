############################################################################
#Assgn_5 Ryan Murphy
#Inventory txt file is imputted
#Inventroy txt file is opened
#Information in Inventory txt file is then sorted and revised
#Inventory request file is then printed with the valid information from Inventory file and is printed out as the inventoryRequested txt file
############################################################################
f1 = open('inventory.txt') #opens inventory.txt
f2 = open('inventoryRequest.txt', 'w') #opens inventoryRequested.txt

print('{} {:>17} {:>15}'.format('Part','Balance','Amount Needed')) #prints the format for the headings

for line in f1: #goes through lines in inventory.txt
    items = line.split(',') #gets rid of , in inventory.txt

    current_balance = int(items[1]) - int(items[2]) #calculation for amount needed

    required = int(items[3]) - current_balance # second part for the equation of amount needed

    f2.write(items[0] + ',' + str(current_balance) + ',' + str(required) + '\n') #formats so the items in inventory.txt are inputted and calculated correctly 

    print(f'{format(items[0])}          {current_balance}        {required}') #prints format for inventoryRequested.txt

f1.close() #closes inventory.txt
f2.close() #closes inventoryRequested.txt
