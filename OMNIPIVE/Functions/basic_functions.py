import psutil

from OMNIPIVE.Functions.input_output_functions import say, take_command
from requests import get
import pyjokes
import datetime
import pyautogui as pyg
import  os


class Basic_functions:

    def take_notes(self):
        say('What should i name the text file sir?')
        query = take_command()
        file_name = query + '-notes.txt'
        d = os.getcwd()
        if not os.path.exists(r'\Notes'):
            os.mkdir(r'\Notes')
        if d != r'C:\Users\bhush\PycharmProjects\PAVAN\OMNIPIVE\Notes':
            os.chdir(r'C:\Users\bhush\PycharmProjects\PAVAN\OMNIPIVE\Notes')

        with open(file_name, 'w+') as f:
            while True:
                say('Tell me what should i note sir?')
                query = take_command()
                if 'note that' in query.lower() or 'note' in query.lower()[:4]:
                    query = query.replace('note that', '')
                    query = query.replace('Note that', '')
                    query = query.replace('note', '')
                    query = query.replace('Note', '')
                    query = query.strip()
                f.write(query + '\n')
                say('Do you want to note anything else sir?')
                query = take_command()
                if 'no' in query.lower():
                    break
        say('Note has been saved sir.')

    def introduce(self):
        say("hello sir, my self OMNIPIVE your personal virtual assistant. I am here to help you sir.")

    def ip_address(self):
        ip = get("https://api.ipify.org").text
        print(f'Your IP address is {ip}, sir')
        say(f'Your IP address is {ip}, sir')

    def tell_jokes(self):
        joke = pyjokes.get_joke()
        say(joke)

    def set_alarm(self):
        say('At what time i should set an alarm sir?')
        query = take_command()
        print(query)

    def take_screenshot(self):
        say('Do you want to give a name to the screenshot?')
        query = take_command()
        print(query)
        ImageName = ''
        if 'no' in query.lower():
            ImageName = 'screenshot-' + str(datetime.datetime.now()).replace(':', '-') + '.png'
        else:
            say('Okay, tell me what should I name it?')
            query = take_command()
            if 'name it as' in query.lower() or 'give the name as' in query.lower() or 'give name as' in query.lower():
                query = query.lower().replace('name it as', '')
                query = query.lower().replace('give the name as', '')
                query = query.lower().replace('give name as', '')
            l = query.split(' ')
            for i in l:
                ImageName += i
            ImageName += '.png'
        img_captured = pyg.screenshot()
        a = os.getcwd()
        print(a)
        if a != r'C:\Users\bhush\PycharmProjects\PAVAN\OMNIPIVE\ScreenShots':
            os.chdir(r'C:\Users\bhush\PycharmProjects\PAVAN\OMNIPIVE\ScreenShots')

        img_captured.save(ImageName)    
        say('The screenshot has been saved sir.')

    def wait(self):
        say('Okay sir. You can call me anytime by saying \'Wake Up\'')
        while True:
            query = take_command()
            if not query:
                continue
            if 'wake up' in query.lower():
                break
        say('Hello sir I am up and ready to receive commands')

    def battery(self):
        battery = psutil.sensors_battery()
        percentage = battery.percent
        say(f'sir our system has {percentage} percent battery.')

    def function(self):
        say('i can do anything for sir')

    def exit(self):
        say("Bye sir")
        exit()
