import customtkinter as ctk
from PIL import Image

from pages.tvn_overlay.communication import CommunicationPage


def create_tvn_card(parent, title, subheading, image_path, command=None):
    card = ctk.CTkFrame(
        parent,
        height=150,
        corner_radius=20,
        fg_color="white",
    )
    card.pack(fill="x", padx=20, pady=12)
    card.pack_propagate(False)

    # image section
    img = ctk.CTkImage(
        Image.open(image_path),
        size=(170, 140)
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
        font=("Konkhmer Sleokchher", 27, "bold"),
        text_color="#3D6FB4"
    )
    title_label.pack(anchor="w")

    # subtitle
    subheading_label = ctk.CTkLabel(
        right_side,
        text=subheading,
        font=("Konkhmer Sleokchher", 23, "bold"),
        justify="left",
        text_color="#4E2626"
    )
    subheading_label.pack(anchor="w", pady=(10, 0))

    if command:
        widgets = [
            card,
            image_label,
            right_side,
            title_label,
            subheading_label
        ]

        for widget in widgets:
            widget.bind("<Button-1>", lambda e: command())

    return card


class TVNPage(ctk.CTkFrame):

    def __init__(self, parent, navigate):
        super().__init__(parent)

        self.pack(fill="both", expand=True)

        title = ctk.CTkLabel(
            self,
            text="Then VS Now",
            font=("Konkhmer Sleokchher", 30, "bold"),
            text_color="#3D6FB4"
        )
        title.pack(anchor="w", padx=25, pady=(20, 10))

        # scroller
        scroller = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroller.pack(fill="both", expand=True)

        # cards
        create_tvn_card(
            scroller,
            "Fashion",
            "From traditional attire to modern styles.",
            "assets/pictures/23.jpeg"
        )

        create_tvn_card(
            scroller,
            "Food",
            "From homemade recipes to fast-paced dining",
            "assets/pictures/2.jpeg"
        )

        create_tvn_card(
            scroller,
            "Comms",
            "From handwritten letters to instant messaging.",
            "assets/pictures/33.jpeg",
            command=lambda: navigate(CommunicationPage, navigate=navigate)
        )

        create_tvn_card(
            scroller,
            "Entertainment",
            "From moonlight stories to digital streaming.",
            "assets/pictures/7.jpeg"
        )
