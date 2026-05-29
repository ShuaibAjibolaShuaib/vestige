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
        text="Major Events in Colonial Nigeria", 
        font=("Poppins", 28, "bold"), 
        text_color="black",
        justify="center",
    )
    title.pack(anchor="n", pady=(20, 10))

    # 3. MAIN CONTENT CARD FRAME
    content_frame = ctk.CTkFrame(
        container, 
        fg_color="#D1C4A9", 
        bg_color="#B5A482", 
        corner_radius=20
    )
    content_frame.pack(fill="both", expand=True, padx=40, pady=(10, 20))

    # 4. MIDDLE IMAGE 
    middle_image = ctk.CTkImage(
        Image.open("assets/pictures/colonial_photo.jpeg"), 
        size=(650, 250) 
    )
    middle_image_label = ctk.CTkLabel(
        content_frame, 
        image=middle_image,
        text=""            
    )
    middle_image_label.pack(pady=(15, 10))

    # 5. DESCRIPTION TEXT
    history_text = (
        "Arrival of the British\n"
        " •  British influence grew through trade, missionary activity,\n"
        "    and military control during the 19th century.\n\n"
        "Establishment of Colonial Rule\n"
        " •  In 1900, the Creation of the Protectorates of Northern and\n"
        "    Southern Nigeria placed much of present-day Nigeria\n"
        "    under direct British administration.\n\n"
        "Amalgamation of Nigeria (1914)"
    )
    
    body = ctk.CTkLabel(
        content_frame, 
        text=history_text, 
        font=("Poppins", 14), 
        text_color="#000000", 
        justify="left",
        fg_color="transparent"
    )
    body.pack(anchor="w", padx=50, pady=(5, 15))

    # 6. FIXED BACK BUTTON POSITIONING
   
   