import datetime
import os
import sys
import threading
from datetime import datetime

import psutil
import pyautogui as pyg
import pyjokes
from requests import get

from OMNIPIVE.Functions.Alarm_Reminder import Alarm
from OMNIPIVE.Functions.Manage_Game import manage
from OMNIPIVE.Functions.input_output_functions import say, take_command
from OMNIPIVE.Games.Main_Game import main


class Basic_functions:

    alarm = Alarm()

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

    def set_alarm(self, q):
        flag1 = False

        if 'remind' in q.lower():
            flag1 = True

        flag = False
        m = ['minutes', 'seconds', 'minute', 'second']
        for i in m:
            if i in q.lower():
                query = q
                flag = True
        if not flag:
            if 'p.m.' not in q.lower() and 'a.m.' not in q.lower():
                say("Please specify the time too sir?")
                query = take_command()
            else:
                query = q

            if len(query) < 15 and ':' not in query:
                if 'p' in query.lower():
                    time = query.split('p')[0].strip()
                    extra = 'p.m.'
                elif 'a' in query.lower():
                    time = query.split('a')[0].strip()
                    extra = 'a.m.'
                else:
                    time = query.strip()
                    extra = ''

                if len(time) == 3:
                    hour = '0' + time[0]
                    minute = time[1:]
                else:
                    hour = time[:2]
                    minute = time[2:]

                query = hour + ':' + minute + ' ' + extra
        self.alarm.initialize(query)
        alarm_thread = threading.Thread(target=self.alarm.check_and_alarm)
        alarm_thread.start()

        if flag1:
            say('Okay sir, I will remind you.')
        else:
            say('Done setting the alarm sir.')

    def Game(self):
        game_thread = threading.Thread(target=manage)
        game_thread.start()
        main()

    def take_screenshot(self):
        say('Do you want to give a name to the screenshot?')
        query = take_command()
        print(query)
        ImageName = ''
        if 'no' in query.lower():
            ImageName = 'screenshot-' + str(datetime.now()).replace(':', '-') + '.png'
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
        say('i can do anything for you sir')

    def exit(self):
        self.alarm.run = False
        say("Bye sir")
        sys.exit()
