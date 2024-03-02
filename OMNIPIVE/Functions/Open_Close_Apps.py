import os
import time

from OMNIPIVE.Functions.input_output_functions import say


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

    def close_apps(self, query):
        for key, value in self.apps.items():
            if f'close {key}'.lower() in query.lower():
                say(f'Closing {key} sir.')
                os.system(f'taskkill /F /im {key}.exe')
                time.sleep(1)
