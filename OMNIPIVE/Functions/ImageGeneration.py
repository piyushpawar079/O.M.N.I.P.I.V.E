import requests
import io
import tkinter as tk
from PIL import Image, ImageTk

from OMNIPIVE.Functions.Clap import MainClapExe
from OMNIPIVE.Functions.input_output_functions import say, take_command


def display_image(category, img_size=(600, 400)):
    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=1n7sSMtCh8Hs_MrBOjhQ1SygTDA-BJ550UdX3rwLYZQ"
    data = requests.get(url).json()
    img_data = requests.get(data["urls"]["regular"]).content

    photo = Image.open(io.BytesIO(img_data)).resize(img_size, resample=Image.LANCZOS)
    return photo


# function to create the root window and display the image
def create_window_and_display_image(category, root=None):
    # create the root window if not provided
    if root is None:
        root = tk.Tk()
        root.title("Generated Image")

    # retrieve and display the image
    image = display_image(category)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.pack()

    # start the tkinter event loop
    root.update_idletasks()
    root.update()

    return root


# function to generate the image based on user input from console
def generate_image():
    prev = None
    image_window = None
    while True:
        say('Tell me what category you want the image of, or say "stop" to exit.')
        category = take_command()

        if not category:
            continue

        if 'stop' in category.lower() or 'exit' in category.lower():
            say('Exiting...')
            if image_window:
                image_window.destroy()
            break
        elif 'clap' in category.lower():
            say("Waiting for clap to change the image")
            i = 0
            while i != 2:
                say('waiting..')
                if MainClapExe():
                    say(f'Regenerating image of {prev}.')
                    if image_window:
                        image_window.destroy()
                    image_window = create_window_and_display_image(prev)
                i += 1
        else:
            prev = category
            say(f'Displaying the image of {category}.')
            if image_window:
                image_window.destroy()
            image_window = create_window_and_display_image(category)


if __name__ == '__main__':
    generate_image()

