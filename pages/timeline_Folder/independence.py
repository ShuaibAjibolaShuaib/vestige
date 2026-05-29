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
        text="Major Events in Independent Nigeria", 
        font=("Poppins", 28, "bold"), 
        text_color="black",
        justify="center",
    )
    title.pack(anchor="n", pady=(20, 10))

    # 3. MAIN CONTENT CARD FRAME
    content_frame = ctk.CTkFrame(
        container, 
        fg_color="#EAEAEA",  # Soft light grey background matching the image frame border
        bg_color="#D1C4A9", 
        corner_radius=20
    )
    content_frame.pack(fill="both", expand=True, padx=40, pady=(10, 80))

    # 4. MIDDLE IMAGE 
    middle_image = ctk.CTkImage(
        Image.open("assets/pictures/30.jpeg"),  # Replace with your actual image path
        size=(650, 400) # Increased height to better fit the proportions of the newspaper/photo
    )
    middle_image_label = ctk.CTkLabel(
        content_frame, 
        image=middle_image,
        text=""            
    )
    middle_image_label.pack(pady=(20, 15))

    # 5. DESCRIPTION PARAGRAPH
    history_text = (
        "On October 1, 1960, Nigeria officially gained full independence from Great Britain, "
        "marking the birth of a proud sovereign nation.\n"
        "The era brought monumental changes, constitutional developments, and a new dawn of self-governance.\n\n"
        "Key Milestones of the Era\n\n"
        "      October 1, 1960: The hoisting of the green-white-green national flag and lowering of the Union Jack.\n"
        "      1963: Nigeria becomes a Federal Republic, completely severing colonial ties to the British Crown.\n"
        "      National Sovereignty: The establishment of an independent parliament and local leadership under Prime Minister Tafawa Balewa.\n"
    )
    
    body = ctk.CTkLabel(
        content_frame, 
        text=history_text, 
        font=("Poppins", 14), 
        text_color="#000000", 
        justify="left",
        fg_color="transparent"
    )
    body.pack(anchor="w", padx=40, pady=10)