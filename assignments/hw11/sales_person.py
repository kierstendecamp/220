"""
Name: kiersten decamp
hw11.py

Problem: <create a program using objects with lists.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


class SalesPerson:
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self, employee_id):
        self.name = employee_id

    def get_name(self, name):
       return self.name


    def set_name(self, name):
        self.name = input("Kiersten DeCamp")
        return name


    def enter_sale(self, sale):
        self.sales.append(sale)


    def total_sale(self, sale):
        my_sale = 0
        return my_sale(self.sale)

    def get_sales(self,sales):
        i = []
        for i in range(len(float(self.sales))):
            if self.sales[i] >= sales:
                return i


    def met_quota(self):
        return self.quota_sales()


    def compare_to(self, other):
        i = -1
        for i in len(self.other):
            if self.sales[i] >= other:
                return i




