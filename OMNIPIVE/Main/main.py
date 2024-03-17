import os

from OMNIPIVE.Functions.input_output_functions import say, take_command, ask_language, wishme
from OMNIPIVE.Functions.Open_Websites import Websites
from OMNIPIVE.Functions.Open_Close_Apps import Apps
from OMNIPIVE.Functions.basic_functions import Basic_functions
from neuralintents import BasicAssistant
from OMNIPIVE.LLM import ChatGPT
from OMNIPIVE.Functions.Personalized import Personalized

w = Websites()
app = Apps()
b = Basic_functions()
p = Personalized()
mappings = {
    "open websites": w.open_website,
    "open apps": app.open_apps,
    "functions": b.function,
    "change language": ask_language,
    "introduction": b.introduce,
    "ip address": b.ip_address,
    "take notes": b.take_notes,
    "tell jokes": b.tell_jokes,
    "set alarm": b.set_alarm,
    "take screenshot": b.take_screenshot,
    "wait": b.wait,
    "battery": b.battery,
    "chatgpt": ChatGPT.ChatGpt,
    "exit": b.exit,
    "games": b.Game,
    "mail": b.mail,
    "weather": p.get_weather_info,
    "news": p.get_news,
    "stock": p.get_news,
    "change_preferences": p.change_preferences
}

assistant = BasicAssistant(intents_data='intents.json', method_mappings=mappings)
if os.path.exists('basic_model.keras'):
    assistant.load_model()
else:
    assistant.fit_model()
    assistant.save_model()

# wishme()
# ask_language()
p.check_for_user()

while True:
    say('Waiting for your commands sir!')
    query = take_command()
    result = assistant.process_input(query, query)
    if result is not None:
        say(result)
