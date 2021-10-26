

from flask import Flask
from flask_restful import Resource, Api, reqparse
import ast

import pandas as pd

app = Flask("My App")
api = Api(app)


ceos = [{"Name" : "Doug McMillion", "Age" : 55},
        {"Name" : "Fu Chengyu", "Age" : 70}, 
        {"Name" : "Andy Jassy", "Age" : 53}, 
        {"Name" : "Zhou Jiping", "Age" : 69}, 
        {"Name" : "Tim Cook", "Age" : 60}]

companies = [{"Name" : "Walmart Inc.", "Ticker" : "WMT", "Revenue (billions)" : 542, "CEO" : "Doug McMillion"},
             {"Name" : "China Petroleum and Chemical Corp.", "Ticker" : "SNP", "Revenue (billions)" : 355.8, "CEO" : "Fu Chengyu"},
             {"Name" : "Amazon.com Inc", "Ticker" : "AMZN", "Revenue (billions)" : 321.8, "CEO" : "Jeff Bezos"}, 
             {"Name" : "PetroChina Co. Ltd", "Ticker" : "PTR", "Revenue (billions)" : 320, "CEO" : "Zhou Jiping"}, 
             {"Name" : "Apple Inc.", "Ticker" : "AAPL", "Revenue (billions)" : 273.9, "CEO" : "Tim Cook"}]

df_ceos = pd.DataFrame.from_dict(ceos)

df_companies = pd.DataFrame.from_dict(companies)


class Ceos(Resource):
    
    def get(self):
        ceos = [df_ceos.iloc[i].to_dict() for i in range(len(df_ceos))]
        return  ceos , 200 # The 200 is the standard way to say everything is ok

class Companies(Resource):
    
    def get(self):
        companies = [df_companies.iloc[i].to_dict() for i in range(len(df_companies))]
        return  companies , 200 # The 200 is the standard way to say everything is ok

api.add_resource(Ceos, '/ceos')
api.add_resource(Companies, '/companies')

if __name__=='__main__':
    app.run()
