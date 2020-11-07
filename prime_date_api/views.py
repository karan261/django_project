from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import MyModel
from . serializers import MyModelSerializer
import datetime
from django.http import HttpResponse

# Create your views here.

class apishow(APIView):
    def get(self,request):
        now=datetime.datetime.now()
        date=int(now.strftime("%d"))

        json_data1=MyModel.objects.all()
        serializer=MyModelSerializer(json_data1,many=True)
        if date > 1:
            for i in range(2, date//2):
                if (date % i) == 0:
                    return HttpResponse('Date is not prime so no date')
                else:
                    print('date is prime')
                    return Response(serializer.data)

        else:
            return HttpResponse('Date is not prime so no date')

    def post(self):
        pass
