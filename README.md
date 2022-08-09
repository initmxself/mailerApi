# mailerApi
Django based notification service

## Installation process

1. clone this repo: 

   `git clone https://github.com/initmxself/mailerApi.git`

2. create a virtual environment

   `python -m venv <envnamegoeshere>`

3. activate the  virtual environment

   `source <envnamegoeshere>/bin/activate`

4. install all the necessary dependancies

   `pip install -r requirements.txt`
   
5. navigate to the downloaded repo
 
   `cd mailerApi`

6. make migrations

   `python manage.py makemigrations && python manage.py migrate`
