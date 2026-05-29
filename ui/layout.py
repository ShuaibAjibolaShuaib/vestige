import customtkinter as ctk
from PIL import Image


# ---------------- LAYOUT FUNCTION ---------------- #

def create_layout(
    app,
    home_command,
    timeline_command,
    tvn_command,
    gallery_command=None,
    ltr_command=None
):

    # ---------------- LEFT SIDEBAR ---------------- #

    left_sidebar = ctk.CTkFrame(
        app,
        width=200,
        corner_radius=0,
        fg_color="#1E1E2E"
    )

    left_sidebar.pack_propagate(False)
    left_sidebar.pack(side="left", fill="y")

    # ---------------- LOGO ---------------- #

    app_icon = ctk.CTkImage(
        Image.open("assets/icons/logo.png"),
        size=(20, 20)
    )

    logo_label = ctk.CTkLabel(
        left_sidebar,
        image=app_icon,
        text=" Vestige",
        compound="left",
        font=("Poppins", 15, "bold")
    )

    logo_label.pack(pady=(20, 10), padx=(5, 40))

    app_icon2 = ctk.CTkImage(
        Image.open("assets/pictures/profile.PNG"),
        size=(50, 50))
    logo_label2 = ctk.CTkLabel(
        left_sidebar,
        image=app_icon2,
        text="  Profile",
        compound="left",
        font=("Poppins", 15, "bold")
    )

    logo_label2.pack(pady=(0), padx=(0, 60))

    top_left = ctk.CTkFrame(left_sidebar, fg_color="transparent")
    top_left.pack(fill="x", side="top")

    bottom_left = ctk.CTkFrame(left_sidebar, fg_color="transparent")
    bottom_left.pack(fill="x", side="bottom", pady=10)

    # ---------------- NAV BUTTON FUNCTION ---------------- #

    def nav_button(text, image_path, parent, command=None):

        icon = ctk.CTkImage(
            light_image=Image.open(image_path),
            dark_image=Image.open(image_path),
            size=(20, 20)
        )

        button = ctk.CTkButton(
            parent,
            image=icon,
            text=text,
            command=command,
            height=45,
            corner_radius=10,
            fg_color="transparent",
            hover_color="#2A2C57",
            anchor="w"
        )

        button.pack(fill="x", padx=10, pady=10)

        return button

    # ---------------- BUTTONS ---------------- #

    nav_button("Home", "assets/icons/home.png", top_left, command=home_command)
    nav_button("Then Vs Now", "assets/icons/tvn.png",
               top_left, command=tvn_command)
    nav_button("Timelines", "assets/icons/time.png",
               top_left, command=timeline_command)
    nav_button("Lost Traditions", "assets/icons/lost.png",
               top_left, command=ltr_command)
    nav_button("Gallery", "assets/icons/gallery.png",
               top_left, command=gallery_command)
    nav_button("About", "assets/icons/about.png", top_left)
    nav_button("Settings", "assets/icons/setting.png", bottom_left)
    nav_button("Log out", "assets/icons/logout.png", bottom_left)

    # ---------------- MAIN AREA ---------------- #

    main_frame = ctk.CTkFrame(
        app,
        fg_color="#F5F5F5"
    )

    main_frame.pack(
        side="left",
        fill="both",
        expand=True
    )

    # --- TOP BAR (QUOTE & SEARCH) ---
    top_bar = ctk.CTkFrame(main_frame, fg_color="transparent")
    top_bar.pack(fill="x", padx=25, pady=(20, 10))

    quote = ctk.CTkLabel(
        top_bar,
        text="\"Exploring how the past shapes the present\nand what we risk losing...\"",
        font=("Poppins", 13, "italic"),
        text_color="#555555",
        justify="left"
    )
    quote.pack(side="left", anchor="w")

    search_bar = ctk.CTkEntry(
        top_bar,
        placeholder_text="Search",
        width=220,
        height=28,
        corner_radius=14,
        fg_color="#E0E0E0",
        border_width=0,
        text_color="black"
    )
    search_bar.pack(side="right", anchor="e", padx=10)

    # --- GREY CONTENT CONTAINER ---
    container = ctk.CTkFrame(
        main_frame, fg_color="#EBEBEB", corner_radius=20)
    container.pack(fill="both", expand=True, padx=25, pady=(10, 20))

    # ---------------- RIGHT SIDEBAR ---------------- #

    # Changed background color to match the deep blue style in the screenshot
    right_sidebar = ctk.CTkFrame(
        app,
        width=280,
        corner_radius=0,
        fg_color="#2D5B94"
    )

    right_sidebar.pack_propagate(False)
    right_sidebar.pack(side="right", fill="y")

    top_right = ctk.CTkFrame(right_sidebar, fg_color="transparent")
    top_right.pack(fill="x", side="top")

    bottom_right = ctk.CTkFrame(right_sidebar, fg_color="transparent")
    bottom_right.pack(fill="x", side="bottom")

    # --- SECTION 1: DID YOU KNOW ---
    dyk_title = ctk.CTkLabel(
        top_right,
        text="Did You Know...?",
        font=("Konkhmer Sleokchher", 20, "bold"),
        text_color="white"
    )
    dyk_title.pack(anchor="w", padx=15, pady=(15, 9))

    third = ctk.CTkFrame(
        top_right,
        width=260,
        height=270,
        corner_radius=19,
        fg_color="#FFFFFF",
    )
    third.pack_propagate(False)
    third.pack(padx=15, pady=5)

    # image for the top frame

    dyk_img_file = ctk.CTkImage(
        Image.open("assets/pictures/5.jpeg"),
        size=(200, 185)
    )
    dyk_img = ctk.CTkLabel(third, image=dyk_img_file, text="",)
    dyk_img.pack(pady=(10, 5))

    dyk_text = ctk.CTkLabel(
        third,
        text="☏ Before smartphones,\ncommunication relied on letters\nand messengers (Town Criers).",
        font=("Konkhmer Sleokchher", 13, "bold"),
        text_color="black"

    )
    dyk_text.pack(pady=5)

    # what we're losing section
    losing_title = ctk.CTkLabel(
        top_right,
        text="What We're Losing",
        font=("Konkhmer Sleokchher", 20, "bold"),
        text_color="white"
    )
    losing_title.pack(anchor="w", padx=15, pady=(10, 0))

    # losing texts
    losing_texts = [
        "Many indigenous languages\nare disappearing",
        "Traditional clothing is now\nmostly worn at events",
        "The stories and customs that\nshaped us are slowly disappearing"
    ]

    for i in range(3):
        card = ctk.CTkFrame(
            top_right,
            width=400,
            height=90,
            corner_radius=12,
            fg_color="white"
        )
        card.pack_propagate(False)
        card.pack(padx=15, pady=5)

        losing_lbl = ctk.CTkLabel(
            card,
            text=losing_texts[i],
            font=("Konkhmer Sleokchher", 13, "bold"),
            text_color="black",
            justify="left",
        )
        losing_lbl.place(relx=0.45, rely=0.5, anchor="center")

    # saved items section
    saved_title = ctk.CTkLabel(
        bottom_right,
        text="Saved Items",
        font=("Poppins", 20, "bold"),
        text_color="white",
    )
    saved_title.pack(anchor="w", padx=15, pady=(10, 0))

    fourth = ctk.CTkFrame(
        bottom_right,
        width=250,
        height=90,
        corner_radius=20,
        fg_color="#FFFFFF",
    )
    fourth.pack_propagate(False)
    fourth.pack(padx=15, pady=5)

    saved_text = ctk.CTkLabel(
        fourth,
        corner_radius=20,
        text="You haven't saved anything yet!",
        font=("Poppins", 13, "bold"),
        text_color="black",
    )
    saved_text.place(relx=0.5, rely=0.5, anchor="center")

    return container
