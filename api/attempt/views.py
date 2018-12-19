from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.http import urlquote
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.conf import settings
from django.utils import timezone
from ipaddress import ip_address
from datetime import datetime

import requests
import pprint
import re
import sys
import os
import logging
import json
import pickle
import shlex
import subprocess
import copy
import time
import uuid

class LocalFunctions:

    def __init__(self, request):
        print(request.session)
        self.uuid = str(uuid.uuid1())
        self.body = request.POST
        self.response = {
            "time": None,
            "id": None,
            "code": None,
            "message": None,
            "results": []
        }

        fullPath = request.get_full_path()

    def resp(self, status_level, status_message, jsonData):
        self.response['time'] = timezone.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        self.response['id'] = self.uuid
        self.response['code'] = status_level
        self.response['message'] = status_message
        self.response['results'].append(jsonData)

    def jResp(self, resp, status, safe=False):
        return JsonResponse(resp, status=status, safe=safe)

    def proccess_request(self, request, param1):
        def build_jResp(body):
            jsonR = body
            return jsonR

        if request.method == 'POST':
            j = build_jResp('STANK')
            self.resp('INFO', "Successfully returned the body you sent with method POST!", j)
            return self.jResp(self.response, status=status.HTTP_200_OK, safe=False)

        elif request.method == 'GET':
            j = build_jResp(param1)
            self.resp('INFO', "Successfully returned the body you sent with method GET!", j)
            return self.jResp(self.response, status=status.HTTP_200_OK, safe=False)
        
class API_PROCCESSOR(APIView):
    def get(self, request, param1, format=None):
        lf = LocalFunctions(request)
        if param1 == '':
            param1 = request.GET.get('param1')
        proccess_resp = lf.proccess_request(request=request, param1=param1)
        if proccess_resp:
            return proccess_resp
        else:
            r = lf.resp('ERROR,', 'Unable to process response, go into debug mode and figure it out biatch!', None)
            return lf.jResp(r, status=status.HTTP_400_BAD_REQUEST, safe=False)

    def post(self, request, param1=None, format=None):
        lf = LocalFunctions(request)
        if param1 == '':
            param1 = request.GET.get('param1')
        proccess_resp = lf.proccess_request(request=request, param1=param1)
        if proccess_resp:
            return proccess_resp
        else:
            r = lf.resp('ERROR,', 'Unable to process response, go into debug mode and figure it out biatch!', None)
            return lf.jResp(r, status=status.HTTP_400_BAD_REQUEST, safe=False)
        

