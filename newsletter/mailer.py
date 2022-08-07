import os
import time
import environ
import requests
from .models import Mailing, Client, Message

env = environ.Env(
        #set casting, default value
        DEBUG=(bool, False)
)

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
DEBUG = env('DEBUG')

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')
URL = env('URL')

def send_message(ids, url = URL, token = SECRET_KEY):

    header = {

            'Authorization': f'Bearer {token}',
            
            'Content-Type': 'application/json'
            
            }

    mailing = Mailing.objects.filter(id=ids).first()
    
    clients = Client.objects.filter(code=mailing.mobile_codes).all()

    for client in clients:

        messages = Message.objects.filter(
                client_id = client.id).select_related(
                        'client', 
                        'mailing').all()

        for message in messages:

            data = {
                    
                    'id': message.id,     
                    
                    'phone': client.phone,
                    
                    'text': mailing.text
                                                                                                                        }

            count = 0

            try:
            
                response = requests.post(url=url + str(message.id), headers=header, json=data)

                print(response.status_code)

                while response.status_code != 200 and count < 200:
                
                    time.sleep(2)
                    
                    count += 1
                    
            except ConnectionError:
            
                return f'Connection error, please contact your network administrator!'


