from tkinter import *

class ITapp():

    def __init__(self):
        self.root = Tk()

        self.root.title("Income Tax Calculator")
        self.root.minsize(600,1200)
        self.root.configure(background="#585858")

        self.label1= Label(self.root, text="IT Compare New and Old Slabs")
        self.label1.configure(font=("Trebuchet MS", 22, "bold"))
        self.label1.pack(pady=(2,5))

        self.name1 = Label(self.root, text="Enter Total Income")
        self.name1.configure(font=("Trebuchet MS", 16, "bold"),background="#585858",foreground="white")
        self.name1.pack(pady=(2, 1))

        self.input_income= Entry(self.root)
        self.input_income.pack(ipadx=35, ipady=10)

        self.name2 = Label(self.root, text="Enter Total Savings")
        self.name2.configure(font=("Trebuchet MS", 16, "bold"),background="#585858",foreground="white")
        self.name2.pack(pady=(2, 1))

        self.input_savings = Entry(self.root)
        self.input_savings.pack(ipadx=35, ipady=10)

        self.click = Button(self.root, text="Calculate", width=23, height=2, command=lambda: self.__calculateTax())
        self.click.configure(font=("Trebuchet MS", 18, "bold"),)
        self.click.pack(pady=(10, 10))

        self.label2 = Label(self.root, text=None)
        self.label2.configure(font=("Trebuchet MS", 16, "bold"),foreground="#585858",background="#585858")
        self.label2.pack(pady=(2, 2))

        self.label3 = Label(self.root, text=None)
        self.label3.configure(font=("Trebuchet MS", 16, "bold"),foreground="#585858",background="#585858")
        self.label3.pack(pady=(2, 2))


        self.root.mainloop()


    def calculateTax_Old(self):

        if self.total_savings < 150000:
            self.max_savings= self.total_savings
        else:
            self.max_savings = 150000

        self.taxable_income = self.total_income - self.max_savings
        rest = self.taxable_income
        slab1=0
        slab2=0
        slab3=0
        slab4=0
        if self.taxable_income > 1000000:
            slab4=(rest-1000000)*0.3
            rest=1000000
        if self.taxable_income>500000:
            slab3=(rest-500000)*0.2
            rest=500000
        if self.taxable_income>250000:
            slab2=(rest-250000)*0.05
            rest=250000
        if self.taxable_income>=0:
            slab1=0
            rest=0
        self.total_tax=slab1+slab2+slab3+slab4

        output="""
        OLD METHOD INCOME TAX
        
        Total Income: {}
        Total Savings: {}
        Maximum Tax savings under 80C: {}
        Total Taxable Income: {}
        Tax Slabs\t\t\tTax
        Rs. 1 to 2,50,000:\t\t {}
        Rs. 2,50,001 to 5,00,000:\t\t {}
        Rs. 5,00,001 to 10,00,000:\t {}
        Rs. 10,00,001 and above:\t\t {}
        Total Tax:\t\t\t {}
        """.format(self.total_income,self.total_savings,self.max_savings,self.taxable_income,slab1,slab2,slab3,slab4,self.total_tax)

        return output

    def calculateTax_New(self):
        self.taxable_income = self.total_income
        rest = self.taxable_income
        slab1=0
        slab2=0
        slab3=0
        slab4=0
        slab5=0
        slab6=0
        slab7=0

        if self.total_income <=500000:
            self.total_tax = 0
        else:

            if self.taxable_income > 1500000:
                slab7=(rest-1500000)*0.30
                rest=1500000
            if self.taxable_income > 1250000:
                slab6=(rest-1250000)*0.25
                rest=1250000
            if self.taxable_income > 1000000:
                slab5=(rest-1000000)*0.20
                rest=1000000
            if self.taxable_income > 750000:
                slab4=(rest-750000)*0.15
                rest=750000
            if self.taxable_income > 500000:
                slab3=(rest-500000)*0.10
                rest=500000
            if self.taxable_income > 250000:
                slab2=(rest-250000)*0.05
                rest=250000
            if self.taxable_income > 0:
                slab1=0
                rest=0
            self.total_tax = slab1 + slab2 + slab3 + slab4 + slab5 + slab6 + slab7

        output = """
        NEW METHOD INCOME TAX
        
        Total Income: {}
        Total Savings: {} but NO Tax savings under 80C
        Total Taxable Income: {}
        Tax Slabs\t\t\tTax
        Rs. 1 to 2,50,000:\t\t {}
        Rs. 2,50,001 to 5,00,000:\t\t {}
        Rs. 5,00,001 to 7,50,000:\t\t {} 
        Rs. 7,50,001 to 10,00,000:\t {}
        Rs. 10,00,001 to 12,50,000:\t {}
        Rs. 12,50,001 to 15,00,000:\t {}
        Rs. 15,00,001 and above:\t\t {}
        Total Tax:\t\t\t {}
        """.format(self.total_income, self.total_savings, self.taxable_income, slab1, slab2, slab3, slab4, slab5, slab6, slab7, self.total_tax)

        return output

    def __calculateTax(self):

        self.total_income = int(self.input_income.get())
        self.total_savings = int(self.input_savings.get())
        text1=self.calculateTax_Old()
        text2=self.calculateTax_New()
        self.label2.configure(text=text1, foreground="white", background="#585858", justify=LEFT)
        self.label3.configure(text=text2, foreground="white", background="#585858", justify=LEFT)

ob=ITapp()