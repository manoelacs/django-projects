import requests
from django.shortcuts import render
from django.http import JsonResponse
import datetime

def get_holidays(request):
    # Get the 'country' parameter from the query string
    country = request.GET.get('country')
    if not country:
        return render(request, 'error.html', {'error': 'Country parameter is missing'})

    # Construct the API URL using the country parameter
    api_url = f"https://date.nager.at/api/v3/publicholidays/{datetime.date.today().year}/{country}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        holidays = response.json()

        # Sort holidays by date
        holidays = sorted(holidays, key=lambda x: datetime.datetime.strptime(x['date'], '%Y-%m-%d'))

        # Separate past and upcoming holidays
        today = datetime.date.today()
        upcoming_holidays = [h for h in holidays if datetime.datetime.strptime(h['date'], '%Y-%m-%d').date() >= today]
        past_holidays = [h for h in holidays if datetime.datetime.strptime(h['date'], '%Y-%m-%d').date() < today]
    except requests.exceptions.RequestException as e:
        return render(request, 'error.html', {'error': f"Failed to fetch holidays: {str(e)}"})

    return render(request, 'holidays/holidays_list.html', {
        'upcoming_holidays': upcoming_holidays,
        'past_holidays': past_holidays,
        'country': country,
        'current_year': datetime.date.today().year,
    })
def chose_country(request):
    return render(request, 'holidays/chose_country.html')

def index(request):
    return render(request, 'index.html')
