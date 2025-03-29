import requests
from django.shortcuts import render
from django.http import JsonResponse

def get_holidays(request):
    # Get the 'country' parameter from the query string
    country = request.GET.get('country')
    if not country:
        return render(request, 'error.html', {'error': 'Country parameter is missing'})

    # Construct the API URL using the country parameter
    api_url = f"https://date.nager.at/api/v3/publicholidays/2025/{country}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        holidays = response.json()
    except requests.exceptions.RequestException as e:
        return render(request, 'error.html', {'error': f"Failed to fetch holidays: {str(e)}"})

    return render(request, 'holidays/holidays_list.html', {'holidays': holidays, 'country': country})

def chose_country(request):
    return render(request, 'holidays/chose_country.html')
