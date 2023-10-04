import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk

# Альтернативное задание, так как не aws.random.cat не отвечал


class DPhoto:
    def __init__(self, root, api_key):
        self.root = root
        self.api_key = api_key
        self.root.title("DayPhoto")

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

        self.load_image()

    def load_image(self):
        url = f'https://api.nasa.gov/planetary/apod?api_key={self.api_key}'
        response = requests.get(url)

        if response.status_code == 200:
            image_url = response.json()['url']
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                image_data = BytesIO(image_response.content)
                pil_image = Image.open(image_data)
                image = ImageTk.PhotoImage(pil_image)

                self.image_label.configure(image=image)
                self.image_label.image = image
            else:
                print(f"Ошибка. Код: {image_response.status_code}")
        else:
            print(f"Ошибка. Код: {response.status_code}")


if __name__ == "__main__":
    api_key = 'Dbktz9tLha912JqeSj0juKMdRSJaOzB8siaAWLeP'
    root = tk.Tk()
    app = DPhoto(root, api_key)
    root.mainloop()
