from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from rest_framework.decorators import api_view
import json
import csv
import requests
import uuid

# Create your views here.

@api_view(["PUT","GET"])

def idealweight(request):
    if request.method == 'PUT':
        try:
            header = ['uuid','height']
            height=request.data['height']
            a = uuid.uuid1()
            a = str(a)
            rows = [a,height]
            with open('data.csv','wt') as f:
                   csv_writer = csv.writer(f)
                   csv_writer.writerow(header)
                   #for row in rows:
                   csv_writer.writerow(rows)
            f.close()

            return JsonResponse("Your height should be:"+"  "+height+" m,your uuid is" + a,safe=False)

        except ValueError as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        try:
            uid=request.data['uuid']
            with open('data.csv','rt') as f:
                   reader = csv.reader(f,delimiter=',')
                   for item in reader:
                      print(item)
                      if (str(item[0]) == str(uid)):
                         return JsonResponse("Your height should be:"+item[1]+"  "+uid,safe=False)
                   return JsonResponse("404 Page Not Found" + uid,safe=False)
            f.close()
        except ValueError as e:
            return Response(e.args[0],status.HTTP_400_BAD_REQUEST)
