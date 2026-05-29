import customtkinter as ctk
from PIL import Image


def create_info_card(
    parent,
    title,
    description,
    image_path
):
    card = ctk.CTkFrame(
        parent,
        height=300,
        fg_color="#f4f7fc",
        corner_radius=15
    )
    card.pack(fill="x", pady=10)
    card.pack_propagate(False)

    title_label = ctk.CTkLabel(
        card,
        text=title,
        font=("Konkhmer Sleokchher", 28, "bold"),
        text_color="#1d5b96"
    )
    title_label.pack(anchor="w", padx=15, pady=(15, 5))

    content = ctk.CTkFrame(card, fg_color="transparent")
    content.pack(fill="both", expand=True, padx=15, pady=(0, 15))

    img = ctk.CTkImage(
        Image.open(image_path),
        size=(170, 170)
    )
    img_label = ctk.CTkLabel(
        content,
        image=img,
        text=""
    )
    img_label.image = img
    img_label.pack(side="left", padx=(0, 15))

    desc_label = ctk.CTkLabel(
        content,
        text=description,
        text_color="#5B1D1D",
        wraplength=300,
        justify="left",
        font=("Konkhmer Sleokchher", 17)
    )
    desc_label.pack(side="left", fill="both", expand=True)

    return card


def build_column(parent, sections):
    for section in sections:
        create_info_card(
            parent,
            section["title"],
            section["description"],
            section.get("image")
        )


class CommunicationPage(ctk.CTkFrame):

    def __init__(self, parent, navigate):
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        scroll = ctk.CTkScrollableFrame(self, fg_color="white")
        scroll.pack(fill="both", expand=True, padx=20, pady=20)

        # x button
        close_btn = ctk.CTkButton(
            scroll,
            text="X",
            width=40,
            command=lambda: navigate(__import__("pages.tvn", fromlist=[
                                     "TVNPage"]).TVNPage, navigate=navigate)
        )
        close_btn.pack(anchor="ne", pady=10)

        # title
        title = ctk.CTkLabel(
            scroll,
            text="Communication: Then VS Now",
            font=("Arial", 28, "bold"),
            text_color="#1d5b96"
        )
        title.pack(pady=(10, 5))

        desc = ctk.CTkLabel(
            scroll,
            text="Communication in past Nigeria was deeply rooted in community and\ntradition. People relied on face-to-face interaction, town criers, drums,\nstorytelling and handwritten letters to share news and preserve cultural\nknowledge.",
            font=("Konkhmer Sleokchher", 20, "bold"),
            text_color="#511616",
            wraplength=900,
            justify="center"
        )
        desc.pack(pady=(0, 25))

        main = ctk.CTkFrame(scroll, fg_color="transparent")
        main.pack(fill="both", expand=True, padx=10, pady=10)

        left = ctk.CTkFrame(main, fg_color="transparent")
        left.pack(side="left", fill="both", expand=True, padx=10, anchor="n")

        right = ctk.CTkFrame(main, fg_color="transparent")
        right.pack(side="left", fill="both", expand=True, padx=10, anchor="n")

        # left side

        traditional_sections = [
            {
                "title": "Town Criers",
                "description": "Messages were passed around villages using drums and loud announcements.",
                "image": "assets/pictures/5.jpeg"
            },
            {
                "title": "Letter Writing",
                "description": "People relied on handwritten letters for long-distance communication.",
                "image": "assets/pictures/25.jpeg"
            }
        ]

        # right side

        modern_sections = [
            {
                "title": "Social Media",
                "description": "People now communicate instantly using apps like WhatsApp and Instagram.",
                "image": "assets/pictures/41.jpeg"
            },
            {
                "title": "Video Calls",
                "description": "Technology allows face-to-face conversations from anywhere.",
                "image": "assets/pictures/33.jpeg"
            }
        ]

        build_column(left, traditional_sections)
        build_column(right, modern_sections)
