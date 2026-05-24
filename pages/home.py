import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class HomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.configure(fg_color="#F3F3F3")

        title_label = ctk.CTkLabel(
            self,
            text="Welcome to the Home Page",
            font=("Konkhmer Sleokchher", 24, "bold"),
            text_color="black"
        )

        title_label.place(x=520, y=40)

#for the scrolling frame
my_frame = ctk.CTkScrollableFrame(self, 
    orientation="vertical",                                        
    width=795,                                        
    height=256,                                         
    label_text="Timeline Of Cultural Change",
    fg_color="#E9E9E9",          
    label_fg_color="#E9E9E9",
    label_text_color="#6A6A6A",
    corner_radius=12
                                            
)
my_frame.place(x=285, y=560)

button_texts = [
    "Pre-Colonial Era\nTraditional Kingdoms, oral storytelling & indigenous languages.",

    "Colonial Era\nWestern Education and new cultural influences",

    "Independence\nNational Identity and cultural revival",

    "Digital Age\nSmartphones, social media & globalisation",

    "Future\nTechnology preserving culture"
]

for text in button_texts:
    ctk.CTkButton(
        my_frame,
        text=text,
        width=576,
        height=121,
        anchor="w",
        fg_color="#3F6EA8",
        hover_color="#355E8C",
        text_color="white",
        corner_radius=10,
        font=("Arial", 18)
    ).pack(pady=10)

#for the button frame
category_frame = ctk.CTkFrame(
    self,
    width=760,
    height=320,
    fg_color="#F3F3F3"
)

category_frame.place(x=320, y=180)


fashion_image = ctk.CTkImage(
    light_image=Image.open("images/fashion.jpg"),
    size=(167, 141)
)

food_image = ctk.CTkImage(
    light_image=Image.open("images/food.jpg"),
    size=(167, 141)
)

comms_image = ctk.CTkImage(
    light_image=Image.open("images/comms.jpg"),
    size=(167, 141)
)

entertainment_image = ctk.CTkImage(
    light_image=Image.open("images/entertainment.jpg"),
    size=(167, 141)
)

fashion_icon = ctk.CTkImage(
    light_image=Image.open("icons/bag.png"),
    size=(90, 90)
)

food_icon = ctk.CTkImage(
    light_image=Image.open("icons/burger.png"),
    size=(90, 90)
)

comms_icon = ctk.CTkImage(
    light_image=Image.open("icons/phone.png"),
    size=(90, 90)
)

entertainment_icon = ctk.CTkImage(
    light_image=Image.open("icons/tv.png"),
    size=(90, 90)
)

cards = [
    ("Fashion", fashion_image, fashion_icon),
    
    ("Food", food_image, food_icon),
    
    ("Comms", comms_image, comms_icon),
    
    ("Entertainment", entertainment_image, entertainment_icon)
]



row = 0
column = 0

for title, picture, icon in cards:

    card = ctk.CTkFrame(
        category_frame,
        width=391,
        height=189,
        corner_radius=20,
        fg_color="white",
        border_width=1,
        border_color="#D9D9D9"
    )

    card.grid(row=row, column=column, padx=10, pady=10)

    card.grid_propagate(False)

    image_label = ctk.CTkLabel(
        card,
        image=picture,
        text=""
    )

    image_label.place(x=15, y=20)

    title_label = ctk.CTkLabel(
        card,
        text=title,
        font=("Konkhmer Sleokchher", 20, "bold"),
        text_color="#707070"
    )

    title_label.place(x=150, y=15)

    icon_label = ctk.CTkLabel(
        card,
        image=icon,
        text=""
    )

    icon_label.place(x=220, y=60)
    
    column += 1

    if column > 1:
        column = 0
        row += 1


root = ctk.CTk()

root.title("Vestige")
root.geometry("1440x896")

homepage = HomePage(root, None)
homepage.pack(fill="both", expand=True)

root.mainloop()