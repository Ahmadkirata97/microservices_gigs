from flask import jsonify, request, Blueprint
from Helper_api.requests import Requests
from Helper_api.elastic import logger
from Helper_api.errorhandlers import ServerError
from dotenv import load_dotenv
import os 


load_dotenv('/usr/src/app/.env')
service_url = os.getenv('AUTH_BASE_URL')
base_url = f"{service_url}/api/v1/auth"
auth_client = Requests(service_url=base_url)
auth_blue_print = Blueprint('auth', __name__, url_prefix='/api/v1/auth')     



def gatewayHealth():
    return jsonify("gateway server is Healthy and OK... "), 200


@auth_blue_print.route('/signup', methods=['POST'])
def signupAuth():
    try:
        response = auth_client.makeRequest(endpoint='signup', service_token='auth')
        return response
    except Exception as err:
        logger.error(f"Error in signupAuth() Function, the Error is : {str(err)}")
        raise ServerError("Internal Server Error", "signupAuth() Function")
    

@auth_blue_print.route('/signin', methods=['POST'])
def signInAuth():
    try:
        response = auth_client.makeRequest(endpoint='signin', service_token='auth')
        return response
    except Exception as err:
        logger.error(f"Error in signinAuth() Function, the Error is : {str(err)}")
        raise ServerError("Internal Server Error", "signinAuth() Function")
    
@auth_blue_print.route('/verify-email', methods=['PUT'])
def verifyEmail():
    try:
        response = auth_client.makeRequest(endpoint=f"verify-email", service_token='auth')
        return response
    except Exception as err:
        logger.error(f"Error in verifyEmail() Function, the Error is : {str(err)}")
        raise ServerError("Internal Server Error", "verifyEmail() Method")
    

    
@auth_blue_print.route('/reset-password', methods=['PUT'])
def resetPassword():
    try:
        response = auth_client.makeRequest(endpoint=f"reset-password", service_token='auth')
        return response
    except Exception as err:
        logger.error(f"Error in resetPassword() Function, the Error is : {str(err)}")
        raise ServerError("Internal Server Error", "resetPassword() Function")




@auth_blue_print.route('/reset-token', methods=['PUT'])
def resetToken():
    try:
        response = auth_client.makeRequest(endpoint='reset-token', service_token='auth')
        return response
    except Exception as err:
        logger.error(f"Error in resetToken() Function, the Error is : {str(err)}")
        raise ServerError("Internal Server Error", "resetToken() Function")
    
@auth_blue_print.route('/currentuser', methods=['GET'])   
def getCurrentUser():
    try:
        response = auth_client.makeRequest(endpoint='currentuser', service_token='auth')
        return response
    except Exception as err:
        logger.error(f"Error in getCurrentUser() Function, the Error is : {str(err)}")
        raise ServerError("Internal Server Error", "getCurrentUser() Function")


@auth_blue_print.route('/resend-email', methods=['POST'])
def resendEmail():
    try:
        response = auth_client.makeRequest(endpoint='resend-email', service_token='auth')
        return response
    except Exception as err:
        logger.error(f"Error in resendEmail() Function, the Error is : {str(err)}")
        raise ServerError("Internal Server Error", "resendEmail() Function")
    

def getRefreshToken(username):
    try:
        response = auth_client.makeRequest(endpoint=f"refresh-token/{username}", service_token='auth')
        return response
    except Exception as err:
        logger.error(f"Error in getRefreshToken() Function, the Error is : {str(err)}")
        raise ServerError("Internal Server Error", "getRefreshToken() Function")
    

def searchGigs():
    try:
        response = auth_client.makeRequest(endpoint='search-gig', service_token='auth')
        return response
    except Exception as err:
        logger.error(f"Error in searcGigs() Function, the Error is : {str(err)}")
        raise ServerError("Internal Server Error", "searchGigs() Function")
        


    


    