import requests
from requests.auth import HTTPBasicAuth

# Replace 'your_api_key' and 'your_api_secret' with your Razorpay API credentials
api_key = 'your_api_key'
api_secret = 'your_api_secret'

# The Razorpay API endpoint to fetch account details
url = 'https://api.razorpay.com/v1/payments'

def check_razorpay_credentials(api_key, api_secret):
    try:
        # Make a GET request to the endpoint using the API key and secret for HTTP Basic Auth
        response = requests.get(url, auth=HTTPBasicAuth(api_key, api_secret))

        # If the response code is 200, the API key and secret are valid
        if response.status_code == 200:
            print('API key and secret are valid.')
            return True
        else:
            # If the response code is not 200, then the credentials are invalid or there's another error
            print(f'Failed to authenticate. Status code: {response.status_code}')
            return False
    except requests.RequestException as e:
        # Handle any other request exceptions
        print(f'An error occurred: {e}')
        return False

# Check Razorpay credentials
check_razorpay_credentials(api_key, api_secret)
