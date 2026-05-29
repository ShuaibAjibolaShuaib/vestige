import customtkinter as ctk
from PIL import Image


def create_tradition_card(
    parent,
    title,
    description,
    side_image1,
    side_image2,
    side_image3
):

    card = ctk.CTkFrame(
        parent,
        height=700,
        corner_radius=40,
        fg_color="#FFFFFF"
    )
    card.pack(fill="x", padx=20, pady=15)
    card.pack_propagate

    # left section
    left_section = ctk.CTkFrame(
        card,
        fg_color="transparent",
        width=200
    )
    left_section.pack(side="left", fill="y", padx=15, pady=15)

    # images
    img1 = ctk.CTkImage(
        Image.open(side_image1),
        size=(150, 120)
    )
    img1_label = ctk.CTkLabel(
        left_section,
        image=img1,
        text=""
    )
    img1_label.pack(pady=5)

    img2 = ctk.CTkImage(
        Image.open(side_image2),
        size=(150, 120)
    )
    img2_label = ctk.CTkLabel(
        left_section,
        image=img2,
        text=""
    )
    img2_label.pack(pady=5)

    img3 = ctk.CTkImage(
        Image.open(side_image3),
        size=(150, 120)
    )
    img3_label = ctk.CTkLabel(
        left_section,
        image=img3,
        text=""
    )
    img3_label.pack(pady=5)

    # right section
    right_section = ctk.CTkFrame(card, fg_color="transparent")
    right_section.pack(
        side="right",
        fill="both",
        expand=True,
        padx=15,
        pady=20
    )

    # title
    title_label = ctk.CTkLabel(
        right_section,
        text=title,
        font=("Konkhmer Sleokchher", 30, "bold"),
        text_color="#6B1818",
        wraplength=450
    )
    title_label.pack(anchor="w", pady=(10, 20))

    # description
    desc_label = ctk.CTkLabel(
        right_section,
        text=description,
        font=("Konkhmer Sleokchher", 25, "bold"),
        text_color="#3D6FB4",
        justify="center",
        wraplength=450
    )
    desc_label.pack(anchor="w")


class LTRPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent)

        self.pack(fill="both", expand=True)

        scroll = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )
        scroll.pack(fill="both", expand=True)

        # ltr cards

        create_tradition_card(
            scroll,
            "Traditional Fanfare For The High Chieftains",
            "Every quarter of the year, the High Chieftains of the lands\n bequeathed to them, meet at the Sacred Meeting Ground\n to discuss the territory, new lands and politics.",
            "assets/pictures/51.jpeg",
            "assets/pictures/55.jpeg",
            "assets/pictures/57.jpeg"
        )

        create_tradition_card(
            scroll,
            "Ritualistic Dances and Their Significances and Symbolism",
            "Each ethnic group accros Nigeria has a select dance\n representing many concepts like milestones, seasons\n or simple expressions of the people .",
            "assets/pictures/7.jpeg",
            "assets/pictures/8.jpeg",
            "assets/pictures/37.jpeg"
        )

        create_tradition_card(
            scroll,
            "Traditional Parades and Cultural Celebrations",
            "These large and colourful marches are\n meant to lift moral and to express\ntogetherness and love for their traditions\nand their fellow man.",
            "assets/pictures/51.jpeg",
            "assets/pictures/55.jpeg",
            "assets/pictures/57.jpeg"
        )

        create_tradition_card(
            scroll,
            "Traditional Rights",
            "These events are held as sacred in the\nlives of the people. These events\nrepresents a trancendence into\ndifferent stages in life..",
            "assets/pictures/7.jpeg",
            "assets/pictures/8.jpeg",
            "assets/pictures/37.jpeg"
        )

        create_tradition_card(
            scroll,
            "Importance of Music in the Consciousness of people",
            "Music is an essential part of culture\nwith it being in many ways the primary\nmethod of storytelling, history and culture..",
            "assets/pictures/51.jpeg",
            "assets/pictures/55.jpeg",
            "assets/pictures/57.jpeg"
        )

        create_tradition_card(
            scroll,
            "Traditional Faiths and Beliefs",
            "The traditional beliefs are vast and varied,\nwith a pantheon of gods, lesser deities\nnature spirits and ancestors. They based\ntheir culture around these beliefs.",
            "assets/pictures/7.jpeg",
            "assets/pictures/8.jpeg",
            "assets/pictures/37.jpeg"
        )
