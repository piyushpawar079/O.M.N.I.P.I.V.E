import json
from datetime import datetime
import requests

from OMNIPIVE.Functions.input_output_functions import say, take_command


class Personalized:

    user_profiles = '''{
        "piyush": {
            "news" : "sports",
            "music" : "m1",
            "location" : "Thane",
            "stock" : "Tata Steels"
        },
        "nikhil": {
            "news" : "",
            "music" : "",
            "location" : "Lower Parel",
            "stock" : ""
        }
    }'''

    user_data = json.loads(user_profiles)
    current_user = ''
    api_key = '021d638fcdcaa2ebbdda6b23b56d2286'

    def check_for_user(self):
        say('please tell me your name sir, so that I can recognize you.')
        self.current_user = take_command().lower()
        if 'my name is' in self.current_user.lower() or 'name is' in self.current_user.lower():
            self.current_user = self.current_user.lower().replace('my name is', '').strip()
            self.current_user = self.current_user.lower().replace('name is', '').strip()

        if self.current_user.lower() in self.user_data.keys():
            say('okay sir I recognize you now.')
        else:
            say('sorry sir but i think your a new user, please give me some basic information so that I can give you '
                'a better response')
            self.add_user()

    def add_user(self):
        say('what type of news would you like to hear about?')
        query = take_command()
        news = query
        say('okay sir, what kind of music would you love to hear?')
        query = take_command()
        music = query
        say('okay, where do you live?')
        query = take_command()
        location = query
        say('which stock do you like sir?')
        query = take_command()
        stock = query
        say(f'thankyou {self.current_user} sir, for giving me some information now i can give you much better response')

        self.user_data[f'{self.current_user}'] = {
            "news": f'{news}',
            "music": f'{music}',
            "location": f'{location}',
            "stock": f'{stock}'
        }

        print(f'{self.user_data[self.current_user]}')

    def get_weather_info(self):
        say('would you like to know weather of new location or your preferred location')
        query = take_command()
        if 'preferred' in query.lower():
            say(f'okay sir telling you the weather updates of your preferred location that is {self.user_data[self.current_user]["location"]}')
            var = self.user_data[self.current_user]['location']
        else:
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
        topic = self.user_data[self.current_user]['news']
        url = f'https://newsapi.org/v2/top-headlines?category={topic}&apiKey={self.api_key}'
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'ok':
            articles = data['articles']
            if articles:
                news_title = articles[0]['title']
                news_description = articles[0]['description']
                say(f"Sports News: {news_title} - {news_description}")
        say(f"Sorry sir, unable to fetch news about your favorite topic that is {self.user_data[self.current_user]['news']} at the moment.")

    def get_stock_news(self):
        stock_current_user = self.user_data[self.current_user]['stock']
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

    def change_preferences(self):
        say('what would you like to change sir? (favorite news topic, your location, favorite stock, favorite music)')
        query = take_command()
        while True:
            if 'news' in query.lower():
                say('okay sir, tell me which is your new favorite news topic?')
                query = take_command()
                self.user_data[self.current_user]['news'] = query
            elif 'location' in query.lower():
                say('okay sir, tell me which is your new favorite location?')
                query = take_command()
                self.user_data[self.current_user]['location'] = query
            elif 'stock' in query.lower():
                say('okay sir, tell me which is your new favorite stock?')
                query = take_command()
                self.user_data[self.current_user]['stock'] = query
            elif 'music' in query.lower():
                say('okay sir, tell me which is your new favorite music?')
                query = take_command()
                self.user_data[self.current_user]['music'] = query
            say('would you like to change any other preferences too sir?')
            query = take_command()
            if 'no' in query.lower():
                break
            say('what should i change sir?')
            query = take_command()
        say('okay sir your preferences are changed now.')
