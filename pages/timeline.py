import customtkinter as ctk

from ui.timeline_preview import create_timeline_preview
from pages.timelinefolder_copy.colonial import TimeColonialPage


class TimelinePage(ctk.CTkFrame):

    def __init__(self, parent, navigate):
        super().__init__(parent)

        self.pack(fill="both", expand=True)

        title = ctk.CTkLabel(
            self,
            text="Historical Timeline",
            font=("Konkhmer Sleokchher", 30, "bold"),
            text_color="#333"
        )
        title.pack(anchor="w", padx=25, pady=(20, 10))

        scroll_frame = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )

        scroll_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        # timeline cards

        create_timeline_preview(
            scroll_frame,
            "Pre-Colonial Era",
            "Traditional kingdoms, trade routes and oral history.",
        )

        create_timeline_preview(
            scroll_frame,
            "Colonial Era",
            "British rule reshaped politics and education.",
            command=lambda: navigate(
                TimeColonialPage, navigate=navigate, back_page=TimelinePage)
        )

        create_timeline_preview(
            scroll_frame,
            "Independence (1960)",
            "Nigeria gained independence from Britain."
        )

        create_timeline_preview(
            scroll_frame,
            "Digital Age",
            "Technology transformed communication and culture."
        )

        create_timeline_preview(
            scroll_frame,
            "Future Nigeria",
            "Preserving traditions in a modern world."
        )
