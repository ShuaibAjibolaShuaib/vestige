import customtkinter as ctk
from PIL import Image

from pages.dashboard import Dashboard
from pages.home import HomePage
from pages.auth.login import LoginPage
from ui.auth_layout import create_auth_layout
from ui.theme import PRIMARY_BLUE, TEXT_WHITE
from db.users_db import create_user, get_user_by_email


class SignupPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        page, left, right, panel = create_auth_layout(self, panel_side="right")
        page.pack(fill="both", expand=True)

        ctk.CTkLabel(
            left, text="Vestige",
            font=("Konkhmer Sleokchher", 22, "bold"),
            text_color=TEXT_WHITE
        ).place(relx=0.08, rely=0.06, anchor="w")

        logo = ctk.CTkImage(
            light_image=Image.open("assets/icons/logo1.png"),
            dark_image=Image.open("assets/icons/logo1.png"),
            size=(300, 300)
        )

        ctk.CTkLabel(
            left,
            image=logo,
            text="",
        ).place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(
            panel,
            text="Sign Up",
            font=("Konkhmer Sleokchher", 26, "bold")
        ).place(relx=0.5, rely=0.12, anchor="center")

        # entry fields
        self.name_entry = ctk.CTkEntry(
            panel,
            placeholder_text="Full Name",
            width=250,
            height=35,
            fg_color="white",
            text_color="black",
            corner_radius=15
        )
        self.name_entry.place(relx=0.5, rely=0.30,
                              anchor="center", relwidth=0.8)

        self.email_entry = ctk.CTkEntry(
            panel,
            placeholder_text="Email",
            width=250,
            height=35,
            fg_color="white",
            text_color="black",
            corner_radius=15
        )
        self.email_entry.place(relx=0.5, rely=0.45,
                               anchor="center", relwidth=0.8)

        self.password_entry = ctk.CTkEntry(
            panel,
            placeholder_text="Create a Password",
            width=250,
            height=35,
            fg_color="white",
            text_color="black",
            corner_radius=15,
            show="*"
        )
        self.password_entry.place(
            relx=0.5, rely=0.60, anchor="center", relwidth=0.8)

        # signup button
        ctk.CTkButton(
            panel, text="Sign Up",
            fg_color=PRIMARY_BLUE,
            text_color=TEXT_WHITE,
            width=150,
            height=35,
            command=self.signup_user
        ).place(relx=0.5, rely=0.75, anchor="center")

        # switch to login page

        ctk.CTkButton(
            panel,
            text="Already have an account? Login",
            fg_color="transparent",
            text_color=PRIMARY_BLUE,
            hover=False,
            command=lambda: self.controller.show_page(LoginPage)
        ).place(relx=0.5, rely=0.85, anchor="center")

        self.message_label = ctk.CTkLabel(panel, text="")
        self.message_label.place(relx=0.5, rely=0.68, anchor="center")

    def signup_user(self):
        full_name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        if not full_name or not email or not password:
            self.message_label.configure(
                text="All fields are required",
                text_color="red"
            )
            return

        existing_user = get_user_by_email(email)
        if existing_user:
            self.message_label.configure(
                text="Email already in use",
                text_color="red"
            )
            return

        create_user(full_name, email, password)
        self.message_label.configure(
            text="Account created successfully",
            text_color="green"
        )
        self.controller.show_page(HomePage)
