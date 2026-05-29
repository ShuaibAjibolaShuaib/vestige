import customtkinter as ctk
from PIL import Image
# 1. Import your external page file here
import pre_colonial_page
import colonial
import independence
import digital


# ---------------- REUSABLE TIMELINE CARD CLASS ---------------- #

class TimelineCard(ctk.CTkFrame):
    def __init__(self, master, title, description, command=None, **kwargs):
        super().__init__(master, fg_color="#2D5B94", corner_radius=15, height=105, **kwargs)
        self.pack_propagate(False)

        self.command = command

        # White status indicator dot
        self.dot = ctk.CTkLabel(self, text="●", font=(
            "Poppins", 16), text_color="white")
        self.dot.place(x=15, y=12)

        # Title text
        self.card_title = ctk.CTkLabel(self, text=title, font=(
            "Poppins", 16, "bold"), text_color="white")
        self.card_title.place(x=40, y=12)

        # Description text
        self.card_desc = ctk.CTkLabel(self, text=description, font=(
            "Poppins", 13), text_color="white", justify="left")
        self.card_desc.place(x=40, y=48)

        self.heart_btn = ctk.CTkButton(self, text="♡", font=(
            "Poppins", 18), text_color="white", fg_color="transparent", width=30, hover=False)
        self.heart_btn.place(relx=0.95, rely=0.75, anchor="center")

        if self.command:
            self.bind_click_events(self.command)

    def bind_click_events(self, callback):
        self.configure(cursor="hand2")
        self.dot.configure(cursor="hand2")
        self.card_title.configure(cursor="hand2")
        self.card_desc.configure(cursor="hand2")

        self.bind("<Button-1>", lambda e: callback())
        self.dot.bind("<Button-1>", lambda e: callback())
        self.card_title.bind("<Button-1>", lambda e: callback())
        self.card_desc.bind("<Button-1>", lambda e: callback())


# ---------------- LAYOUT FUNCTION ---------------- #

