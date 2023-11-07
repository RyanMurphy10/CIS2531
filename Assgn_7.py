####################################################################################################################
#Assgn_7 Ryan Murphy 
#Using the library Matplotlib and the provided data files create the following graphs
#Create a pie chart that shows the percentage of employees in each department within a company
#The provided file: employee_count_by_department.txt contains the data required in order to generate this pie chart
#Create a line graph that shows a company’s profit over the past ten years
#The provided file: last_ten_year_net_profit.txt contains the data required in order to generate this line graph
#Create a bar graph that shows a company’s profit over the past ten years
#The provided file: last_ten_year_net_profit.txt contains the data required in order to generate this bar graph
####################################################################################################################
import matplotlib.pyplot as plt #imports matplotlib

def barGraph(X,Y): #creates bar graph with X and Y variables
  bargraph = plt.figure(figsize = (6,4))
  plt.bar(X,Y) #plots X and Y
  plt.xlabel("Year") #sets X-axis to "Year"
  plt.ylabel("$USD in millions") #sets Y-axis label to "$USD in millions"
  plt.title("Profits by year") #sets title to "Profits by year"
  plt.show() #plots barGraph labels without imported data

def pieChart(X,Y): #creates pie chart with X and Y variables
  piechart = plt.figure(figsize = (6,4)) 
  plt.pie(Y, labels = X,autopct = '%1.2f%%') 
  plt.show() #plots pieChart labels without imported data

def lineGraph(X,Y): #creates lineGraph with X and Y variables
  linegraph = plt.figure(figsize = (6,4))
  plt.plot(X,Y) #plots X and Y
  plt.xlabel("Year") #sets X-axis to "Year"
  plt.title("Last ten year profit line Graph") #sets title to "Last ten year profit line Graph"
  plt.show() #plots lineGraph labels without imported data

def main(): #main function
  X = [] #x list
  Y = [] #y list
  with open("last_ten_year_net_profit.txt","r") as rdf: #opens "last_ten_year_net_profit.txt"
      lines = rdf.readlines() #reads lines
      for line in lines[1:]: #skips the first line
          tup = line.split(";") #reads over ";"
          X.append(int(tup[0])) #appends the numbers 
          value = 0 #sets value to 0
          for i in tup[1]:
            try: #trys for loop
              value = value * 10 + int(i) #equation for value
            except: #tests conditional case
              continue #continues
          Y.append(value) #appends the value
  barGraph(X,Y) #uses the X and Y values for the 
  lineGraph(X,Y) #uses the X and Y values for the lineGraph
  X = [] #x list
  Y = [] #y list
  with open("employee_count_by_department.txt","r") as rdf: #opens "employee_count_by_department.txt"
      lines = rdf.readlines() #reads lines in file
      for line in lines[1:]: #skips the first line
          tup = line.split(",") #reads over ";"
          X.append(tup[0]) 
          Y.append(int(tup[1]))
  pieChart(X,Y) #plots piechart with X and Y
  
if __name__ == '__main__':
      main()