from fastapi import FastAPI 
from flask import request, jsonify
import json
import requests

app = FastAPI()


@app.get('/')
def home():
    return '''<h1>Covid 19 Api</h1>
<p>A prototype API for getting covid stats.</p>'''

@app.get('/{id}')
def api_id(id: str):
    # Create an empty list for our results
    results = []
    with open ('/home/divyessh/Desktop/covid/Covid19Api/data/data.json','r') as f:
        books = json.load(f)  

        # Loop through the data and match results that fit the requested ID.
        # IDs are unique, but other fields might return many results
        for book in books:
            if book == id:
                results.append(books[book])
            
        if len(results) == 0:
            results.append('none')

        return results[0]