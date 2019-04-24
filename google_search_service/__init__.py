from flask import Flask

from google_search_service.places_search import GooglePlacesSearchProvider

class AppDefinition:

    def __init__(self):
        self.App = Flask(__name__, instance_relative_config = True)
        self.PlacesProvider = GooglePlacesSearchProvider(
            'https://maps.googleapis.com/maps/api/place/findplacefromtext/json',
            'AIzaSyCqdwRW3hJxKyDeSYCR2AnmD4MuaeRYj-Y')

app = AppDefinition()

import google_search_service.places_search_controller