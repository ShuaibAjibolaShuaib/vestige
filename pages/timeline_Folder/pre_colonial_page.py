import customtkinter as ctk
from PIL import Image

def load_view(container):
    # 1. BACKGROUND IMAGE
    bg_image = ctk.CTkImage(
        Image.open("assets/pictures/background.jpeg"), 
        size=(2000, 2000)
    )
    bg_label = ctk.CTkLabel(
        container, 
        image=bg_image, 
        text=""             
    )
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # 2. TITLE
    title = ctk.CTkLabel(
       container, 
        text="Major Events in Precolonial Nigeria", 
        font=("Poppins", 28, "bold"), 
        text_color="black",
        justify="center",
    )
    title.pack(anchor="n", pady=(20, 10))

    # 3. MAIN CONTENT CARD FRAME
    # FIX: Removed fixed width/height and pack_propagate(False) so it flows dynamically
    content_frame = ctk.CTkFrame(
        container, 
        fg_color="#D1C4A9", 
        bg_color="#B5A482", 
        corner_radius=20
    )
    # The bottom padding (pady=(20, 80)) leaves clean structural room for your main file's back button
    content_frame.pack(fill="both", expand=True, padx=40, pady=(10, 80))

    # 4. MIDDLE IMAGE 
    middle_image = ctk.CTkImage(
        Image.open("assets/pictures/28.jpeg"), 
        size=(650, 250) # Sized dynamically to keep text completely readable on screen
    )
    middle_image_label = ctk.CTkLabel(
        content_frame, 
        image=middle_image,
        text=""            
    )
    middle_image_label.pack(pady=(15, 10))

    # 5. DESCRIPTION PARAGRAPH
    history_text = (
        "During the Pre-Colonial Era, various kingdoms and empires flourished with "
        "rich traditions, oral storytelling, and distinct indigenous languages.\n"
        "Here you can add your images, text descriptions, timelines, and anything else "
        "specific to this period!\n\n"
        "Rise of Powerful Kingdoms\n\n"
        "      The Formation of the Oyo Empire led to one of West Africa’s most powerful states.\n"
        "      The Rise of the Benin Kingdom brought advances in governance, trade, and bronze art.\n"
        "      The Establishment of the Kanem-Bornu Empire created a major political and commercial center.\n"
    )
    
    body = ctk.CTkLabel(
        content_frame, 
        text=history_text, 
        font=("Poppins", 14), 
        text_color="#000000", 
        justify="left",
        fg_color="transparent",
        wraplength=800
    )
    body.pack(anchor="w", padx=40, pady=10)