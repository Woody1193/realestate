from requests import (
    get,
    Response
)

PhoneNumber = 'phonenumber'
TextQuery = 'textquery'

class GooglePlacesSearchProvider():

    def __init__(self, baseUri: str, apiKey: str):
        self.BaseUri = baseUri
        self.ApiKey = apiKey
    
    def get_by_phone_number(self, phone: str, language: str):
        return get(self.BaseUri, params = self.get_params(PhoneNumber, phone, language))
    
    def get_by_address(self, address: str, language: str):
        return get(self.BaseUri, params = self.get_params(TextQuery, address, language))
    
    def get_params(self, input_type: str, input_str: str, language: str):
        return {
            'key': self.ApiKey,
            'inputtype': input_type,
            'input': input_str,
            'fields': 'name,formatted_address,geometry,plus_code,place_id,id',
            'language': language
        }