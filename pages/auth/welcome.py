import customtkinter as ctk

from pages.auth.login import LoginPage
from ui.auth_layout import create_auth_layout
from ui.theme import PRIMARY_BLUE, TEXT_WHITE


class WelcomePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        # shared layout
        page, left, right, panel = create_auth_layout(self, panel_side="left")
        page.pack(fill="both", expand=True)

        # logo placeholder
        ctk.CTkLabel(
            right,
            text="lOGO",
            font=("Konkhmer Sleokchher", 40, "bold")
        ).place(relx=0.5, rely=0.5, anchor="center")

        # small logo placeholder
        ctk.CTkLabel(
            right,
            text="LOGO",
            font=("Konkhmer Sleokchher", 20, "bold"),
            text_color="white"
        ).place(relx=0.5, rely=0.15, anchor="center")

        ctk.CTkLabel(
            right,
            text="Vestige",
            font=("Konkhmer Sleokchher", 32, "bold"),
            text_color="white"
        ).place(relx=0.5, rely=0.30, anchor="center")

        # motto
        ctk.CTkLabel(
            panel,
            text="Preserving Yesterday",
            font=("Konkhmer Sleokchher", 18),
            text_color="white"
        ).place(relx=0.5, rely=0.40, anchor="center")

        # get started button
        ctk.CTkButton(
            right,
            text="Get Started",
            fg_color=PRIMARY_BLUE,
            text_color=TEXT_WHITE,
            command=lambda: self.controller.show_page(LoginPage)
        ).place(relx=0.5, rely=0.60, anchor="center")
