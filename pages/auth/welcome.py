import customtkinter as ctk
from PIL import Image

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

        # large logo image
        large_logo = ctk.CTkImage(
            light_image=Image.open("assets/icons/logo1.png"),
            dark_image=Image.open("assets/icons/logo1.png"),
            size=(300, 300)
        )

        small_logo = ctk.CTkImage(
            light_image=Image.open("assets/icons/logo2.png"),
            dark_image=Image.open("assets/icons/logo2.png"),
            size=(70, 70)
        )

        # large logo placeholder
        ctk.CTkLabel(
            panel,
            image=large_logo,
            text=""
        ).place(relx=0.5, rely=0.50, anchor="center")

        # small logo placeholder
        ctk.CTkLabel(
            right,
            image=small_logo,
            text=""
        ).place(relx=0.5, rely=0.15, anchor="center")

        ctk.CTkLabel(
            right,
            text="Vestige",
            font=("Konkhmer Sleokchher", 50, "bold"),
            text_color="white"
        ).place(relx=0.5, rely=0.30, anchor="center")

        # motto
        ctk.CTkLabel(
            right,
            text="Preserving Yesterday...",
            font=("Konkhmer Sleokchher", 20, "bold")
        ).place(relx=0.5, rely=0.5, anchor="center")

        # get started button
        ctk.CTkButton(
            right,
            text="Get Started",
            fg_color=PRIMARY_BLUE,
            text_color=TEXT_WHITE,
            corner_radius=30,
            width=250,
            height=57,
            font=("Khonkhmer Sleokchher", 22, "bold"),
            command=lambda: self.controller.show_page(LoginPage)
        ).place(relx=0.50, rely=0.68, anchor="center")
