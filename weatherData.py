import requests

class WeatherData():
    def getDaily(longitute,latitude):
        url = 'https://api.open-meteo.com/v1/forecast?latitude=' + str(latitude) + '&longitude=' + str(longitude) +'&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,rain_sum,showers_sum,snowfall_sum,precipitation_hours&windspeed_unit=mph&timezone=Europe%2FLondon'
        data = requests.get(url)
        data = data.json()
        return data['daily']

    def getHourly(longitude,latitude):
        url = 'https://api.open-meteo.com/v1/forecast?latitude='+ str(latitude) +'&longitude=' + str(longitude) + '&hourly=temperature_2m,apparent_temperature,precipitation_probability,rain,showers,snowfall,snow_depth'
        data = requests.get(url)
        data = data.json()
        return data['hourly']


# for i in range(len(data['time'])):
#         temp_list = []
#         for header in data:
#             temp_list.append(data[header][i])
#         forecast.append(temp_list)