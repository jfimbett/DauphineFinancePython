


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

        parser = reqparse.RequestParser()
        parser.add_argument('min_age', required=False)

        args = parser.parse_args()

        # Args is a dictionary
        data = pd.DataFrame()
        if args['min_age'] is not None:
            data = df_ceos[df_ceos['Age'] >= float(args['min_age'])]

        ceos = [data.iloc[i].to_dict() for i in range(len(data))]

        return ceos, 200


class Companies(Resource):

    def get(self):

        parser = reqparse.RequestParser()

        parser.add_argument('ticker', required = False) # If the ticker is mandatory for the request, change to True
        parser.add_argument('min_revenue', required=False)

        args = parser.parse_args()

        # Args is a dictionary
        data = pd.DataFrame()
        if args['ticker'] is not None:
            data = df_companies[df_companies['Ticker'] == args['ticker']]

        if args['min_revenue'] is not None:
            data = df_companies[df_companies['Revenue (billions)'] >= float(args['min_revenue'])]

        companies = [data.iloc[i].to_dict() for i in range(len(data))]

        return companies, 200

api.add_resource(Ceos, '/ceos')
api.add_resource(Companies, '/companies')

if __name__=='__main__':
    app.run()







