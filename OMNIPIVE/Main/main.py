import os
import threading

from neuralintents import BasicAssistant

from OMNIPIVE.Functions.input_output_functions import say, take_command, ask_language, wishme, ih
from OMNIPIVE.Functions.Open_Websites import Websites
from OMNIPIVE.Functions.Open_Close_Apps import Apps
from OMNIPIVE.Functions.basic_functions import Basic_functions
from OMNIPIVE.LLM import ChatGPT
from OMNIPIVE.Functions.Personalized import Personalized
from OMNIPIVE.Functions.ImageGeneration import generate_image

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
    "change_preferences": p.change_preferences,
    "images": generate_image
}

assistant = BasicAssistant(intents_data='intents.json', method_mappings=mappings)
if os.path.exists('basic_model.keras'):
    assistant.load_model()
else:
    assistant.fit_model()
    assistant.save_model()

# wishme()
# ask_language()
# p.check_for_user()
alarm_thread = threading.Thread(target=ih.face)
alarm_thread.start()

while True:
    say('Waiting for your commands sir!')
    query = take_command()
    result = assistant.process_input(query, query)
    if result is not None:
        say(result)
