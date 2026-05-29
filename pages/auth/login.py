import customtkinter as ctk
from PIL import Image

from pages.dashboard import Dashboard
from pages.home import HomePage
from ui.auth_layout import create_auth_layout
from ui.theme import PRIMARY_BLUE, TEXT_WHITE
from db.users_db import get_user_by_email


class LoginPage(ctk.CTkFrame):
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
            text="Login",
            font=("Konkhmer Sleokchher", 26, "bold"),
            text_color=TEXT_WHITE
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
            placeholder_text="Password",
            width=250,
            height=35,
            fg_color="white",
            text_color="black",
            corner_radius=15,
            show="*"
        )
        self.password_entry.place(
            relx=0.5, rely=0.60, anchor="center", relwidth=0.8)

        self.message_label = ctk.CTkLabel(panel, text="")
        self.message_label.place(relx=0.5, rely=0.68, anchor="center")

        # login button
        ctk.CTkButton(
            panel, text="Login",
            fg_color=PRIMARY_BLUE,
            text_color=TEXT_WHITE,
            width=150,
            height=35,
            command=self.login_user
        ).place(relx=0.5, rely=0.75, anchor="center")

        # switch to signup page
        from pages.auth.signup import SignupPage

        ctk.CTkButton(
            panel,
            text="Need and account? Sign Up",
            fg_color="transparent",
            text_color=PRIMARY_BLUE,
            hover=False,
            command=lambda: self.controller.show_page(SignupPage)
        ).place(relx=0.5, rely=0.85, anchor="center")

    def login_user(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()

        user = get_user_by_email(email)

        if user is None:
            self.message_label.configure(
                text="User not found", text_color="red")
            return

        # user tuple
        # 0 = id, 1 = full_name, 2 = email, 3 = password_hash
        stored_password = user[3]

        if password != stored_password:
            self.message_label.configure(
                text="Incorrect password", text_color="red")
            return

        self.controller.show_page(Dashboard)
