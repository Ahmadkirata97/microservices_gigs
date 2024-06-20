from flask import jsonify, request
from dotenv import load_dotenv
from Helper_api.cloudinary import uploadCloudinaryFile
import jwt 
import os 
import requests
import json

load_dotenv('.env')


class Requests():
    def __init__(self, service_url):
        self.service_url = service_url
        self.key = os.getenv('GATEWAY_JWT_TOKEN')

    def getJwtToken(self, service_token):
        payload = {
            'service_name': service_token,
        }
        jwt_token = jwt.encode(payload, self.key, algorithm='HS256')
        return jwt_token
    
    
    def makeRequest(self,endpoint, service_token):
        print('Data in the Request: ', request.get_data())
        print('URL of the Destination Service is :', self.service_url)
        jwt_token = self.getJwtToken(service_token=service_token)
        headers = {
            'Authorization': f"Bearer {jwt_token}",
            'Content-Type': 'application/json'
        }
        url = f"{self.service_url}/{endpoint}"
        if request.files:
            image = request.files.get('profile_pic')
            image_url = uploadCloudinaryFile(image)
            data = {
                'username': request.form.get('username'),
                'email': request.form.get('email'),
                'password': request.form.get('password'),
                'country': request.form.get('country'),
                'profile_pic': image_url,
            }
            response = requests.request(
                method= request.method,
                url= url,
                headers= headers,
                json= data,
                params= request.args,
                cookies= request.cookies,
                allow_redirects= False
            )
        else:
            response = requests.request(
                method= request.method,
                url= url,
                headers= headers,
                json= dict(request.form),
                params= request.args,
                cookies= request.cookies,
                allow_redirects= False
            )
        response.content.decode('utf-8')
        response_json = json.loads(response.content)
        return json.dumps(response_json)
    