from django.shortcuts import render
from django.http import JsonResponse
import pymongo
# from pymongo import Connection


MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DBS_NAME = 'donorschoose'
COLLECTION_NAME = 'projects'
FIELDS = {'school_state': True, 'resource_type': True, 'poverty_level': True, 'date_posted': True, 'total_donations': True, '_id': False}


def api(request):
    connection = pymongo.Connection(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DBS_NAME][COLLECTION_NAME]
    projects = collection.find(fields=FIELDS)
    json_projects = []
    for project in projects:
        json_projects.append(project)
    return JsonResponse(json_projects)


def home(request):
    return render(request, "index.html")
