from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import MyModel
from . serializers import MyModelSerializer
import datetime
from django.http import HttpResponse
import math

# Create your views here.

class apishow(APIView):
    def get(self,request):
        now=datetime.datetime.now()
        date=int(now.strftime("%d"))
        json_data1=MyModel.objects.all()
        serializer=MyModelSerializer(json_data1,many=True)

        if date > 1:
            for i in range(2, int(math.sqrt(date))+1):
                if (date % i) == 0:
                    return HttpResponse('Date is not prime so no date')
                                   
            else:        
                print("the number is prime")
                return Response(serializer.data)
        else:                                
            return HttpResponse('Date is not prime so no date')
