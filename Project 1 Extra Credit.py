#Shamsadean Mirghani
#Project1.py
#This program will calculate taxes and total purchase price
#For a given amount of purchases and display them in a table

def main():
    # Constants
    STATETAX= .045
    LOCALTAX= .025
    
    # Handshake
    print("This program will compute the taxes for a given amount of purchases and will display the total purchase price")

    # Input for purchases is rendered
    x = eval(input("Enter number of purchases: "))

    
    a = []
    b = []
    c = []
    d = []
    # For loop used to calculate the inputs that were rendered
    for i in range(x):
        z=str(i+1)
        y = eval(input("Please enter price of item "+z+": "))
        StateTax = (STATETAX * y)
        a.append(StateTax)
        LocalTax = (LOCALTAX * y)
        b.append(LocalTax)
        TotalTax = (LocalTax + StateTax)
        c.append(TotalTax)
        PurchasePrice = (y + TotalTax)
        d.append(PurchasePrice)
        #print("StateTax: {0:.2f}" .format(StateTax))
        #print("Local Tax: {0:.2f}".format(LocalTax))
        #print("Total Tax: {0:.2f}".format(TotalTax))
        #print("Purchase Price {0:.2f}".format(PurchasePrice))
        
    print("State Tax    Local Tax     Total Tax   Purchase Price")
    for j in range(x):
        print("$ {0:.2f}       ${1:.2f}          ${2:.2f}         ${3:.2f}" .format(a[i],b[i],c[i], d[i]))          
main()
