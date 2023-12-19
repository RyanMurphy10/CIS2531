#######################################################################################
#Assgn_10 Ryan Murphy 
# Class Services: Manages service-related information such as number of hours and rate per hour.
# Class Supplies: Manages supply-related information such as number of items and price per item.
#main(): Demonstrates the usage of Services and Supplies classes by creating instances, modifying attributes, calculating costs, and displaying information.
#Create instances of Services and Supplies classes.
#Modify attributes using getter and setter methods.
#Calculate and display the cost accrued for each object.
#######################################################################################
class Services:
  def __init__(self, number_of_hours, rate_per_hour): #constructor class that takes in number of hours and rate per hour
      self.__number_of_hours = number_of_hours 
      self.__rate_per_hour = rate_per_hour

  def get_number_of_hours(self): #Getter and setter for numberOfHours
      return self.__number_of_hours

  def set_number_of_hours(self, number_of_hours): #function to set number of hours
      self.__number_of_hours = number_of_hours

  def get_rate_per_hour(self):   #Getter and setter for ratePerHour
      return self.__rate_per_hour

  def set_rate_per_hour(self, rate_per_hour): #function to set rate per hour
      self.__rate_per_hour = rate_per_hour

  def calculate_sales(self): #Method to calculate cost accrued for services
      return self.__number_of_hours * self.__rate_per_hour #returns cost accrued for services

  def __str__(self): #String representation of Services
      return f"Services - Hours: {self.__number_of_hours}, Rate per Hour: ${self.__rate_per_hour}" #returns string representation of services


class Supplies:
  def __init__(self, number_of_items, price_per_item): #function to initialize number of items and price per item
      self.__number_of_items = number_of_items
      self.__price_per_item = price_per_item

  def get_number_of_items(self): #Getter and setter for numberOfItems
      return self.__number_of_items

  def set_number_of_items(self, number_of_items): #function to set number of items
      self.__number_of_items = number_of_items

  def get_price_per_item(self): #Getter and setter for pricePerItem
      return self.__price_per_item #returns price per item

  def set_price_per_item(self, price_per_item): #function to set price per item
      self.__price_per_item = price_per_item

  def calculate_sales(self): #Method to calculate cost accrued for supplies
      return self.__number_of_items * self.__price_per_item #returms cost accrued for supplies

  def __str__(self): #String representation of Supplies
      return f"Supplies - Items: {self.__number_of_items}, Price per Item: ${self.__price_per_item}" #returns string representation of supplies


def main():

  service_1 = Services(5, 20.0) #creates instance of Services class
  service_2 = Services(8, 25.0) #creates instance of Services class

  supply_1 = Supplies(50, 2.5) #creates instances of Supplies class
  supply_2 = Supplies(100, 1.8) #creates instances of Supplies class

  service_1.set_number_of_hours(6) #sets number of hours for service 1
  supply_2.set_price_per_item(2.0) #sets price per item for supply 2

  services_list = [service_1, service_2]
  supplies_list = [supply_1, supply_2]

  for service in services_list: #checks for service in service list
      print(service) #prints service
      print(f"Cost accrued: ${service.calculate_sales()}")
      print()

  for supply in supplies_list: #checks for supply in supply list
      print(supply)
      print(f"Cost accrued: ${supply.calculate_sales()}")
      print()


if __name__ == "__main__":
  main()