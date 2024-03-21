import datetime
import os
import sys
import threading
from datetime import datetime
from email.message import EmailMessage
import imghdr

import smtplib
import psutil
import pyautogui as pyg
import pygame
import pyjokes
from requests import get

from OMNIPIVE.Functions.Alarm_Reminder import Alarm
from OMNIPIVE.Functions.Manage_Game import manage
from OMNIPIVE.Functions.input_output_functions import say, take_command
from OMNIPIVE.GUI.main_gui import imageHandler
from OMNIPIVE.Games.Main_Game import main


class Basic_functions:

    alarm = Alarm()
    ih = imageHandler()

    def take_notes(self):
        say('What should i name the text file sir?')
        query = take_command()
        if 'name it as' in query.lower() or 'give the name as' in query.lower() or 'give name as' in query.lower():
            query = query.lower().replace('name it as', '')
            query = query.lower().replace('give the name as', '')
            query = query.lower().replace('give name as', '')
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
        m = None
        if 'remind' in q.lower():
            flag1 = True
            say('do you want me to remind you about anything specific sir?')
            m = take_command()
            if 'no' in m.lower():
                say('okay sir')
            elif 'yes' in m.lower() or 'yes remind me by saying' in m.lower() or 'yes say that' in m.lower():
                m = m.lower().replace('yes', '')
                m = m.lower().replace('yes remind me by saying', '')
                m = m.lower().replace('yes say that', '')
            else:
                say('okay sir tell me what should i say')
                m = take_command()

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
        self.alarm.initialize(query, m)
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

    def mail(self):
        flag = False
        say('will you specify the mail id by speaking or typing sir (if the mail id is complicated please consider typing the mail id sir')
        query = take_command().lower()
        if 'speaking' in query or 'speak' in query:
            say('tell me the gmail id of the person you want to send the mail to (without the @gmail.com)')
            query = take_command().lower()
            l = query.split()
        elif 'typing' in query or 'type' in query:
            query = input('Enter the gmail id of the person (without the @gmail.com)')
            l = query.split()

        recipient = ''
        for i in l:
            recipient += i.lower()
        recipient += '@gmail.com'
        print(recipient)
        sender_email = "miniproject437@gmail.com"
        sender_password = "rjgu hyjo svta clwy"
        say('do you want to set the subject of the mail? (please reply in yes or no)')
        query = take_command()
        if 'no' in query.lower():
            say('okay sir')
            subject = ''
        else:
            say('Okay sir, tell me the what should i write')
            query = take_command()
            subject = query

        say("tell me the body content of the mail sir")
        body = ''
        while True:
            query = take_command()
            d = ["i don't want to", "nothing", "no", "don't set", "don't"]
            if query.lower() in d:
                say("you need to set the body content of the mail sir we can't keep it empty so tell me what should i set to")
                query = take_command()
            else:
                for i in d:
                    if i == query.lower():
                        say("you need to set the body content of the mail sir we can't keep it empty so tell me what should i set to")
                        query = take_command()
                        break
            body += query
            say('Do you want to add anything else sir?')
            query = take_command()
            if 'no' in query.lower():
                say('okay sir')
                break
            say('Tell me sir what should i add')

        say('do you want to attach anything to the mail sir?')
        query = take_command()

        if 'no' in query.lower():
            say('okay sir sending the mail')
        else:
            d = os.getcwd()
            if d != r'C:\Users\bhush\PycharmProjects\PAVAN\OMNIPIVE\Documents':
                os.chdir(r'C:\Users\bhush\PycharmProjects\PAVAN\OMNIPIVE\Documents')
            flag = True
            say('tell me sir which document should i attach?')
            query = take_command()
            photos = ['groupphoto']
            pdfs = ['machinelearning']
            name = ''

            for i in query.split():
                name += i
            if photos[0] in name:
                main_type = 'image'
                name = 'groupphoto.jpeg'
                with open(name, 'rb') as f:
                    file_data = f.read()
                    sub_type = imghdr.what(f.name)
                    file_name = f.name
            elif pdfs[0] in name:
                name = 'machinelearning.pdf'
                main_type = 'application'
                sub_type = 'octet-stream'
                with open(name, 'rb') as f:
                    file_data = f.read()
                    file_name = f.name
            else:
                say('can you please specify the path of the document that you want to attach sir?')
                q = input('Enter the path here: ')
                d = os.getcwd()
                if d != q:
                    os.chdir(q)
                l = q.split('\\')[-1]
                if '.jpeg' in q or '.jpg' in q:
                    main_type = 'image'
                    name = l
                    with open(name, 'rb') as f:
                        file_data = f.read()
                        sub_type = imghdr.what(f.name)
                        file_name = f.name
                elif '.pdf' in q:
                    name = l
                    main_type = 'application'
                    sub_type = 'octet-stream'
                    with open(name, 'rb') as f:
                        file_data = f.read()
                        file_name = f.name

            say('okay sir sending the mail')

        em = EmailMessage()

        em['From'] = sender_email
        em['To'] = recipient
        em['Subject'] = subject
        em.set_content(body)

        if flag:
            em.add_attachment(file_data, maintype=main_type, subtype=sub_type, filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as f:
            f.login(sender_email, sender_password)
            f.send_message(em)
            say('Done sending the email sir.')

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
            if 'wake up' == query.lower():
                break
        say('Hello sir I am up and ready to receive commands')

    def battery(self):
        battery = psutil.sensors_battery()
        percentage = battery.percent
        say(f'sir our system has {percentage} percent battery.')

    def function(self):
        say('i can do everything like opening google, youtube and sending mails, setting reminders and alarms taking '
            'screenshot and notes and many more things sir.')

    def exit(self):
        self.alarm.run = False
        say("Bye sir")
        self.ih.Exit()
        sys.exit()