def create_layout(app):

    # ---------------- MASTER SHOWPAGE ENGINE ---------------- #

    def show_page(page_name):
        # Wipes absolutely everything inside the window clean (Sidebars, Topbars, etc.)
        for widget in app.winfo_children():
            widget.destroy()

        # Create a brand new full-window frame to build on top of
        full_page_frame = ctk.CTkFrame(app, fg_color="#F5F5F5")
        full_page_frame.pack(fill="both", expand=True)

        # TOP NAVIGATION BAR (Always visible at the top, never pushed down!)
        nav_bar = ctk.CTkFrame(
            full_page_frame, fg_color="transparent", height=50)
        nav_bar.pack(fill="x", padx=30, pady=(15, 0))
        nav_bar.pack_propagate(False)

        # Global back button that reconstructs your entire main layout view
        back_btn = ctk.CTkButton(
            nav_bar,
            text="← Back to Main Menu",
            font=("Poppins", 13),
            fg_color="#3975BD",
            command=lambda: [full_page_frame.destroy(), create_layout(app)]
        )
        back_btn.pack(side="left")

        # Dynamic Content Container (The sub-pages load inside this)
        dynamic_container = ctk.CTkScrollableFrame(
            full_page_frame, fg_color="transparent")
        dynamic_container.pack(fill="both", expand=True,
                               padx=30, pady=(10, 20))

        # Routing to the correct external file
        if page_name == "pre_colonial":
            pre_colonial_page.load_view(dynamic_container)

        elif page_name == "colonial":
            colonial.load_view(dynamic_container)

        elif page_name == "independence":
            independence.load_view(dynamic_container)

        elif page_name == "digital":
            digital.load_view(dynamic_container)
    # In your main script/file:

    # ---------------- LEFT SIDEBAR ---------------- #

    sidebar = ctk.CTkFrame(
        app,
        width=200,
        corner_radius=0,
        fg_color="#1E1E2E"
    )

    sidebar.pack_propagate(False)
    sidebar.pack(side="left", fill="y")

    # ---------------- LOGO ---------------- #

    app_icon = ctk.CTkImage(
        Image.open("assets/icons/logo.png"),
        size=(20, 20)
    )

    logo_label = ctk.CTkLabel(
        sidebar,
        image=app_icon,
        text=" Vestige",
        compound="left",
        font=("Poppins", 15, "bold")
    )

    logo_label.pack(pady=(20, 10), padx=(5, 40))

    app_icon2 = ctk.CTkImage(
        Image.open("ggg.PNG"),
        size=(50, 50))
    logo_label2 = ctk.CTkLabel(
        sidebar,
        image=app_icon2,
        text="  Profile",
        compound="left",
        font=("Poppins", 15, "bold")
    )

    logo_label2.pack(pady=(0), padx=(0, 60))

    # ---------------- NAV BUTTON FUNCTION ---------------- #

    def nav_button(text, image_path):

        icon = ctk.CTkImage(
            Image.open(image_path),
            size=(20, 20)
        )

        button = ctk.CTkButton(
            sidebar,
            image=icon,
            text=text,
            height=45,
            corner_radius=10,
            fg_color="transparent",
            hover_color="#313244",
            anchor="w"
        )

        button.pack(fill="x", padx=10, pady=10)

        return button

    # ---------------- BUTTONS ---------------- #

    nav_button("Home", "home.png")
    nav_button("Then Vs Now", "tvn.png")
    nav_button("Timelines", "time.png")
    nav_button("Lost Traditions", "lost.png")
    nav_button("Gallery", "gallery.png")
    nav_button("About", "about.png")
    nav_button("Settings", "setting.png")
    nav_button("Log out", "logout.png")

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

    # --- MIDDLE FRAME CONTENT ---
    top_bar = ctk.CTkFrame(main_frame, fg_color="transparent")
    top_bar.pack(fill="x", padx=25, pady=(20, 10))

    quote_lbl = ctk.CTkLabel(
        top_bar,
        text="\"Exploring how the past shapes the present\nand what we risk losing...\"",
        font=("Poppins", 13, "italic"),
        text_color="#555555",
        justify="left"
    )
    quote_lbl.pack(side="left", anchor="w")

    search_bar = ctk.CTkEntry(
        top_bar,
        placeholder_text="Search",
        width=180,
        height=28,
        corner_radius=14,
        fg_color="#E0E0E0",
        border_width=0,
        text_color="black"
    )
    search_bar.pack(side="right", anchor="e", padx=10)

    timeline_container = ctk.CTkFrame(
        main_frame, fg_color="#EBEBEB", corner_radius=20)
    timeline_container.pack(fill="both", expand=True, padx=25, pady=(10, 20))

    # --- NAVIGATION CHANNELS ---
    def go_to_pre_colonial():
        show_page("pre_colonial")

    def go_to_colonial():
        show_page("colonial")

    def go_to_independence():
        show_page("independence")

    def go_to_digital_age():
        show_page("digital")

    # --- GENERATING THE CARDS USING THE TIMELINECARD CLASS ---
    card1 = TimelineCard(timeline_container, "Pre-Colonial Era",
                         "Traditional Kingdoms, oral storytelling, indigenous\nlanguages.", command=go_to_pre_colonial)
    card1.pack(fill="x", padx=20, pady=10)

    card2 = TimelineCard(timeline_container, "Colonial Era",
                         "Western Education and new cultural influences.", command=go_to_colonial)
    card2.pack(fill="x", padx=20, pady=10)

    card3 = TimelineCard(timeline_container, "Independence",
                         "National identity and cultural revival", command=go_to_independence)
    card3.pack(fill="x", padx=20, pady=10)

    card4 = TimelineCard(timeline_container, "Digital Age",
                         "Modern adaptation and technological shifts.", command=go_to_digital_age)
    card4.pack(fill="x", padx=20, pady=10)

    # ---------------- RIGHT SIDEBAR ---------------- #

    right_sidebar = ctk.CTkFrame(
        app,
        width=200,
        corner_radius=0,
        fg_color="#2D5B94"
    )

    right_sidebar.pack_propagate(False)
    right_sidebar.pack(side="right", fill="y")

    dyk_title = ctk.CTkLabel(
        right_sidebar,
        text="Did You Know...?",
        font=("Poppins", 14, "bold"),
        text_color="white"
    )
    dyk_title.pack(anchor="w", padx=15, pady=(15, 9))

    Third = ctk.CTkFrame(
        right_sidebar,
        width=170,
        height=170,
        corner_radius=10,
        fg_color="#FFFFFF",
    )
    Third.pack_propagate(False)
    Third.pack(fill="x", padx=15, pady=5)

    dyk_img_file = ctk.CTkImage(Image.open("10.jpeg"), size=(150, 80))
    dyk_img = ctk.CTkLabel(Third, image=dyk_img_file, text="",)
    dyk_img.pack(pady=(10, 5))

    dyk_text = ctk.CTkLabel(
        Third,
        text="☏Before smartphones,\ncommunication relied on letters\nand messengers (Town Criers).",
        font=("Exo", 10),
        text_color="black"
    )
    dyk_text.pack(pady=5)

    losing_title = ctk.CTkLabel(
        right_sidebar,
        text="What We're Losing",
        font=("Poppins", 14, "bold"),
        text_color="white"
    )
    losing_title.pack(anchor="w", padx=15, pady=(10, 0))

    losing_texts = [
        "Many indigenous languages are\ndisappearing",
        "Traditional clothing is now\nmostly worn at events",
        "The stories and customs that\nshaped us are slowly disappearing"
    ]
    # SAMPLE CARDS
    for i in range(3):
        card = ctk.CTkFrame(
            right_sidebar,
            width=170,
            height=70,
            corner_radius=5,
            fg_color="white"
        )
        card.pack_propagate(False)
        card.pack(fill="x", padx=15, pady=5)

        losing_lbl = ctk.CTkLabel(
            card,
            text=losing_texts[i],
            font=("Poppins", 9, "bold"),
            text_color="black",
            justify="center"
        )
        losing_lbl.pack(fill="both", expand=True, padx=10)
    saved_title = ctk.CTkLabel(
        right_sidebar,
        text="Saved Items",
        font=("Poppins", 14),
        text_color="white",

    )
    saved_title.pack(anchor="w", padx=15, pady=(10, 0))

    fourth = ctk.CTkFrame(
        right_sidebar,
        width=170,
        height=90,
        corner_radius=10,
        fg_color="#FFFFFF",
    )

    fourth.pack_propagate(False)
    fourth.pack(fill="x", padx=15, pady=5)
    saved_text = ctk.CTkLabel(
        fourth,
        text="You haven't saved anything yet!",
        font=("Poppins", 10, "bold"),
        text_color="black",


    )
    saved_text.pack(fill="both", expand=True)

    return main_frame

# In your main script/file:

# ---------------- APP WINDOW ---------------- #


app = ctk.CTk()

app.geometry("1200x650")
app.title("Vestige")

# CREATE THE LAYOUT
create_layout(app)

# START APP
app.mainloop()
