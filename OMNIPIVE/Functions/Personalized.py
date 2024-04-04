import json
from datetime import datetime
import requests

from OMNIPIVE.Functions.input_output_functions import say, take_command


class Personalized:
    api_key = '021d638fcdcaa2ebbdda6b23b56d2286'

    def get_weather_info(self):
        say("tell me sir which location's weather would you like to know")
        query = take_command()
        var = query
        url = f'https://api.openweathermap.org/data/2.5/weather?q={var}&appid={self.api_key}'
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            weather_description = data['weather'][0]['description'].capitalize()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            sunrise = data['sys']['sunrise']
            sunset = data['sys']['sunset']

            sunrise_time = datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')
            sunset_time = datetime.fromtimestamp(sunset).strftime('%H:%M:%S')

            weather_report = f"Current Weather in {data['name']}:\n" \
                             f"- Weather: {weather_description}\n" \
                             f"- Temperature: {temperature}°C\n" \
                             f"- Humidity: {humidity}%,\n" \
                             f"- Wind: {wind_speed} miles per second, " \
                             f"- Sunrise: {sunrise_time}\n" \
                             f"- Sunset: {sunset_time}\n"
            say(f'{weather_report}')
        return "Sorry, unable to fetch weather information for the specified location."

    def get_news(self):
        say('tell me sir on which topic you want the news')
        topic = take_command()
        url = f'https://newsapi.org/v2/top-headlines?category={topic}&apiKey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'ok':
            articles = data['articles']
            if articles:
                news_title = articles[0]['title']
                news_description = articles[0]['description']
                say(f"Sports News: {news_title} - {news_description}")
        say(f"Sorry sir, unable to fetch news about {topic} at the moment.")

    def get_stock_news(self):
        say('tell me sir on which stock you want the information about')
        stock_current_user = take_command()
        url = f'https://newsapi.org/v2/everything?q={stock_current_user}&apiKey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'ok':
            articles = data['articles']
            if articles:
                news_title = articles[0]['title']
                news_description = articles[0]['description']
                say(f"Stock News ({stock_current_user}): {news_title} - {news_description}")
        say(f"Sorry, unable to fetch stock news for {stock_current_user} at the moment.")
