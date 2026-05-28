import customtkinter as ctk
from PIL import Image

from ui.theme import PRIMARY_BLUE, TEXT_WHITE

# tvn cards function


def create_card(parent, title, image_path, icon_path, command=None):
    card = ctk.CTkFrame(
        parent,
        width=300,
        height=170,
        corner_radius=20,
        fg_color="white",
    )
    card.pack_propagate(False)

    # image section
    img = ctk.CTkImage(
        Image.open(image_path),
        size=(120, 100)
    )
    image_label = ctk.CTkLabel(
        card,
        image=img,
        text=""
    )
    image_label.pack(side="left", padx=15, pady=15)

    # right section
    right_side = ctk.CTkFrame(card, fg_color="transparent")
    right_side.pack(
        side="right",
        fill="both",
        expand=True,
        padx=(0, 15),
        pady=15
    )

    # title
    title_label = ctk.CTkLabel(
        right_side,
        text=title,
        font=("Konkhmer Sleokchher", 19, "bold"),
        justify="center",
        text_color="#333"
    )
    title_label.pack(anchor="w")

    # icon
    icon = ctk.CTkImage(
        Image.open(icon_path),
        size=(50, 50)
    )
    icon_label = ctk.CTkLabel(
        right_side,
        image=icon,
        text=""
    )
    icon_label.pack(anchor="w", pady=(10, 0))

    return card

# timleine preview function


def create_timeline_preview(parent, title, subheading, command=None):
    card = ctk.CTkFrame(
        parent,
        height=150,
        corner_radius=20,
        fg_color="#2D5B94",
    )
    card.pack(fill="x", pady=10)
    card.pack_propagate(False)

    content = ctk.CTkFrame(card, fg_color="transparent")
    content.pack(fill="both", expand=True, padx=15, pady=15)

    left_side = ctk.CTkFrame(content, fg_color="transparent")
    left_side.pack(side="left", fill="y")

    circle = ctk.CTkLabel(
        left_side,
        text="●",
        font=("Arial", 40),
        text_color="white"
    )
    circle.pack(side="left", pady=(0, 12))

    text_frame = ctk.CTkFrame(content, fg_color="transparent")
    text_frame.pack(side="left")

    title_label = ctk.CTkLabel(
        text_frame,
        text=title,
        font=("Konkhmer Sleokchher", 25, "bold"),
        text_color="white"
    )
    title_label.pack(anchor="w")

    # subheading
    subheading_label = ctk.CTkLabel(
        text_frame,
        text=subheading,
        font=("Konkhmer Sleokchher", 20),
        text_color="white"
    )
    subheading_label.pack(anchor="w", pady=(5, 0))

    if command:
        widgets = [
            card,
            content,
            left_side,
            circle,
            text_frame,
            title_label,
            subheading_label
        ]
        for widget in widgets:
            widget.bind("<Button-1>", lambda e: command())

    return card


class HomePage(ctk.CTkFrame):

    def __init__(self, parent, tvn_command, timeline_command):
        super().__init__(parent)

        # top section tvn cards

        top_section = ctk.CTkFrame(parent, fg_color="transparent")
        top_section.pack(fill="x", padx=15, pady=(0, 20))

        # bottom section timeline preview
        bottom_section = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        bottom_section.pack(fill="both", expand=True, padx=15, pady=(0, 20))

        title = ctk.CTkLabel(
            top_section,
            text="Then VS Now",
            font=("Konkhmer Sleokchher", 23, "bold"),
            text_color="#333"
        )
        title.pack(anchor="w", padx=15, pady=(20, 10))

        card_grid = ctk.CTkFrame(top_section, fg_color="transparent")
        card_grid.pack(fill="x")
        card_grid.columnconfigure(0, weight=1)
        card_grid.columnconfigure(1, weight=1)

        card1 = create_card(
            card_grid,
            "Fashion",
            "assets/pictures/23.jpeg",
            "assets/icons/handbag.png"
        )
        card1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        card2 = create_card(
            card_grid,
            "Food",
            "assets/pictures/2.jpeg",
            "assets/icons/hamburger.png"
        )
        card2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        card3 = create_card(
            card_grid,
            "Communication",
            "assets/pictures/33.jpeg",
            "assets/icons/phone-call.png"
        )
        card3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        card4 = create_card(
            card_grid,
            "Entertainment",
            "assets/pictures/7.jpeg",
            "assets/icons/tv.png"
        )
        card4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # timeline preview
        create_timeline_preview(
            bottom_section,
            "Pre-colonial Era",
            "Traditional Kingdoms, Oral Story Telling, Indigenous Languages",
            command=timeline_command
        )

        create_timeline_preview(
            bottom_section,
            "Colonial Era",
            "Western Education and Cultural Influences",
            command=timeline_command
        )

        create_timeline_preview(
            bottom_section,
            "Independence",
            "National Identity and Cultural Revival",
            command=timeline_command
        )

        create_timeline_preview(
            bottom_section,
            "Digital Age",
            "Smartphones, Social Media, Globalization",
            command=timeline_command
        )

        create_timeline_preview(
            bottom_section,
            "Future Age",
            "AI, Virtual Reality, Cultural Fusion",
            command=timeline_command
        )
