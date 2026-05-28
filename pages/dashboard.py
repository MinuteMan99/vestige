import customtkinter as ctk

from ui.layout import create_layout
from pages.home import HomePage
from pages.timeline import TimelinePage
from pages.tvn import TVNPage


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.container = create_layout(
            self,
            home_command=lambda: self.show_content(HomePage),
            timeline_command=lambda: self.show_content(TimelinePage),
            tvn_command=lambda: self.show_content(TVNPage),
        )

        # showing the homepage initially
        self.show_content(HomePage)

    def show_content(self, page_class):
        # destroy existing content
        for widget in self.container.winfo_children():
            widget.destroy()

        if page_class == HomePage:
            page_class(
                self.container,
                tvn_command=lambda: self.show_content(TVNPage),
                timeline_command=lambda: self.show_content(TimelinePage)
            )
        else:
            page_class(self.container)
