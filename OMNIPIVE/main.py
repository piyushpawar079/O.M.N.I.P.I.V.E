import time
import pyjokes
import pyautogui as pyg
from requests import get
from OMNIPIVE.basic_functions import take_command, wishme, say, ask_language
from open_close_operations import Websites, Apps
from searching import Search
from LLM import ChatGPT
import psutil

if __name__ == '__main__':

    # print("In order to start me, you have to say 'Wake up'")
    # while True:
    #     query = take_command()
    #
    #     if 'wake up' in query.lower():
    #         break

    wishme()
    lang = ask_language()
    ws = Websites()
    apps = Apps()
    search = Search()

    while True:
        say("Waiting for your command Sir..")
        query = take_command()

        if 'position of mouse' in query.lower():
            print(pyg.position())
            continue

        if ws.open_website(query):
            continue

        elif apps.open_apps(query) or apps.close_apps(query):
            continue

        elif search.web_search(query):
            continue

        system_commands = {
            'shutdown': 'shutdown /s /t 5',
            'restart': 'shutdown /r /t 5',
            'sleep': 'rund1132.exe powrprof.d11,SetSuspendState 0,1,0'
        }

        if 'shutdown'.lower() in query.lower() or 'exit' in query.lower():
            say("Shutting down, Thank you sir.")
            exit()

        elif 'change window' in query.lower():
            pyg.hotkey('alt', 'tab')

        elif 'introduce yourself' in query.lower():
            say("Hello sir, I am omnipive (a virtual assistant) created by Piyush Pawar. I am here to help you sir.")

        elif 'ip address' in query.lower():
            ip = get("https://api.ipify.org").text
            print(f'Your IP address is {ip}, sir')
            say(f'Your IP address is {ip}, sir')

        elif 'take notes' in query.lower():
            apps.take_notes()

        elif 'tell me' in query.lower() and 'joke' in query.lower():
            joke = pyjokes.get_joke()
            say(joke)

        # elif 'set an alarm' in query.lower():
        #     say('At what time i should set an alarm sir?')
        #     query = take_command()
        #     input_time = query

        elif 'take screenshot' in query.lower():
            say('sir, please tell me what name should i give to tha screenshot')
            name = take_command()
            say('okay sir wait for few minutes.')
            img = pyg.screenshot()
            img.save(f'{name}.png')
            say('Done sir!')

        elif 'battery percentage' in query.lower() or 'battery' in query.lower():
            battery = psutil.sensors_battery()
            percentage = battery.percent
            say(f'sir our system has {percentage} percent battery.')

        elif 'change' in query.lower() and 'language' in query.lower():
            lang = ask_language()

        # elif 'open camera' in query.lower():
        #     cap = cv2.VideoCapture(0)
        #     while True:
        #         ret, frame = cap.read()
        #         cv2.imshow('camera', frame)
        #         say('to close the camera please say close camera')
        #         query = take_command()
        #         if 'close camera' in query.lower():
        #             break
        #     cap.release()
        #     cv2.destroyAllWindows()

        else:
            result = ChatGPT.ChatGpt(query)
            say(result)

        time.sleep(0.5)





