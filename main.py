import requests, json

api_key = "TJGC208iOajQelnECtvoU7hD5sJAxWRw"
region_code_asia = "ASI"
region_code_srilanka = "LK"

url_to_get_country = "http://dataservice.accuweather.com/locations/v1/countries/" + region_code_asia + "?apikey=" + api_key
url_to_get_region = "http://dataservice.accuweather.com/locations/v1/regions?"+ "apikey=" + api_key
url_to_get_cities = "http://dataservice.accuweather.com/locations/v1/topcities/150?"+ "apikey=" + api_key
url_to_get_geo_position = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search?"+ "apikey=" + api_key
url_to_get_120hours_of_hourly_forecasts = "http://dataservice.accuweather.com/forecasts/v1/hourly/120hour/311399"+ "apikey=" + api_key

print(url_to_get_region)
get_regions_req = requests.request("get", url_to_get_region)

print(url_to_get_region)
get_countries_req = requests.request("get", url_to_get_country)

print(url_to_get_cities)
get_cities_req = requests.request("get", url_to_get_cities)

# with open('region_data.json', 'w') as outfile:
#     json.dump(get_regions_req.json(), outfile)
#
# with open('country_data.json', 'w') as outfile:
#     json.dump(get_countries_req.json(), outfile)

# with open('city_data.json', 'w') as outfile:
#     json.dump(get_cities_req.json(), outfile)

with open('120hours_of_hourly_forecasts.json', 'w') as outfile:
    json.dump(get_cities_req.json(), outfile)


# requests.request(get, url_to_get_country,)


# Forecast data can be obtained by this.Historical data upto 5 days is available. This is not free as well. limited requests