import keyboard
import time

import pyautogui as pyg

from OMNIPIVE.Functions.input_output_functions import say, take_command


def manage():

    say('Tell me sir which game would you like to play?')
    query = take_command()
    if 'pong' in query.lower() or 'second' in query.lower():
        say('Launching Ping Pong game for you sir..')
        pyg.press('up')
        time.sleep(2)
        keyboard.press('enter')
        pong()
    elif 'tic' in query.lower() or 'x' in query.lower() or 'first' in query.lower():
        say('Launching tic tac toe game for you sir..')
        keyboard.press('enter')
        ttt()


def pong():
    say('which mode would you like to play sir?')
    query = take_command()
    flag = False
    if not query:
        pass

    if 'single' in query.lower() or 'one player' in query.lower():
        pyg.moveTo(x=919, y=420)
        pyg.click()
        flag = True
    elif 'two player' in query.lower():
        pyg.moveTo(x=920, y=552)
        pyg.click()
        flag = True
    elif 'quit' in query.lower() or 'exit' in query.lower():
        pyg.moveTo(x=934, y=737)
        time.sleep(1)
        pyg.click()
    else:
        pass

    if flag:
        while True:
            query = take_command()
            if not query:
                continue

            if 'single' in query.lower() or 'one player' in query.lower():
                pyg.moveTo(x=919, y=420)
                pyg.click()
            elif 'two player' in query.lower():
                pyg.moveTo(x=920, y=552)
                pyg.click()
            if 'pause' in query.lower():
                pyg.moveTo(x=939, y=238)
                time.sleep(1)
                pyg.click()
            elif 'resume' in query.lower():
                pyg.moveTo(x=928, y=679)
                time.sleep(1)
                pyg.click()
            elif 'restart' in query.lower():
                pyg.moveTo(x=945, y=575)
                time.sleep(1)
                pyg.click()
            elif 'quit' in query.lower() or 'exit' in query.lower():
                pyg.moveTo(x=934, y=737)
                time.sleep(1)
                pyg.click()
                break
            elif 'menu' in query.lower():
                pyg.moveTo(x=943, y=476)
                time.sleep(1)
                pyg.click()


def ttt():
    pass

