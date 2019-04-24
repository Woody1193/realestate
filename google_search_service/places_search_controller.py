from google_search_service.places_search import GooglePlacesSearchProvider
from google_search_service import app

from flask import json
from requests import Response

@app.App.route('/search')
def index(self):
    return 'INDEX'

@app.App.route('/search/phone/<phone>/<language>')
def search_with_phone_number(phone: str, language: str):
    resp = app.PlacesProvider.get_by_phone_number(phone, language)
    return from_response(resp)
    
@app.App.route('/search/address/<address>/<language>')
def search_with_address(address: str, language: str):
    resp = app.PlacesProvider.get_by_address(address, language)
    return from_response(resp)

def from_response(resp: Response):
    return json.dumps(resp.json(), ensure_ascii = False)
