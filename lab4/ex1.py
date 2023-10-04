import tkinter as tk
import random
import pygame
from PIL import Image, ImageTk

def generate_key():
    def generate_block():
        letters = random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 3)
        digits = random.sample('0123456789', 2)
        block = letters + digits
        random.shuffle(block)
        return ''.join(block)

    key = f"{generate_block()}-{generate_block()}-{generate_block()}"
    return key

def on_generate_click():
    generated_key = generate_key()
    key_entry.config(state="normal")
    key_entry.delete(0, tk.END)
    key_entry.insert(0, generated_key)
    key_entry.config(state="readonly")

def animate_image(label, dx, dy):
    x, y = label.winfo_x(), label.winfo_y()
    if y < 350:
        label.place(x=x + dx, y=y + dy)
    else:
        label.place(x=x + dx, y=0)
    root.after(20, animate_image, label, dx, dy)

root = tk.Tk()
root.title("Key Generator")
root.geometry("700x400")
root.wm_attributes('-alpha', 1)

bg_image = tk.PhotoImage(file="bg.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

key_entry = tk.Entry(root, state="readonly", bg='#333333', fg='black', font=("Verdana", 14), insertbackground='white', justify="center", width=20)
key_entry.place(x=235, y=250)

generate_button = tk.Button(root, text="Сгенерировать ключ", command=on_generate_click, font=("Verdana", 14), bg='#555555', fg='white')
generate_button.place(x=245, y=300)

pygame.init()

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)

image = Image.open("bg.png")
image = image.resize((50, 50), Image.ANTIALIAS if hasattr(Image, 'ANTIALIAS') else Image.NEAREST)
image = ImageTk.PhotoImage(image)

logo = Image.open("logo.png")
logo = logo.resize((50, 50), Image.ANTIALIAS if hasattr(logo, 'ANTIALIAS') else Image.NEAREST)
logo = ImageTk.PhotoImage(logo)

image2 = Image.open("2.png")
image2 = ImageTk.PhotoImage(image2)

transparent_canvas = tk.Canvas(root, width=50, height=400, highlightthickness=0)

image_id = transparent_canvas.create_image(0, 0, anchor=tk.NW, image=image2)
transparent_canvas.place(x=650, y=0)

image_label = tk.Label(transparent_canvas, image=logo, borderwidth=0)
image_label.place(x=0, y=50)

animate_image(image_label, 0, 2)

root.mainloop()
