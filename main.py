import random
import tkinter as tk
from tkinter import Label
from tkinter import filedialog, messagebox, StringVar
from PIL import Image, ImageTk, ImageDraw, ImageFont
import shutil

filepath = " "
img = ""
draw = ""
filepath_2 = ""
img = ""


def image_preview(filepath):
    global img

    #   opening the original image
    img = Image.open(filepath)
    resized_img = img.resize((600, 600))
    label_img = ImageTk.PhotoImage(resized_img)
    picture_label.configure(image=label_img)
    picture_label.image = label_img

    path_entry.insert(0, filepath)


def select_img():
    global filepath
    filepath = tk.filedialog.askopenfilename(filetypes=(("png images", "*png"),
                                                        ("jpeg images", "*jepg"),
                                                        ("jpg images", "*jpg")))
    image_preview(filepath)


def watermark_text():

    global draw
    global img
    global filepath_2
    # select picture for watermark
    draw = ImageDraw.Draw(img)

    # mark
    text = watermark_entry.get()
    # Picture (width , height)
    width, height = img.size
    # Watermark size
    text_left_top_right_bottom = draw.textbbox((0, 0), text, font_size=width*0.03)  #   gives tuple of text left_top_right_bottom
    # margin
    margin_x = width * 0.05
    margin_y = width * 0.05
    # text width and height
    text_width = text_left_top_right_bottom[2] - text_left_top_right_bottom[0]
    text_height = text_left_top_right_bottom[3] - text_left_top_right_bottom[1]

    def position_calc(x_cor, y_cor):
        draw.text((x_cor, y_cor), text, font_size=width * 0.03)
        img.show()

    position = value_inside.get()
    if position == "lower right (LR)":
        x = width - text_width - margin_x
        y = height - text_height - margin_y
        position_calc(x, y)
    elif position == "upper left (UL)":
        x = 0+margin_x
        y = 0+margin_y
        position_calc(x, y)
    elif position == "center left (CL)":
        x = 0+margin_x
        y = (height - text_height - margin_y)/2
        position_calc(x, y)
    elif position == "lower left (LL)":
        x = 0+margin_x
        y = height - text_height - margin_y
        position_calc(x, y)
    elif position == "center upper (CU)":
        x = (width - text_width - margin_x)/2
        y = 0+margin_y
        position_calc(x, y)
    elif position == "center (CT)":
        x = (width - text_width - margin_x)/2
        y = (height - text_height - margin_y)/2
        position_calc(x, y)
    elif position == "center lower (CL)":
        x = (width - text_width - margin_x) / 2
        y = (height - text_height - margin_y)
        position_calc(x, y)
    elif position == "upper right (UR)":
        x = (width - text_width - margin_x)
        y = 0+margin_y
        position_calc(x, y)
    elif position == "center right (CR)":
        x = (width - text_width - margin_x)
        y = (height - text_height - margin_y)/2
        position_calc(x, y)

    # print(text_left_top_right_bottom)
    # print(width, height, text_width, text_height, x, y)
    # font = ImageFont.load_default(60)

    # draw.text((x, y), text, font_size=300)

    # response = messagebox.askquestion("", "Would you like to proceed?")
    # if response == "yes":


def upload_img():
    global img

    # shutil.copy(filepath_2, "./images/")

    copied_image = img.copy()
    copied_image.save(f"/Users/umitaslan/Downloads/Watermarked Picture/water_marked{random.randint(1, 300)}.png")
    messagebox.showinfo(message="File has been uploaded successfully")


window = tk.Tk()
window.geometry("700x700")

positions = ["upper left (UL)", "center left (CL)", "lower left (LL)", "center upper (CU)", "center (CT)",
             "center lower (CL)", "upper right (UR)", "center right (CR)", "lower right (LR)"]


select_button = tk.Button(text="Browse Image", command=lambda: select_img())
path_entry = tk.Entry(width=40)
watermark_label = tk.Label(text="Watermark Text", bg="white", fg="black")
watermark_entry = tk.Entry(width=40)
add_button = tk.Button(text="Add Image", command=upload_img)
watermark_preview_button = tk.Button(text="Preview ", command=lambda: watermark_text())
picture_label = tk.Label()

#   Drop down list for Watermark Position
dropdown_label = tk.Label(text="WM Position",bg="white", fg="black")
value_inside = StringVar(window)
value_inside.set("Select WM position")
dropdown = tk.OptionMenu(window, value_inside, *positions)

#   layout Grid
select_button.grid(column=1, row=1, padx=5, pady=5, sticky="wens")
path_entry.grid(column=2, row=1, padx=5, pady=5, sticky="wens")
watermark_entry.grid(column=2, row=2, padx=5, pady=5, sticky="wens")
watermark_label.grid(column=1, row=2, padx=5, pady=5, sticky="wens")
watermark_preview_button.grid(column=3, row=2, padx=5, pady=5, sticky="wens")
add_button.grid(column=3, row=1, padx=5, pady=5, sticky="wens")
picture_label.grid(column=1, row=4, columnspan=3, pady=5, sticky="wens")
dropdown_label.grid(column=1, row=3, padx=5, pady=5, sticky="wens")
dropdown.grid(column=2, row=3, padx=5, pady=5,columnspan=2, sticky="wens")

window.mainloop()
