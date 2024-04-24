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

letters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
capitals = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
numbers = (1,2,3,4,5,6,7,8,9,0)

# =====================================
# ADDING, UPDATING AND REMOVING IS LEFT
# =====================================

class Sales(Product):
    
    def __init__(self):
        super().__init__()
        URI = "mongodb+srv://" + self.status + ":" + self.status + "@businessinventorychecke.hnarzhd.mongodb.net/?retryWrites=true&w=majority&appName=BusinessInventoryChecker&tlsInsecure=true"
        client = MongoClient(URI, server_api=ServerApi('1'))
        self.data_base = client['CompanyDetails']
        self.sales_DB = self.data_base['SalesDone']
        
    def total_revenue_calculator(self, start_date, end_date):
        start_date = normal_date_checker(start_date)
        end_date = normal_date_checker(end_date)
        cursor = sales_DB.find({}, {'_id': 0, 'date': 1, 'SKU': 0, 'product_name': 0, 'num': 1, 'cost': 1})
        if start_date != False and end_date != False:
            if cursor:
                for document in cursor:
                    if datetime.strptime(start_date, "%Y-%m-%d") <= datetime.strptime(document.get('date', 'N/A'), "%Y-%m-%d") <= datetime.strptime(end_date, "%Y-%m-%d"):
                        num = float(document.get('num', 0))
                        cost = float(document.get('cost', 0))
                        revenue += num * cost
                print(revenue)
        else:
            return False
                    
    def SKU_revenue_calculator(self, SKU, start_date, end_date):
        start_date = normal_date_checker(start_date)
        end_date = normal_date_checker(end_date)
        cursor = sales_DB.find({'SKU': SKU}, {'_id': 0, 'date': 1, 'SKU': 0, 'product_name': 0, 'num': 1, 'cost': 1})
        if start_date != False and end_date != False:
            if cursor:
                for document in cursor:
                    if datetime.strptime(start_date, "%Y-%m-%d") <= datetime.strptime(document.get('date', 'N/A'), "%Y-%m-%d") <= datetime.strptime(end_date, "%Y-%m-%d"):
                        num = float(document.get('num', 0))
                        cost = float(document.get('cost', 0))
                        revenue += num * cost
                print(revenue)
        else:
            return False
        
    def name_revenue_calculator(self, product_name, start_date, end_date):
        start_date = normal_date_checker(start_date)
        end_date = normal_date_checker(end_date)
        cursor = sales_DB.find({'product_name': product_name}, {'_id': 0, 'date': 1, 'SKU': 0, 'product_name': 0, 'num': 1, 'cost': 1})
        if start_date != False and end_date != False:
            if cursor:
                for document in cursor:
                    if datetime.strptime(start_date, "%Y-%m-%d") <= datetime.strptime(document.get('date', 'N/A'), "%Y-%m-%d") <= datetime.strptime(end_date, "%Y-%m-%d"):
                        num = float(document.get('num', 0))
                        cost = float(document.get('cost', 0))
                        revenue += num * cost
                print(revenue)
        else:
            return False

        
        
        
        
        
        
        
        
        
        
        
        
        

        
    def ABC_revenue(self):
        return True
        #range of dates
        # tied to date
        #num * cost per SKU per item
        
        
    def SKU_class(self):
        return True
        


        


        
        
        
        
        
