from django.db import models


import requests

def my_default():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=delhi&appid=c9a0d14cd73a71d381378454be7a9ba2'
    return requests.get(url).json()

class MyModel(models.Model):
    json_data= models.JSONField(default=my_default)


