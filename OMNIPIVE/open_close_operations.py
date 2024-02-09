import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyautogui as pyg
from OMNIPIVE.basic_functions import take_command, say
from searching import Search


class Websites:
    sites = {
        'youtube': 'https://youtube.com',
        'google': 'https://google.com',
        'chat gpt': 'https://chat.openai.com',
        'wikipedia': 'https://wikipedia.com'
    }
    PATH = r"C:\Users\bhush\OneDrive\Desktop\PAVAN\VS_Code\python\SELENIUM!!\chromedriver.exe"

    def open_website(self, query):
        for key, value in self.sites.items():
            if f'open {key}'.lower() in query.lower():
                say(f"Opening {key} sir.")
                # wb.open(f'{value}')
                service = Service(executable_path=self.PATH)

                driver = webdriver.Chrome(service=service)
                driver.maximize_window()
                driver.get(f'{value}')
                time.sleep(1)
                say(f'What you want to search for on {key} sir?')
                query = take_command()

                if key == 'google':
                    pyg.moveTo(x=893, y=470, duration=1)
                elif key == 'youtube':
                    pyg.moveTo(x=962, y=185, duration=1)
                elif key == 'chat gpt':
                    pyg.moveTo(x=917, y=958, duration=1)

                if 'i want to search for' in query.lower() or 'search for' in query.lower():
                    query = query.lower()
                    query = query.replace('i want to search for', '')
                    query = query.replace('search for', '')
                pyg.click()
                pyg.write(query.strip(), 0.1)
                pyg.press('enter')
                pyg.click()
                search = Search()
                search.search(driver)

                if 'nothing' in query.lower():
                    say('Okay sir')
                    pyg.hotkey('ctrl', 'w')
                elif 'exit' in query.lower():
                    say(f'closing {key} sir')
                    pyg.hotkey('ctrl', 'w')

                return 1
        return 0


class Apps:
    apps = {
        'vs code': 'C:\\Users\\bhush\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe',
        'notepad': 'C:\\windows\\system32\\notepad.exe',
        'command prompt': 'start cmd',
        'camera': ''
    }

    def open_apps(self, query):
        for key, value in self.apps.items():
            if f'open {key}'.lower() in query.lower():
                say(f'Opening {key} sir.')
                if f'{key}' == 'command prompt':
                    os.system('start cmd')
                else:
                    os.startfile(value)
                time.sleep(1)
                return 1
        return 0

    def take_notes(self):
        self.open_apps('open notepad')
        print('Opening notepad')
        pyg.moveTo(x=929, y=525)
        pyg.click()
        pyg.hotkey('windows', 'Up Arrow')
        pyg.click()
        while True:
            say('What should i note sir?')
            query = take_command()
            if 'note that' in query.lower()[:10] or 'note' in query.lower()[:4]:
                query = query.replace('note that', '')
                query = query.replace('Note that', '')
                query = query.replace('note', '')
                query = query.replace('Note', '')
                query = query.strip()
            elif 'nothing' in query.lower():
                say('Okay sir.')
                self.close_apps('close notepad')
                break
            pyg.write(query, 0.2)

            say('Do you want to note anything else sir?')
            print('Yes/No')
            query = take_command()
            if 'no' in query.lower():
                say('Okay sir.')
                self.close_apps('close notepad')
                break
            pyg.write('\n')

    def close_apps(self, query):
        for key, value in self.apps.items():
            if f'close {key}'.lower() in query.lower():
                say(f'Closing {key} sir.')
                os.system(f'taskkill /F /im {key}.exe')
                time.sleep(1)
                return 1
        return 0
