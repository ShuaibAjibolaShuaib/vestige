import customtkinter as ctk
from PIL import Image


def create_card(
        parent,
        bg_img_path,
        fg_img_path,
        title,
        description,
        back_command=None
):

    card = ctk.CTkFrame(
        parent,
        width=500,
        height=800,
        fg_color="white",
        corner_radius=20
    )
    card.pack(fill="x", padx=5, pady=5)
    card.pack_propagate(False)

    close_btn = ctk.CTkButton(
        card,
        text="X",
        font=("Konkhmer Sleokchher", 25, "bold"),
        width=35,
        height=35,
        corner_radius=100,
        command=back_command
    )
    close_btn.place(
        relx=0.9,
        rely=0.0,
        anchor="ne",
        x=20,
        y=20
    )

    title_label = ctk.CTkLabel(
        card,
        text=title,
        font=("Konkhmer Sleokchher", 30, "bold"),
        text_color="#401616",
    )
    title_label.pack(pady=5)

    fg_img = ctk.CTkImage(
        Image.open(fg_img_path),
        size=(600, 400),
    )
    fg_label = ctk.CTkLabel(
        card,
        image=fg_img,
        text=""
    )
    fg_label.place(relx=0.5, rely=0.8, anchor="center")

    desc_label = ctk.CTkLabel(
        card,
        text=description,
        font=("Konkhmer Sleokchher", 20, "bold"),
        text_color="#3D6FB4"
    )
    desc_label.pack(pady=7)


class TimeColonialPage(ctk.CTkFrame):

    def __init__(self, parent, navigate, back_page):
        super().__init__(parent)

        self.pack(fill="both", expand=True)

        scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        scroll.pack(fill="both", expand=True)

        create_card(
            scroll,
            "assets/pictures/background.jpeg",
            "assets/pictures/43.jpeg",
            "Major Events in Pre-Colonial Nigeria",
            "Rise of Powerful Kingdoms\n - The formation of the Oyo Empired led to one of West Africa's most\npowerful states\n - The rise of the Benin Kingdom brought advances in governance,\ntrade, and bronze art.\n- The establishment of the Kanem-Bornu Empire created a major\npolitical and commercial center. \nSome more major events include:\n - Spread of Islam \n - Cultural Development, and \n- War and Expansion",
            back_command=lambda: navigate(back_page, navigate=navigate)
        )
