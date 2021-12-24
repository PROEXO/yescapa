from django.http import HttpResponse
import json
from datetime import datetime

with open('campers/level1/campers.json') as campers_l1:
    campers_l1_data = json.load(campers_l1)

with open('campers/level1/searches.json') as searches_l1:
    searches_l1_data = json.load(searches_l1)

with open('campers/level2/campers.json') as campers_l2:
    campers_l2_data = json.load(campers_l2)

with open('campers/level2/searches.json') as searches_l2:
    searches_l2_data = json.load(searches_l2)

with open('campers/level3/campers.json') as campers_l3:
    campers_l3_data = json.load(campers_l3)

with open('campers/level2/searches.json') as searches_l3:
    searches_l3_data = json.load(searches_l3)

with open('campers/level3/calendars.json') as calendars_l3:
    calendars_l3_data = json.load(calendars_l3)


resultBox = []


def boundingBox(longitude, latitude, dist):
    lonMin = longitude - dist
    lonMax = longitude + dist
    latMin = latitude - dist
    latMax = latitude+ dist
    return (lonMin, latMin, lonMax, latMax)

def my_engine_level1(request):
    campers = []
    searches = []
    resultBox = []

    for i in campers_l1_data['campers']:
        campers.append(i)

    for i in searches_l1_data['searches']:
        searches.append(i)

    for i in campers:
        for j in searches:
            if (i['latitude'] >= boundingBox(j['longitude'], j['latitude'], 0.1)[1] and i['latitude'] <=
                boundingBox(j['longitude'], j['latitude'], 0.1)[3]) and (
                    i['longitude'] >= boundingBox(j['longitude'], j['latitude'], 0.1)[0] and i['longitude'] <=
                    boundingBox(j['longitude'], j['latitude'], 0.1)[2]):
                resultBox.append((j['id'], i['id']))
    for i in campers_l1_data['campers']:
        campers.append(i)

    for i in searches_l1_data['searches']:
        searches.append(i)

    result = {}
    results = []
    search_results = []
    search_el = {}
    camper = {}
    for i in range(1, 4):

        for j in resultBox:
            search_el['search_id'] = i
            if j[0] == i:
                camper['camper_id'] = j[1]
                if {'camper_id': j[1]} not in search_results:
                    search_results.append(camper)
                camper = {}
        search_el['search_results'] = search_results
        search_results = []
        results.append(search_el)
        search_el = {}

    result["results"] = [results]
    return HttpResponse(json.dumps(result, indent=4), content_type="application/json")


def my_engine_level2(request):
    campers = []
    searches = []
    resultBox = []
    result = {}
    results = []
    search_results = []
    search_el = {}
    camper = {}

    for i in campers_l2_data['campers']:
        campers.append(i)

    for i in searches_l2_data['searches']:
        searches.append(i)

    for i in campers:
        for j in searches:
            if (i['latitude'] >= boundingBox(j['longitude'], j['latitude'], 0.1)[1] and i['latitude'] <=
                boundingBox(j['longitude'], j['latitude'], 0.1)[3]) and (
                    i['longitude'] >= boundingBox(j['longitude'], j['latitude'], 0.1)[0] and i['longitude'] <=
                    boundingBox(j['longitude'], j['latitude'], 0.1)[2]):
                resultBox.append((j['id'], i['id']))
    for i in campers_l2_data['campers']:
        campers.append(i)

    for i in searches_l2_data['searches']:
        searches.append(i)


    for i in range(1, 4):

        for j in resultBox:
            search_el['search_id'] = i
            if j[0] == i:
                camper['camper_id'] = j[1]
                try:
                    start_date = datetime.strptime(str(searches[i-1]["start_date"]), '%Y-%m-%d')
                    end_date = datetime.strptime(str(searches[i-1]["end_date"]), '%Y-%m-%d')
                    nb_jours = (abs(end_date - start_date).days) +1
                except:
                    nb_jours = 1
                print(nb_jours)
                try:
                    discount = campers[j[1]-1]["weekly_discount"]
                except:
                    discount = 0
                if nb_jours > 7:
                    price = campers[j[1]-1]["price_per_day"]*nb_jours*(1- discount)
                else:
                    price = campers[j[1] - 1]["price_per_day"] * nb_jours
                camper['price'] = price
                if {'camper_id': j[1]} not in search_results:
                    search_results.append(camper)
                camper = {}
        search_el['search_results'] = search_results
        search_results = []
        results.append(search_el)
        search_el = {}

    result["results"] = [results]
    return HttpResponse(json.dumps(result, indent=4), content_type="application/json")

def my_engine_level3(request):
    campers = []
    searches = []
    resultBox = []
    result = {}
    results = []
    search_results = []
    search_el = {}
    camper = {}

    for i in campers_l3_data['campers']:
        campers.append(i)

    for i in searches_l3_data['searches']:
        searches.append(i)

    for i in campers:
        for j in searches:
            if (i['latitude'] >= boundingBox(j['longitude'], j['latitude'], 0.1)[1] and i['latitude'] <=
                boundingBox(j['longitude'], j['latitude'], 0.1)[3]) and (
                    i['longitude'] >= boundingBox(j['longitude'], j['latitude'], 0.1)[0] and i['longitude'] <=
                    boundingBox(j['longitude'], j['latitude'], 0.1)[2]):
                resultBox.append((j['id'], i['id']))
    for i in campers_l3_data['campers']:
        campers.append(i)

    for i in searches_l3_data['searches']:
        searches.append(i)


    for i in range(1, 4):

        for j in resultBox:
            search_el['search_id'] = i
            if j[0] == i:
                camper['camper_id'] = j[1]
                try:
                    start_date = datetime.strptime(str(searches[i-1]["start_date"]), '%Y-%m-%d')
                    end_date = datetime.strptime(str(searches[i-1]["end_date"]), '%Y-%m-%d')
                    nb_jours = (abs(end_date - start_date).days) +1
                except:
                    nb_jours = 1
                print(nb_jours)
                try:
                    discount = campers[j[1]-1]["weekly_discount"]
                except:
                    discount = 0
                if nb_jours > 7:
                    price = campers[j[1]-1]["price_per_day"]*nb_jours*(1- discount)
                else:
                    price = campers[j[1] - 1]["price_per_day"] * nb_jours
                camper['price'] = price
                if {'camper_id': j[1]} not in search_results:
                    search_results.append(camper)
                camper = {}
        search_el['search_results'] = search_results
        search_results = []
        results.append(search_el)
        search_el = {}

    result["results"] = [results]
    return HttpResponse(json.dumps(result, indent=4), content_type="application/json")