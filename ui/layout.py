import customtkinter as ctk
from PIL import Image


# ---------------- LAYOUT FUNCTION ---------------- #

def create_layout(app):

    # ---------------- LEFT SIDEBAR ---------------- #

    sidebar = ctk.CTkFrame(
        app,
        width=200,
        corner_radius=0,
        fg_color="#1E1E2E"
    )

    sidebar.pack_propagate(False)
    sidebar.pack(side="left", fill="y")

    # ---------------- LOGO ---------------- #

    app_icon = ctk.CTkImage(
        Image.open("ves.PNG"),
        size=(20, 20)
    )

    logo_label = ctk.CTkLabel(
        sidebar,
        image=app_icon,
        text=" Vestige",
        compound="left",
        font=("Poppins", 15, "bold")
    )

    logo_label.pack(pady=(20,10), padx=(5,40))

    app_icon = ctk.CTkImage(
        Image.open("ggg.PNG"),
        size=(50, 50))
    logo_label = ctk.CTkLabel(
        sidebar,
        image=app_icon,
        text="  Profile" ,
        compound="left",
        font=("Poppins", 15, "bold")
    )

    logo_label.pack(pady=(0), padx=(0,60))

    # ---------------- NAV BUTTON FUNCTION ---------------- #

    def nav_button(text, image_path):

        icon = ctk.CTkImage(
            Image.open(image_path),
            size=(20, 20)
        )

        button = ctk.CTkButton(
            sidebar,
            image=icon,
            text=text,
            height=45,
            corner_radius=10,
            fg_color="transparent",
            hover_color="#313244",
            anchor="w"
        )

        button.pack(fill="x", padx=10, pady=10)

        return button

    # ---------------- BUTTONS ---------------- #

    nav_button("Home", "home.png")
    nav_button("Then Vs Now", "tvn.png")
    nav_button("Timelines", "time.png")
    nav_button("Lost Traditions", "lost.png")
    nav_button("Gallery", "gallery.png")
    nav_button("About", "about.png")
    nav_button("Settings", "setting.png")
    nav_button("Log out", "logout.png")

    # ---------------- MAIN AREA ---------------- #

    main_frame = ctk.CTkFrame(
        app,
        fg_color="#F5F5F5"
    )

    main_frame.pack(
        side="left",
        fill="both",
        expand=True
    )

    # SAMPLE CONTENT
    title = ctk.CTkLabel(
        main_frame,
        text="Main Content Area",
        font=("Poppins", 35, "bold"),
        text_color="black"
    )

    title.pack(pady=50)

    # ---------------- RIGHT SIDEBAR ---------------- #

    right_sidebar = ctk.CTkFrame(
        app,
        width=200,
        corner_radius=0,
        fg_color="#525258"
    )

    right_sidebar.pack_propagate(False)
    right_sidebar.pack(side="right", fill="y")

    Third = ctk.CTkFrame(
    right_sidebar,
    width=170,
    height=170,
    
    corner_radius=10,
    fg_color="#FFFFFF",
    )
    


    Third.pack( fill="y", pady=(40,40))
    # SAMPLE CARDS
    for i in range(3):

        card = ctk.CTkFrame(
            right_sidebar,
            width=170,
            height=70,
            corner_radius=10,
            fg_color="white"
        )

        card.pack(pady=8)
        
        

    fourth = ctk.CTkFrame(
    right_sidebar,
    width=170,
    height=90,
    
    corner_radius=10,
    fg_color="#FFFFFF",
    
    )

    fourth.pack( fill="y", pady=(10))
        

        

       


    return main_frame


# ---------------- APP WINDOW ---------------- #

app = ctk.CTk()

app.geometry("1200x650")
app.title("Vestige")

# CREATE THE LAYOUT
create_layout(app)

# START APP
app.mainloop()