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
        text="Digital Era", 
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
        Image.open("assets/pictures/94.jpg"),  # Replace with your actual image path
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
        "Technology in the Digital Age\n\n "
        "Technology has transformed the way people live, communicate, learn, and preserve culture. In today’s digital.\n"
        "age, devices such as smartphones, computers, and the internet make information easily accessible and.\n\n"
        "connect people across the world within seconds. Social media platforms, digital libraries, and online learning\n"
        "systems have changed how knowledge is shared and how societies interact\n"
        "In Nigeria and many other parts of the world, technology has improved communication, business\n"
        "healthcare, transportation, and education. Tasks that once required physical effort or long-distance travel can\n"
        "now be completed online through digital platforms\n"
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