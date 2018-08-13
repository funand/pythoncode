"""This is a Tab calculator. It is used to calculate how much tip,
tax, and total of the bill would be. Caqn be used at restaurants
and bars """
class Tab(object):#tab calculator class
    tax = 0
    """docstring for Tab."""
    def __init__(self, name, bill, tip): #__init__ or constructor
        self.name = name
        self.bill = bill
        self.tip = tip
        self.tax = 8.75

    def tipCalculator(self): #calculates the tip to be left
        #U must leave at least a 20 percent tip BE NICE!!!!!
        while(int(self.tip)<20):
            self.tip = int(input("Be nice, Re-Enter tip%: "))
        return (self.tip)/100 * self.bill

    def taxCalculator(self): #calculates the tax for the bill
        # tax is 8.75% of your biill
        return (self.tax)/100 * self.bill

    def tabTotal(self): #calculates the total for the bill
        return self.bill + self.tax + self.tipCalculator()

name = input("Kindly tell me your name: ")
print ("Hello, "+name+ " welcome to the Tab Calculator")
bill = int(input("What is your bill: "))
tip = int(input("How much tip% are you leaving: "))

my_bill = Tab(name, bill, tip)
tip = int(my_bill.tipCalculator())
print ("\nTab Breakdown:")
print ("Tip:   ", tip)
print ("Tax:   " +  str(my_bill.taxCalculator()))
print ("Total: " + str(my_bill.tabTotal()))
print ("\nThank you for using the Tab Calculator", name)
