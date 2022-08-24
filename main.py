'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
class wallet(object):
    bag = []
    def __init__ (self,name,money):
        self.name = name
        self.money = money
    def purchase(self,price,item_name):
        if self.money - price < 0:
            print("_____________________________________________")
            print("Cant make your purchase, your balance is low")
            print("_____________________________________________")
            return 
        self.money -= price 
        self.bag.append([item_name,price])
        print("______________________________________")
        print("Purchase successful, Your Updated balance is : " + str(self.money))
        print("______________________________________")
    def __str__ (self):
        return "Hi " + self.name + " Your updated wallet amount is Rs " + str(self.money)
    def Bag (self):
        return self.bag

print("Enter your name : ",end="")
p = input()
print("Enter your wallet amount : ",end="")
m = int(input())
a = wallet(p,m)
print("__________________________________")
print("To exit press 1, to view main menu press any other key : ",end="")
k = input()
item = {"Chair" : 500, "Bench" : 1000, "Table" : 2000, "Mouse" : 350, "LG TV" : 50000, "Acer Laptop" : 25000, "Travel Bag" : 1900, "Lan Cable" : 250, "Earphones" : 2000,
"Ipad" : 30000, "Watch" : 5000}
alphlower = {k6.lower(): v for k6, v in item.items()}


while(k != '1'):
    print("__________________________________")
    print("1. To view your balance, press 1")
    print("2. To view item list, press 2")
    print("3. To view your purchases, press 3")
    print("4. To exit, press 4")
    print("___________________________________")
    print("Enter your choice : ",end="")
    k1 = input()
    if(k1 != '4'):
        if k1 == '1':
            print(a)
        elif k1 == '2':
            print(item)
        elif k1 == '3':
            li = a.Bag()
            if len(li) == 0:
                print("YOU HAVE NOT PURCHASED ANY ITEM YET")
                continue
            count = 1
            for i in range(1,len(li)+1):
                print(str(i) + ". Item : " + li[i-1][0].capitalize() + " ; price: " + str(li[i-1][1]))
    else:
        break
    print("__________________________________")
    print("To purchase press 1, press any other to exit : ",end="")
    k2 = input()
    if k2 == '1':
        print("Enter Item name to purchase : ",end = "")
        k3 = input()
        k3 = k3.lower()
        if k3 in alphlower:
            a.purchase(alphlower[k3],k3)
        else:
            print("Name entered incorrectly, Please try again")
    
    