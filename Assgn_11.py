#######################################################################################
#Assgn_11 Ryan Murphy 
#Employee Class: Represents an employee with name and employee number attributes.
#ProductionWorker Class: Represents a production worker, a subclass of Employee, with additional attributes for shift number and hourly pay rate.
#ShiftSupervisor Class: Represents a shift supervisor, a subclass of Employee, with attributes for annual salary and annual production bonus.
#get_annual_salary(): Retrieves the annual salary.
#set_annual_salary(annual_salary: float): Sets the annual salary.
#get_annual_production_bonus(): Retrieves the annual production bonus.
#set_annual_production_bonus(annual_production_bonus: float): Sets the annual production bonus.
#######################################################################################
class Employee: # Employee class
  def __init__(self, name, number): #function `
      self._name = name  #Protected members
      self._number = number #Protected members

class ProductionWorker(Employee): #ProductionWorker class
  def __init__(self, name, number, shift_number, hourly_pay_rate): #function that takes in employee name, number, shift number and hourly pay rate
      super().__init__(name, number) #sets the name and number of the employee
      self.shift_number = shift_number #sets the shift number
      self.hourly_pay_rate = hourly_pay_rate #sets the hourly pay rate

  def getShift(self): #function that returns the shift number
      return self.shift_number #returns the shift number

  def getHourlyPayRate(self): #function that returns the hourly pay rate
      return self.hourly_pay_rate

  def __str__(self): #function that returns the name and number of the employee
      if self.shift_number == 1: #checks if the shift number is 1
          return "Employee Number: " + str(self._number) + ", Name: " + self._name + ", Day shift, Hourly Pay Rate: " + str(self.hourly_pay_rate) #retruns the name and number of the employee and the day shift and hourly pay rate
      else:   
          return "Employee Number: " + str(self._number) + ", Name: " + self._name + ", Night shift, Hourly Pay Rate: " + str(self.hourly_pay_rate) #returns the name and number of the employee and the night shift and hourly pay rate

class ShiftSupervisor(Employee): #class that represents a shift supervisor
  def __init__(self, name, number, annual_salary, production_bonus): #function that takes in employee name, number, annual salary and production bonus
      super().__init__(name, number) #super function that sets the name and number of the employee
      self.annual_salary = annual_salary 
      self.production_bonus = production_bonus

  def getAnnualSalary(self): #function that returns the annual salary
      return self.annual_salary #returns the annual salary

  def getBonus(self): #function that returns the production bonus
      return self.production_bonus

  def getSalary(self): #funtion that returns the annual salary plus the production bonus
      return self.annual_salary + self.production_bonus

  def __str__(self): #function that returns the name and number of the employee
      return "Employee Number: " + str(self._number) + ", Name: " + self._name + ", Annual Salary: " + str(self.annual_salary) + ", Bonus: " + str(self.production_bonus) + ", Total Salary: " + str(self.getSalary()) #returns the name and number of the employee, annual salary, bonus and total salary


ProductionWorker1 = ProductionWorker("James Green", 1, 1, 1000) #creates a production worker object
ProductionWorker2 = ProductionWorker("Ana Walter", 2, 2, 2000)
listOfProductionWorker = [ProductionWorker1,ProductionWorker2] #creates a list of production workers
for object in listOfProductionWorker: #checks for each object in the list
  print(object) #prints the object
  
ShiftSupervisor1 = ShiftSupervisor("John William", 3, 10000, 2000)
ShiftSupervisor2 = ShiftSupervisor("Rachel Green", 4, 20000, 3000)
listOfShiftSupervisor = [ShiftSupervisor1, ShiftSupervisor2]
for object in listOfShiftSupervisor:
  print(object)