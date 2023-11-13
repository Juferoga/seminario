from django.shortcuts import render
import requests

def HomePage (request):
    return render(request, "home.html")


def IntegrationTest(request):
    url = "http://localhost:3000/api/resources/all-resources"
    url_self = "http://localhost:8000/api/resource/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    
    try:
        response = requests.get(url_self)
        response.raise_for_status()
        rdata = response.json()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)

    return render(request, 'integration_test.html', {'data': data, 'rdata': rdata})

