import customtkinter as ctk

class Food(ctk.CTk):
    # --- Color Palette Hex Codes as Class Constants ---
    COLOR_HEADER_BLUE = "#1d5b96"
    COLOR_TEXT_BROWN = "#8a3324"
    COLOR_TEXT_DARK_BROWN = "#5c2d25"
    COLOR_CARD_BG = "#f4f7fc"
    COLOR_DIVIDER_BLUE = "#bfdbfe"
    COLOR_PLACEHOLDER_BG = "#e2e8f0"
    COLOR_PLACEHOLDER_TEXT = "#94a3b8"

    def __init__(self):
        super().__init__()
        
        # Initialize the main window configurations
        self.title("Food: Then VS Now")
        self.geometry("1000x750")
        
        # Set the theme and main window background color
        ctk.set_appearance_mode("Light")
        self.configure(fg_color="#f3f4f6") 

        # Initialize database simulation variables
        self.init_database()
        
        # Build the user interface
        self.create_widgets()

    def init_database(self):
        """Initializes database simulation variables as instance attributes."""
        self.db_page_title = None           
        self.db_page_description = None     

        # 1. Traditional Column Data
        self.db_trad_clothing_title = None  
        self.db_trad_clothing_desc_1 = None 
        self.db_trad_clothing_desc_2 = None 
        self.db_trad_clothing_image = None  

        self.db_trad_acc_title = None       
        self.db_trad_acc_desc = None        
        self.db_trad_acc_image = None       

        self.db_trad_foot_title = None      
        self.db_trad_foot_desc = None        
        self.db_trad_foot_image = None       

        # 2. Modern Column Data
        self.db_mod_clothing_title = None   
        self.db_mod_clothing_desc_1 = None  
        self.db_mod_clothing_desc_2 = None  
        self.db_mod_clothing_image = None   

        self.db_mod_acc_title = None        
        self.db_mod_acc_desc = None         
        self.db_mod_acc_image = None        

        self.db_mod_foot_title = None      
        self.db_mod_foot_desc = None         
        self.db_mod_foot_image = None        

    def build_era_column(self, parent_frame, c_title, c_desc1, c_desc2, c_img, a_title, a_desc, a_img, f_title, f_desc, f_img):
        """Creates a leveled column layout containing clothing, accessories, and footwear blocks."""
        parent_frame.grid_columnconfigure(0, weight=1)
        
        # 3 uniform grid rows keep everything completely matched across the split screen
        parent_frame.grid_rowconfigure(0, weight=1, uniform="Maindish_row") 
        parent_frame.grid_rowconfigure(1, weight=1, uniform="snacks_row") 


        # ---------------------------------------------------------
        # 1. Main dish BLOCK
        # ---------------------------------------------------------
        dish_card = ctk.CTkFrame(parent_frame, fg_color=self.COLOR_CARD_BG, corner_radius=12, border_width=1, border_color="#eff6ff")
        dish_card.grid(row=0, column=0, sticky="nsew", pady=(0, 25))
        
        ctk.CTkLabel(
            dish_card, 
            text=c_title if c_title is not None else "Main Dish [Null]", 
            font=("Arial", 16, "bold"), text_color=self.COLOR_HEADER_BLUE
        ).pack(anchor="w", padx=15, pady=(15, 10))

        c_split_box = ctk.CTkFrame(dish_card, fg_color="transparent")
        c_split_box.pack(fill="x", padx=15, pady=(0, 10))

        if c_img is None:
            img_placeholder = ctk.CTkFrame(c_split_box, width=110, height=160, fg_color=self.COLOR_PLACEHOLDER_BG, corner_radius=8)
            img_placeholder.pack(side="left", padx=(0, 15))
            img_placeholder.pack_propagate(False)
            ctk.CTkLabel(img_placeholder, text="No Image\n[Null]", text_color=self.COLOR_PLACEHOLDER_TEXT, font=("Arial", 11, "bold")).pack(expand=True)

        ctk.CTkLabel(
            c_split_box, 
            text=c_desc1 if c_desc1 is not None else "Main dish overview details are currently unpopulated in database rows.",
            font=("Arial", 12, "bold"), text_color=self.COLOR_TEXT_DARK_BROWN, wraplength=260, justify="left"
        ).pack(side="left", fill="both", expand=True, anchor="n")

        ctk.CTkLabel(
            dish_card, 
            text=c_desc2 if c_desc2 is not None else "Extended design description block missing from the database record [Null].",
            font=("Arial", 12, "bold"), text_color=self.COLOR_TEXT_DARK_BROWN, wraplength=410, justify="left"
        ).pack(fill="both", expand=True, padx=15, pady=(10, 15))

        # ---------------------------------------------------------
        # 2. SNACKS BLOCK
        # ---------------------------------------------------------
        acc_card = ctk.CTkFrame(parent_frame, fg_color=self.COLOR_CARD_BG, corner_radius=12, border_width=1, border_color="#eff6ff")
        acc_card.grid(row=1, column=0, sticky="nsew", pady=(0, 25))
        
        ctk.CTkLabel(
            acc_card, 
            text=a_title if a_title is not None else "Snacks [Null]", 
            font=("Arial", 16, "bold"), text_color=self.COLOR_HEADER_BLUE
        ).pack(pady=(15, 10))

        a_split_box = ctk.CTkFrame(acc_card, fg_color="transparent")
        a_split_box.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        if a_img is None:
            acc_img_placeholder = ctk.CTkFrame(a_split_box, width=110, height=160, fg_color=self.COLOR_PLACEHOLDER_BG, corner_radius=8)
            acc_img_placeholder.pack(side="left", padx=(0, 15))
            acc_img_placeholder.pack_propagate(False)
            ctk.CTkLabel(acc_img_placeholder, text="No Image\n[Null]", text_color=self.COLOR_PLACEHOLDER_TEXT, font=("Arial", 11, "bold")).pack(expand=True)

        ctk.CTkLabel(
            a_split_box, 
            text=a_desc if a_desc is not None else "Snack usage summary text is unpopulated inside the database [Null].",
            font=("Arial", 12, "bold"), text_color=self.COLOR_TEXT_DARK_BROWN, wraplength=280, justify="left"
        ).pack(side="left", fill="both", expand=True, anchor="n")


    def create_widgets(self):
        """Generates layout layout, main containers, and triggers column builds."""
        # Main Container (Scrollable Frame)
        main_container = ctk.CTkScrollableFrame(
            self, 
            fg_color="white", 
            corner_radius=16, 
            border_width=1, 
            border_color="#e5e7eb",
            scrollbar_fg_color="transparent",        
            scrollbar_button_color="#cbd5e1",       
            scrollbar_button_hover_color="#94a3b8"  
        )
        main_container.pack(padx=30, pady=30, fill="both", expand=True)

        # Close Button (X) top right
        close_button = ctk.CTkButton(
            main_container, 
            text="×", 
            font=("Arial", 24, "bold"), 
            text_color="#9ca3af", 
            hover_color="white", 
            fg_color="transparent", 
            width=30, 
            height=30,
            command=self.quit
        )
        close_button.pack(anchor="ne", padx=10, pady=5)

        # Dynamic Header Section
        header_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        header_frame.pack(fill="x", padx=40, pady=(0, 20))

        title_label = ctk.CTkLabel(
            header_frame, 
            text=self.db_page_title if self.db_page_title is not None else "Title Section [Null]", 
            font=("Arial", 26, "bold"), 
            text_color=self.COLOR_HEADER_BLUE
        )
        title_label.pack(pady=(10, 5))

        desc_label = ctk.CTkLabel(
            header_frame, 
            text=self.db_page_description if self.db_page_description is not None else "Main page description text is currently unassigned in the database [Null].", 
            font=("Arial", 13, "bold"), 
            text_color=self.COLOR_TEXT_BROWN, 
            wraplength=850, 
            justify="center"
        )
        desc_label.pack(pady=5)

        # Split Columns Layout Frame
        columns_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        columns_frame.pack(fill="both", expand=True, padx=40, pady=(10, 30))

        columns_frame.grid_columnconfigure(0, weight=1, uniform="col")
        columns_frame.grid_columnconfigure(1, weight=0) 
        columns_frame.grid_columnconfigure(2, weight=1, uniform="col")
        columns_frame.grid_rowconfigure(0, weight=1)

        # Central Vertical Line
        vertical_line = ctk.CTkFrame(columns_frame, width=1, fg_color=self.COLOR_DIVIDER_BLUE)
        vertical_line.grid(row=0, column=1, sticky="ns", padx=20)

        # Left Hand Side Container (Traditional)
        left_column_container = ctk.CTkFrame(columns_frame, fg_color="transparent")
        left_column_container.grid(row=0, column=0, sticky="nsew")

        self.build_era_column(
            parent_frame=left_column_container,
            c_title=self.db_trad_clothing_title,
            c_desc1=self.db_trad_clothing_desc_1,
            c_desc2=self.db_trad_clothing_desc_2,
            c_img=self.db_trad_clothing_image,
            a_title=self.db_trad_acc_title,
            a_desc=self.db_trad_acc_desc,
            a_img=self.db_trad_acc_image,
            f_title=self.db_trad_foot_title,
            f_desc=self.db_trad_foot_desc,
            f_img=self.db_trad_foot_image
        )

        # Right Hand Side Container (Modern)
        right_column_container = ctk.CTkFrame(columns_frame, fg_color="transparent")
        right_column_container.grid(row=0, column=2, sticky="nsew")

        self.build_era_column(
            parent_frame=right_column_container,
            c_title=self.db_mod_clothing_title,
            c_desc1=self.db_mod_clothing_desc_1,
            c_desc2=self.db_mod_clothing_desc_2,
            c_img=self.db_mod_clothing_image,
            a_title=self.db_mod_acc_title,
            a_desc=self.db_mod_acc_desc,
            a_img=self.db_mod_acc_image,
            f_title=self.db_mod_foot_title,
            f_desc=self.db_mod_foot_desc,
            f_img=self.db_mod_foot_image
        )


# --- Application Entry Point ---
if __name__ == "__main__":
    app = Food()
    app.mainloop()