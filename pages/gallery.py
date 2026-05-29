import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow


class ScrollableImageGallery:
    def __init__(self, root):
        self.root = root
        self.root.title("Scrollable Gallery")
        self.root.geometry("844x896")
        self.root.resizable(False, False)

        # Main Canvas for scrolling
        self.canvas = tk.Canvas(root, width=844, height=896, bg="#f0f0f0")
        self.scrollbar = ttk.Scrollbar(
            root, orient="vertical", command=self.canvas.yview)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Inner frame to hold all content
        self.inner_frame = tk.Frame(self.canvas, bg="#f0f0f0")
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")

        # Bind scroll
        self.inner_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<MouseWheel>", self.on_mousewheel)  # Windows
        self.canvas.bind("<Button-4>", self.on_mousewheel)    # Linux scroll up
        # Linux scroll down
        self.canvas.bind("<Button-5>", self.on_mousewheel)

        self.setup_ui()

    def setup_ui(self):
        # ====================== TOP HEADER ======================
        header_frame = tk.Frame(self.inner_frame, bg="#ffffff", height=100)
        header_frame.pack(fill="x", padx=10, pady=10)
        header_frame.pack_propagate(False)

        # Two-line text (Italic, size 18) - Top Left
        text_label = tk.Label(
            header_frame,
            text="Discover Amazing\nCollections",
            font=("Arial", 18, "italic"),
            bg="#ffffff",
            anchor="w",
            justify="left"
        )
        text_label.pack(side="left", padx=15, pady=15)

        # Search Bar - Top Right
        search_frame = tk.Frame(header_frame, bg="#ffffff")
        search_frame.pack(side="right", padx=15, pady=20)

        self.search_var = tk.StringVar()
        search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Arial", 12),
            width=25,
            relief="solid",
            bd=1
        )
        search_entry.pack(side="left", padx=(0, 5))
        search_entry.insert(0, "Search images...")

        # Optional: Search button
        search_btn = tk.Button(search_frame, text="🔍",
                               font=("Arial", 12), width=3)
        search_btn.pack(side="left")

        # ====================== IMAGES SECTION ======================
        images_frame = tk.Frame(self.inner_frame, bg="#f0f0f0")
        images_frame.pack(fill="x", padx=20, pady=10)

        # Two columns
        col1 = tk.Frame(images_frame, bg="#f0f0f0")
        col2 = tk.Frame(images_frame, bg="#f0f0f0")
        col1.pack(side="left", padx=(0, 15))
        col2.pack(side="left")

        # Image paths (Replace with your actual image paths)
        image_paths = [f"assets/pictures/{i}.jpg" for i in range(
            1, 12)]  # Example

        # Column 1: 6 images
        for i in range(6):
            self.add_image_to_column(col1, image_paths[i], i)

        # Column 2: 5 images
        for i in range(6, 11):
            self.add_image_to_column(col2, image_paths[i], i)

    def add_image_to_column(self, parent, img_path, index):
        frame = tk.Frame(parent, bg="#ffffff", relief="solid", bd=1)
        frame.pack(pady=12)

        try:
            # Load and resize image
            img = Image.open(img_path)
            img = img.resize((327, 457), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            label = tk.Label(frame, image=photo, bg="#ffffff")
            label.image = photo  # Keep reference
            label.pack()

            # Optional: Caption
            caption = tk.Label(frame, text=f"Image {index+1}", bg="#ffffff",
                               font=("Arial", 10))
            caption.pack(pady=5)

        except Exception as e:
            # Placeholder if image not found
            placeholder = tk.Label(frame, text=f"Image {index+1}\n(327×457)",
                                   width=40, height=40, bg="#ddd", relief="solid")
            placeholder.pack(pady=10, padx=10)

    def on_frame_configure(self, event=None):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mousewheel(self, event):
        if event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "units")


# ====================== RUN THE APP ======================
if __name__ == "__main__":
    root = tk.Tk()
    app = ScrollableImageGallery(root)
    root.mainloop()
