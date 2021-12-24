from django.http import JsonResponse

def my_api_view(request):
    data = {
        'url': 'https://www.pyscoop.com/',
        'skills': ['Python', 'Django'],
    }
    return JsonResponse(data)