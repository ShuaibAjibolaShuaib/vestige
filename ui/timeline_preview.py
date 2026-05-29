import customtkinter as ctk

# timleine preview function


def create_timeline_preview(parent, title, subheading, command=None):
    card = ctk.CTkFrame(
        parent,
        height=150,
        corner_radius=20,
        fg_color="#2D5B94",
    )
    card.pack(fill="x", pady=10)
    card.pack_propagate(False)

    content = ctk.CTkFrame(card, fg_color="transparent")
    content.pack(fill="both", expand=True, padx=15, pady=15)

    left_side = ctk.CTkFrame(content, fg_color="transparent")
    left_side.pack(side="left", fill="y")

    circle = ctk.CTkLabel(
        left_side,
        text="●",
        font=("Arial", 40),
        text_color="white"
    )
    circle.pack(side="left", pady=(0, 12))

    text_frame = ctk.CTkFrame(content, fg_color="transparent")
    text_frame.pack(side="left")

    title_label = ctk.CTkLabel(
        text_frame,
        text=title,
        font=("Konkhmer Sleokchher", 25, "bold"),
        text_color="white"
    )
    title_label.pack(anchor="w")

    # subheading
    subheading_label = ctk.CTkLabel(
        text_frame,
        text=subheading,
        font=("Konkhmer Sleokchher", 20),
        text_color="white"
    )
    subheading_label.pack(anchor="w", pady=(5, 0))

    if command:
        widgets = [
            card,
            content,
            left_side,
            circle,
            text_frame,
            title_label,
            subheading_label
        ]
        for widget in widgets:
            widget.bind("<Button-1>", lambda e: command())

    return card
