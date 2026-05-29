import tkinter as tk
from tkinter import ttk

class CultureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Culture Explorer Dashboard")
        self.root.geometry("550x700")
        self.root.configure(bg="white")

        # Configure universal styles for a modern look
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Card.TFrame", background="white", relief="solid", borderwidth=1)

        # --- HEADER SECTION ---
        self.create_header()

        # --- SCROLLABLE CONTAINER ---
        # Main canvas to allow scrolling
        self.canvas = tk.Canvas(self.root, bg="white", highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas, bg="white")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw", width=510)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True, padx=15, pady=5)
        self.scrollbar.pack(side="right", fill="y")

        # --- CARD DATA ---
        cards_data = [
            {"title": "Fashion", "desc": "From traditional attire\nto modern trends"},
            {"title": "Food", "desc": "From homemade\nrecipes to fast paced\ndining"},
            {"title": "Comms", "desc": "From handwritten\nletters to instant\nmessaging"},
            {"title": "Entertainment", "desc": "From moonlight stories\nto digital streaming"}
        ]

        for data in cards_data:
            self.create_card(self.scrollable_frame, data)

    def create_header(self):
        header_frame = tk.Frame(self.root, bg="white")
        header_frame.pack(fill="x", padx=20, pady=(20, 10))

        quote_label = tk.Label(
            header_frame, 
            text="“Exploring how the past shapes the present\nand what we risk losing...”", 
            font=("Arial", 11, "italic"), 
            fg="#555555",
            bg="white",
            justify="left"
        )
        quote_label.pack(side="left", anchor="w")

        # Search Bar
        search_frame = tk.Frame(header_frame, bg="#F2F2F2", bd=0)
        search_frame.pack(side="right", anchor="ne", pady=5)
        
        search_entry = tk.Entry(
            search_frame, 
            font=("Arial", 11), 
            bg="#F2F2F2", 
            fg="black", 
            bd=0, 
            width=15,
            insertbackground="black"
        )
        search_entry.insert(0, "Search")
        search_entry.pack(padx=8, pady=5)

    def create_card(self, parent, data):
        # Card Outer container
        card = tk.Frame(parent, bg="white", highlightbackground="#E0E0E0", highlightcolor="#E0E0E0", highlightthickness=1, height=130)
        card.pack(fill="x", pady=8)
        card.pack_propagate(False)

        # 1. Left Photo Space
        img_label = tk.Label(card, text="[ Photo ]", width=18, bg="#EAEAEA", fg="gray", font=("Arial", 11))
        img_label.pack(side="left", fill="y")

        # Divider 1
        div1 = tk.Frame(card, width=1, bg="#E0E0E0")
        div1.pack(side="left", fill="y")

        # 2. Middle Title & Icon Space
        mid_section = tk.Frame(card, bg="white", width=110)
        mid_section.pack(side="left", fill="y", padx=10)
        mid_section.pack_propagate(False)

        tk.Label(mid_section, text=data["title"], font=("Arial", 15, "bold"), fg="#707070", bg="white").pack(anchor="w", pady=(15, 2))
        tk.Label(mid_section, text="[Icon]", font=("Arial", 10), fg="gray", bg="#F5F5F5", width=6, height=2).pack(anchor="w")

        # Divider 2
        div2 = tk.Frame(card, width=1, bg="#E0E0E0")
        div2.pack(side="left", fill="y")

        # 3. Right Description & Heart
        right_section = tk.Frame(card, bg="white")
        right_section.pack(side="left", fill="both", expand=True, padx=15)

        desc_label = tk.Label(right_section, text=data["desc"], font=("Arial", 12, "bold"), fg="#7A4F43", bg="white", justify="left")
        desc_label.pack(side="left", anchor="w")

        heart_label = tk.Label(right_section, text="♡", font=("Arial", 18), fg="#404040", bg="white", cursor="hand2")
        heart_label.pack(side="right", anchor="se", pady=10, padx=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = CultureApp(root)
    root.mainloop()