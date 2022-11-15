class Product:
  def __init__(self, ID, name, quantity, cost):
    self.ID = ID
    self.name = name
    self.quantity = quantity
    self.cost = cost

  def myfunc(self):
    print('(' + str(self.ID) + ') ' + str(self.name) + " $ " + str(self.cost))

  def setProductID(self,x):
      self.ID = x
  def setProductname(self,x):
      self.name = x
  def setProductquantity(self,x):
      self.quantity = x
  def setProductcost(self,x):
      self.cost = x 

  def getProductID(self):
     return self.ID
  def getProductname(self):
     return self.name
  def getProductquantity(self):
     return self.quantity
  def getProductcost(self):
     return self.cost

Productlist = []
Productlist.append(Product(0,"Ultrasonic range finder", 4, 2.50))
Productlist.append(Product(1,"Servo motor",10,14.99))
Productlist.append(Product(2,"Servo Controller",5,44.95))
Productlist.append(Product(3,"Microcontroller Board",7,34.95))
Productlist.append(Product(4,"Laser range finder",2,149.99))
Productlist.append(Product(5,"Lithium polymer battery",8,8.99))


def print_stock():
    print("\nAvailable Products")
    print("---------------")
    for i in range(0,6):
        Productlist[i].myfunc()
    print()

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        print_stock()
        vals = input("Enter Product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit": break

        prod_id = int(vals[0])
        count = int(vals[1])

        if Productlist[prod_id].getProductquantity() >= count:
            if cash >= Productlist[prod_id].getProductcost():
                Productlist[prod_id].getProductquantity() * count
                cost = Productlist[prod_id].getProductcost() * count
                cash -= cost
                print("You purchased", count, Productlist[prod_id].getProductname() + " for $" + str(cost) + ".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
                Productlist[prod_id].setProductquantity(Productlist[prod_id].getProductquantity() - count)
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we do not have that many", Productlist[prod_id].getProductname())


main()