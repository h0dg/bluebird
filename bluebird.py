import urllib.request, urllib.parse
import json, datetime

apikey = '549ff861d027aace174c37773f24c989'

# Function to download JSON data from APIs
def apicall(baseurl, params, apikey) :
    params['appid'] = apikey
    url = baseurl + '?' + urllib.parse.urlencode(params)
    handle = urllib.request.urlopen(url)
    data = handle.read().decode()
    try :
        js = json.loads(data)
    except :
        js = None
    return js

# User inputs
location = input('Enter a city and state, separated by a comma (ex: Denver, CO): ')
location = location.strip().split(',')

# Find latitude and longitude of user entered location
geo_url = 'http://api.openweathermap.org/geo/1.0/direct'
geo_params = {
    'q': f'{location}',
    'limit': 1,
}
geo = apicall(geo_url, geo_params, apikey)

# Error checking
if not geo or len(geo) == 0 :
    print('==== Location not found ====')
    quit()

lat = str(geo[0]['lat'])
lon = str(geo[0]['lon'])
city = geo[0]['name']
country = geo[0]['country']
try : 
    state = geo[0]['state']
    condA = True
except :
    condA = False

# Send latitude and longitude to OpenWeather API
weather_url = 'https://api.openweathermap.org/data/3.0/onecall'
weather_params = {
    'lat': lat,
    'lon': lon,
    'units': 'imperial',
   # 'exclude':
}
weather = apicall(weather_url, weather_params, apikey)

# Error checking
if not weather or 'current' not in weather: # checks whether the returned dictionary has a key called 'current'
    print('==== Download error ====')
    print('Please try again .')
    quit()
if not weather['current'] : # checks for empty dict, list, or None
    print('==== Current weather conditions not found ====')
    quit()

# DEBUGGING
# print(json.dumps(weather['current'], indent=4))

# Current weather conditions

#time = int(js['current']['dt'])
#dt_object_utc = datetime.datetime.utcfromtimestamp(time)
#local_time = dt_object_utc.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
#print(local_time)
temp = int(weather['current']['temp'])
realfeel = int(weather['current']['feels_like'])
windspeed = int(weather['current']['wind_speed'])
try : 
    gusts = int(weather['current']['wind_gust'])
    condB = True
except : 
    condB = False
desc = weather['current']['weather'][0]['description']

if condA is True:
    print('\nCurrently in ', city, ', ', state, ', ', country, ':', sep='')
else:
    print('\nCurrently in ', city, ', ', country, ':', sep='')
print(temp, 'degrees F with a real feel of', realfeel, 'degrees F')
if condB is True :
    print('Wind speed is', windspeed, 'MPH with gusts up to', gusts, 'MPH')
else: 
    print('Wind speed is', windspeed, 'MPH')
print('Weather condition:', desc.title())