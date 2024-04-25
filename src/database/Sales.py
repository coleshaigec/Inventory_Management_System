import sys
import os
import bcrypt
import random
from urllib.parse import quote_plus
from time import ctime
import subprocess
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure
from datetime import date
import re
from Product import Product
import csv
import json

letters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
capitals = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
numbers = (1,2,3,4,5,6,7,8,9,0)

class Sales(Product):
    
    # Initialise the object
    def __init__(self):
        super().__init__()
        # Connects to the BusinessInventoryChecker database
        URI = "mongodb+srv://" + self.status + ":" + self.status + "@businessinventorychecke.hnarzhd.mongodb.net/?retryWrites=true&w=majority&appName=BusinessInventoryChecker&tlsInsecure=true"
        client = MongoClient(URI, server_api=ServerApi('1'))
        
        # Assign the AccessDetails collection from LoginSystem database to variable called login_DB 
        self.data_base = client['CompanyDetails']
        self.sales_DB = self.data_base['SalesDone']
        
    def revenue_calculator(self, num, cost):
        # range of dates
        # add a date
        document = self.performance_DB.find_one({'num': 1})
        new_revenue = document.get('revenue', 0) + num * cost
        self.performance_DB.update_one({'num': 1}, {'$set': {'revenue': new_revenue}})
        
    def reset_revenue(self):
        document = self.performance_DB.find_one({'num': 1})
        self.performance_DB.update_one({'num': 1}, {'$set': {'revenue': 0}})
        
    def ABC_revenue(self):
        return True
        #range of dates
        # tied to date
        #num * cost per SKU per item
        
        
    def SKU_class(self):
        return True
        
    def sales_to_csv(self):
        with open('sales.csv', 'w', newline='') as csvfile:
            fieldnames = ['date', 'SKU', 'product_name', 'num', 'cost']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in self.place_order_DB.find():
                date = row.get('date')
                SKU = row.get('SKU')
                product_name = row.get('product_name')
                num = row.get('num')
                cost = row.get('cost')
                
            writer.writerow({'date': date, 'SKU': SKU, 'product_name': product_name, 'num': num, 'cost': cost})
        csvfile.close()

    def csv_to_sales(self):
        if self.status != "Admin":
            print("You dont have access to this feature")
        else:
            with open('sales.csv', newline='') as csvfile:
                myreader = csv.reader(csvfile)
            for row in myreader:  
                self.place_order_DB.insert_one({'date': row[0], 'SKU': row[1], 'product_name': row[2], 'num': row[3], 'cost': row[4]})
            csvfile.close()
        
    def add_sale(self):
        return True
        
    def delete_sale(self):
        return True

    def update_sale(self):
        return True

if __name__ == '__main__':
    if len(sys.argv) == 2:
        _, page_number_str = sys.argv
        page_number = int(page_number_str)
        db = Sales()
        # ... existing code to connect to MongoDB ...
        cursor = list(db.sales_DB.find({}, {'_id': 0, 'date': 1, 'SKU': 1, 'product_name': 1, 'num': 1, 'cost': 1,}))
        length = len(cursor)
        data = []
        start = (int(page_number_str)-1) * 50
        for x in range(50):
            if start > length:
                break
            else:
                data.append(cursor[start])
                start += 1
        print(json.dumps(data))  # print JSON data
    else:
        print("Invalid argument")
        sys.exit(1)