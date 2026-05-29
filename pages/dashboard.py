import customtkinter as ctk

from ui.layout import create_layout
from pages.home import HomePage
from pages.timeline import TimelinePage
from pages.tvn import TVNPage
from pages.ltr import LTRPage


class Dashboard(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.container = create_layout(
            self,
            home_command=lambda: self.show_content(
                HomePage, navigate=self.show_content),
            timeline_command=lambda: self.show_content(
                TimelinePage, navigate=self.show_content),
            tvn_command=lambda: self.show_content(
                TVNPage, navigate=self.show_content),
            ltr_command=lambda: self.show_content(LTRPage)
        )

        # showing the homepage initially

        self.show_content(
            HomePage,
            navigate=self.show_content
        )

    def show_content(self, page_class, **kwargs):
        # destroy existing content
        for widget in self.container.winfo_children():
            widget.destroy()

            if isinstance(page_class, str):
                if page_class == "tvn":
                    from pages.tvn import TVNPage
                    page_class = TVNPage

        page_class(self.container, **kwargs)
