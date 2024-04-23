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
import json
import HelperFunctions
from LoginSystem import LoginSystem

letters = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
capitals = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
numbers = (1,2,3,4,5,6,7,8,9,0)




# =====================================
# ADDING, UPDATING AND REMOVING IS LEFT
# =====================================

class Product(LoginSystem):
    
    def __init__(self):
        self.status = "Admin"
        super().__init__()
        URI = "mongodb+srv://" + self.status + ":" + self.status + "@businessinventorychecke.hnarzhd.mongodb.net/?retryWrites=true&w=majority&appName=BusinessInventoryChecker&tlsInsecure=true"
        client = MongoClient(URI, server_api=ServerApi('1'))
        self.data_base = client['CompanyDetails']
        self.product_DB = self.data_base['ProductInformation']
        
    def get_product_everything(self):
        cursor = self.product_DB.find({}, {'_id': 0, 'SKU': 1, 'product_name': 1, 'stock': 1, 'cost': 1, 'inventory_value': 1, 'expected_sales': 1, 'SKU_class': 1})
        data = []
        if cursor:
            for document in cursor:
                data.append(document)
            print(json.dumps(data))
        else:
            print("There are no products")
         
    def get_product_name(self, name):
        cursor = self.product_DB.find({'product_name': name}, {'_id': 0, 'SKU': 1, 'product_name': 1, 'stock': 1, 'cost': 1, 'inventory_value': 1, 'expected_sales': 1, 'SKU_class': 1})
        data = []
        if cursor:
            for document in cursor:
                data.append(document)
            print(json.dumps(data))
        else:
            print("There is no such product with the specified name")
      
    def get_product_SKU(self, SKU):
        cursor = self.product_DB.find({'SKU': SKU}, {'_id': 0, 'SKU': 1, 'product_name': 1, 'stock': 1, 'cost': 1, 'inventory_value': 1, 'expected_sales': 1, 'SKU_class': 1})
        if cursor:
            for document in cursor:
                data.append(document)
            print(json.dumps(data))
        else:
            print("There is no such product with the specified SKU")
            
    def get_product_SKU_class(self, SKU_class):                
        cursor = self.product_DB.find({'SKU_class': choice}, {'_id': 0, 'SKU': 1, 'product_name': 1, 'stock': 1, 'cost': 1, 'inventory_value': 1, 'expected_sales': 1, 'SKU_class': 1})
        if cursor:
            for document in cursor:
                data.append(document)
            print(json.dumps(data))
        else:
            print("There is no product with the specified SKU class!")
        



    
