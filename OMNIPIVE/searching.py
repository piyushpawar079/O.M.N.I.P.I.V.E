import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from word2number import w2n
import pyautogui as pyg
import wikipedia as wik
from OMNIPIVE.basic_functions import take_command, say


class Search:

    def search(self, driver):
        flag1 = 0
        flag2 = 0
        while True:
            time.sleep(1)
            say("Waiting for your command's Sir..")
            query = take_command()

            if 'open the' in query.lower() and 'link' in query.lower():
                nums = {
                    'first': 0,
                    'second': 1,
                    'third': 2,
                    'fourth': 3,
                    'fifth': 4,
                    'sixth': 5
                }

                for key, value in nums.items():
                    if f'open the {key} link' in query.lower():
                        h3_elements = driver.find_elements(By.CLASS_NAME, "LC20lb")
                        h3_element = h3_elements[int(f'{value}')]
                        if h3_element.text != '':
                            h3_element.click()
                            flag2 = 1

            elif 'open the' in query.lower() and 'video' in query.lower():
                nums = {
                    'first': 0,
                    'second': 1,
                    'third': 2,
                    'fourth': 3,
                    'fifth': 4,
                    'sixth': 5
                }

                for key, value in nums.items():
                    if f'open the {key} video' in query.lower():
                        elements = driver.find_elements(By.CSS_SELECTOR, "#contents ytd-video-renderer")
                        element = elements[int(f'{value}')]
                        element.click()

            elif 'wait' in query.lower():
                say('You can call me anytime by saying \'WakeUp OMNIPIVE\'')
                while True:
                    query = take_command()
                    if 'WakeUp OMNIPIVE'.lower() in query.lower():
                        break

            elif 'pause the video' in query.lower():
                driver.execute_script("document.querySelector('video').pause();")

            elif 'resume the video' in query.lower():
                driver.execute_script("document.querySelector('video').play();")

            elif 'increase the volume' in query.lower():
                # driver.execute_script("document.querySelector('video').volume += 0.1;")
                pyg.press('volumeup')

            elif 'decrease the volume' in query.lower():
                # driver.execute_script("document.querySelector('video').volume -= 0.1;")
                pyg.press('volumedown')

            elif 'mute' in query.lower():
                pyg.press('volumemute')

            elif 'scroll down' in query.lower():
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

            elif 'scroll up' in query.lower():
                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)

            elif 'screen' in query.lower():
                pyg.press('f')

            elif 'go back' in query.lower():
                if flag2:
                    flag1 = 1
                    driver.back()
                else:
                    say('There is no option to go back sir!')

            elif 'go forward' in query.lower():
                if flag1:
                    driver.forward()
                else:
                    say('There is no option to go forward sir!')

            elif 'change tab' in query.lower():
                time.sleep(0.3)
                say("How many times you want to change the tab sir?")
                query = take_command()
                if 'times' in query.lower() and 'types' in query.lower():
                    query = query.lower()
                    query = query.replace('times', '')
                    query = query.replace('types', '')
                    query = query.strip()
                    query = w2n.word_to_num(query)
                pyg.moveTo(89, 372, 1)
                pyg.click()
                query = int(query)
                for _ in range(query):
                    pyg.hotkey('ctrl', 'tab')
                    time.sleep(0.3)

            elif 'change window' in query.lower():
                pyg.hotkey('alt', 'tab')

            elif 'do nothing' in query.lower():
                say('Okay sir.')
                break

            elif 'exit' in query.lower():
                # pyg.moveTo(89, 372, 1)
                # pyg.click()
                pyg.hotkey('ctrl', 'w')
                break

            else:
                say(query + "Cannot recognize the command.")

    def web_search(self, query):

        # if 'search on google for'.lower() in query.lower():
        #     say("Searching on google sir..")
        #     query = query.lower()
        #     query = query.replace('search on google for', '')
        #     pyw.search(query)
        #     self.search()
        #     return 1
        #
        # elif 'search on youtube for'.lower() in query.lower():
        #     say("Searching on youtube sir..")
        #     query = query.lower()
        #     query = query.replace('search on youtube for', '')
        #     pyw.playonyt(query)
        #     self.search()
        #     return 1

        if 'search on wikipedia for' in query.lower():
            say("Searching on wikipedia sir..")
            query = query.lower()
            query = query.replace('search on wikipedia for', '')
            result = wik.summary(query, sentences=2)
            print(result)
            say(f"According to wikipedia, {result}")
            time.sleep(1)
            return 1
        return 0
