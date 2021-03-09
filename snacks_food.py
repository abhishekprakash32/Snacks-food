# Using while loop, list, dictionary and table format & datetime packages from(https://pypi.org/)

from Color_Console import color
color('black','blue')
#from tabulate import tabulate
from texttable import Texttable
import itertools
a = "Sai Snacks Centre"
print(a.center(72,'*'))

e = 'yes'
while(e == 'yes'):
    Sr_No = [1,2,3,4,5]
    Food_item = ['Poha','Shira','Tea','Coffee','cookie']
    price = [15,20,10,12,25]
    t = Texttable()
    t.add_rows([['Sr No','Food item','price'],[Sr_No[0],Food_item[0],price[0]],
    [Sr_No[1],Food_item[1],price[1]],[Sr_No[2],Food_item[2],price[2]],[Sr_No[3],Food_item[3],price[3]],[Sr_No[4],Food_item[4],price[4]]])
    print(t.draw())
    #print(tabulate([[Sr_No,Food_item,price]], headers=['Sr No','Food item','price per item'],tablefmt='orgtbl'))
    print("**********************************************************")
    b = input("Enter Customer Name=")
        
    
    print("************************Customer Info*********************")
    print(f"Customer Name={b}")
    import random
    n = random.randint(101,200)
    print(f"Bill No.={n}")
    from datetime import datetime
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("Date and Time =", dt_string)	

    dict1 = {"1":["Poha",15],"2":["Shira",20],"3":["Tea",10],"4":["Coffee",12],"5":["Cookie",25]}
 
    r = []
    r1 = []
    quant1 = []
    total2 = []
    Sr_No1 = 1
    quant1 = []
    grand_total1 = []
    grand_total = 0
    for i in range(5):
        b = input("Enter Food Item Code=")
        x = dict1.get(b)
        z = x[0]
        o = x[1]
        r.append(z)
        
        
        r1.append(o)
        quant = int(input("Enter Quantity"))
        quant1.append(quant)
        total1 = o * quant
        total2.append(total1)
        grand_total = grand_total + total1
        grand_total1.append(grand_total)
        e = input("Do you want more items? yes/no=")
         
        
        s=[1,2,3,4]
        
        if e == 'no':
            print("****************** Your Bill *****************************")
            print("Sr No.\tFood Item\tRate\tQuantity\tTotal")
            for s1,j,k,m,l in zip(s,r,r1,quant1,total2):
                
                print(f"{s1}\t{j}\t\t{k}\t{m}\t\t{l}\t\t")
            print("---------------------------------------------------")
            print(f"                                     Grand Totl={grand_total}")
            print(f"Your Total Bill is Rs {grand_total}/- only.")
            print("Thanks for visting!!!!! Come Again!!!!!!")
            exit()
               

