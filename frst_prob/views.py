from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from frst_prob import frst_api,scnd_api
from django.views.decorators.csrf import csrf_exempt
import json
import pprint

# Create your views here.
def index(request):
    return HttpResponse(" hello")
@csrf_exempt
def show_values(request):
    if request.method == "GET":
        result = []
        element = frst_api.final_values
        for val in element:
            dta={ 'coordinates' : val }
            result.append(dta)
        return HttpResponse(json.dumps(result))
fnl_lst = []
def find_cordinates(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        for ele in data:
            coordnt = scnd_api.addr_coordinate(ele)
            fnl_lst.append({ 'add': ele, 'location': coordnt })
        pprint(fnl_lst)
        return HttpResponse("done")



