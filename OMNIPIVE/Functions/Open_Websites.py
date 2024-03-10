import time

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui as pyg
from word2number import w2n

from OMNIPIVE.Functions.Checking_For_More_Functions import Check
from OMNIPIVE.Functions.input_output_functions import take_command, say


class Websites:
    sites = {
        'youtube': 'https://youtube.com',
        'google': 'https://google.com',
        'chat gpt': 'https://chat.openai.com',
        'gemini': 'https://gemini.google.com'
    }
    nums = {
        'first': 0,
        'second': 1,
        'third': 2,
        'fourth': 3,
        'fifth': 4,
        'sixth': 5
    }
    PATH = r"C:\Users\bhush\OneDrive\Desktop\PAVAN\VS_Code\python\SELENIUM!!\chromedriver.exe"
    c = Check()

    def open_website(self, query):
        b = 0
        for key, value in self.sites.items():
            if f'open {key}'.lower() in query.lower():
                say(f"Opening {key} sir.")
                service = Service(executable_path=self.PATH)

                driver = webdriver.Chrome(service=service)
                driver.maximize_window()
                driver.get(f'{value}')
                while True:
                    search = None
                    say('Do you want to search for anything sir (please reply in Yes or No)')
                    query = take_command()
                    if 'no' in query.lower():
                        say('Okay sir, then tell me what should i do?')
                        while True:
                            query = take_command()

                            if 'close' in query.lower() or 'exit' in query.lower():
                                say(f'Okay sir, closing {key}')
                                break

                            elif 'open' in query.lower() and 'video' in query.lower():
                                for key, value in self.nums.items():
                                    if f'open the {key} video' in query.lower():
                                        elements = driver.find_elements(By.CSS_SELECTOR, "#contents ytd-video-renderer")
                                        element = elements[int(f'{value}')]
                                        element.click()
                                        b += 1

                            elif 'scroll down' in query.lower():
                                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

                            elif 'scroll up' in query.lower():
                                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)

                            self.c.in_Basic_functions(query)
                            say("What should i do next sir?")
                    else:
                        say('What should I search for,sir?')
                        b += 1
                        query = take_command()
                        if f'{key}' == 'google':
                            search = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.TAG_NAME, 'textarea')))
                        elif f'{key}' == 'youtube':
                            search = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.TAG_NAME, 'input')))
                        elif f'{key}' == 'chat gpt':
                            search = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "prompt-textarea")))
                        elif f'{key}' == 'gemini':
                            search = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.TAG_NAME, "rich-textarea")))

                        if 'for' in query.lower():
                            s = query.split('for')[1].strip().title()
                        s = query.title()
                        print(s)
                        search.clear()
                        search.send_keys(s)
                        search.send_keys(Keys.ENTER)
                        while b != 0:
                            say('What should I do next sir?')
                            query = take_command()

                            if 'open' in query.lower() and 'link' in query.lower():
                                for key, value in self.nums.items():
                                    if f'open the {key} link' in query.lower():
                                        h3_elements = driver.find_elements(By.CLASS_NAME, "LC20lb")
                                        h3_element = h3_elements[int(f'{value}')]
                                        if h3_element.text != '':
                                            h3_element.click()
                                            b += 1
                                            continue

                            elif 'open' in query.lower() and 'video' in query.lower():
                                for key, value in self.nums.items():
                                    if f'open the {key} video' in query.lower():
                                        elements = driver.find_elements(By.CSS_SELECTOR, "#contents ytd-video-renderer")
                                        element = elements[int(f'{value}')]
                                        element.click()
                                        b += 1
                                        continue

                            if 'pause' in query.lower() and 'video' in query.lower():
                                driver.execute_script("document.querySelector('video').pause();")

                            elif 'resume' in query.lower() and 'video' in query.lower():
                                driver.execute_script("document.querySelector('video').play();")

                            elif 'increase' in query.lower() and 'volume' in query.lower():
                                pyg.press('volumeup')

                            elif 'decrease' in query.lower() and 'volume' in query.lower():
                                pyg.press('volumedown')

                            elif 'mute' in query.lower():
                                pyg.press('volumemute')

                            elif 'scroll down' in query.lower():
                                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

                            elif 'scroll up' in query.lower():
                                driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_UP)

                            elif 'full screen' in query.lower():
                                pyg.press('f')

                            elif 'go back' in query.lower():
                                driver.back()
                                b -= 1

                            elif 'go forward' in query.lower():
                                driver.forward()
                                b += 1

                            if 'change tab' in query.lower():
                                say("How many times you want to change the tab sir?")
                                query = take_command()
                                if 'times' in query.lower() and 'types' in query.lower():
                                    query = query.lower()
                                    query = query.replace('times', '')
                                    query = query.replace('types', '')
                                    query = query.strip()
                                    query = w2n.word_to_num(query)
                                elif 'one' in query.lower() or 'single' in query.lower():
                                    query = '1'
                                query = int(query)
                                for _ in range(query):
                                    pyg.hotkey('ctrl', 'tab')
                                    time.sleep(0.3)

                            elif 'change' in query.lower() and 'window' in query.lower():
                                pyg.hotkey('alt', 'tab')

                            elif 'close' in query.lower() and 'tab' in query.lower():
                                pyg.press('ctrl', 'w')
                                break

                            elif 'close' in query.lower() and 'window' in query.lower():
                                pyg.hotkey('ctrl', 'W')
                                break

                            self.c.in_Basic_functions(query)

                            time.sleep(1.5)
