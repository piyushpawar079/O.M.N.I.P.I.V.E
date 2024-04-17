import g4f

from OMNIPIVE.Functions.input_output_functions import say

messages = [
    {"role": "system", "content": "I'm the latest J.A.R.V.I.S. AI, designed by Piyush Pawar with capabilities to access systems through various programming languages "
                                  "using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."}
            ]


def ChatGpt(text):

    global messages
    text += ' Give me to the point answer and in 2 to 3 sentences only.'
    messages.append({
        'role': 'user',
        'content': text
    })

    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True,
    )

    m = ''
    try:
        for message in response:
            m += message
    except RuntimeError as e:
        if "async generator ignored GeneratorExit" in str(e):
            pass  # Ignore the exception
        else:
            raise  # Re-raise other RuntimeErrors
    print(m)
    messages.append(
        {
            'role': 'assistant',
            'content': m
        }
    )
    say(m)
