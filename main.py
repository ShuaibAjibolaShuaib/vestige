import customtkinter as ctk
from customtkinter import *

from pages.auth.welcome import WelcomePage
from pages.auth.login import LoginPage
from pages.auth.signup import SignupPage


class App:

    # app window
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("900x600")
        self.root.title("Vestige")

        self.container = ctk.CTkFrame(self.root, fg_color="transparent")
        self.container.pack(fill="both", expand=True)

        self.current_page = None
        self.show_page(WelcomePage)

        self.root.mainloop()

    def show_page(self, page_class):
        if self.current_page is not None:
            self.current_page.destroy()

        self.current_page = page_class(self.container, self)
        self.current_page.pack(fill="both", expand=True)


app = App()
