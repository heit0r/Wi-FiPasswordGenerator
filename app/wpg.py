#!/usr/bin/env python

from tkinter import PhotoImage

import core
import customtkinter

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: blue (default), dark-blue, green

#
# Info Window
#


class InfoWindow(customtkinter.CTkToplevel):
    """Info window with text regarding Easy and Hard modes."""

    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.title("Wi-Fi Password Generator")

        # Icon
        info_image = PhotoImage(file="../assets/icon.png")
        self.iconphoto(False, info_image)

        # Label
        text = """
        Characters like \\, " and ' may be hard to type or copy on some keyboards. Symbols such as # and |, or letters like I, l, and 1 can also be difficult to distinguish in certain fonts, especially non-monospaced ones, or when typing manually.

    Easy mode avoids using these characters, while Hard mode includes all of them.
    """
        self.label = customtkinter.CTkLabel(
            self,
            text=text,
            wraplength=350,
            justify="left",
        )
        self.label.pack(padx=20, pady=30)
        # self.label.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
        self.label.configure(font=customtkinter.CTkFont(family="Verdana", size=18))

        self.button_info_exit = customtkinter.CTkButton(
            self,
            fg_color="#ff6666",
            hover_color="brown",
            text="Exit",
            font=customtkinter.CTkFont(family="Verdana", size=24),
            command=self.destroy,
        )

        self.button_info_exit.pack(padx=20, pady=20)  # pack (place) button


#
# QRCode Window
#


class QRCodeWindow(customtkinter.CTkToplevel):
    """Window to display the generated QRCode."""

    def __init__(self):
        super().__init__()
        self.geometry("400x500")
        self.title("Generated QRCode")

        # Icon
        info_image = PhotoImage(file="../assets/icon.png")
        self.iconphoto(False, info_image)


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("Wi-Fi Password Generator")

        # Label

        self.title_label = customtkinter.CTkLabel(
            master=self,
            text="Wi-Fi Password Generator",  # Title text
            font=customtkinter.CTkFont(
                family="Verdana", size=32
            ),  # Font style and size
        )
        self.title_label.grid(row=0, column=0, pady=50, sticky="n")

        # Center label horizontally

        self.grid_columnconfigure(0, weight=1)

        # Define window icon

        icon_image = PhotoImage(file="../assets/icon.png")
        self.iconphoto(False, icon_image)

        # Define fonts

        self.button_font = customtkinter.CTkFont(family="Verdana", size=26)
        self.textbox_font = customtkinter.CTkFont(family="Verdana", size=16)

        # add widgets to app
        #
        # 1. Textbox: Main no-editable textbox with title "Wi-Fi Password Generator"
        # 2. Textbox: Copyable
        # 3. 3 Buttons + 1 external event
        #   3.1 External event with the last 4 passwords generated.

        # Textbox_regenerate:

        # self.textbox_regenerate = None

        self.textbox_regenerate = customtkinter.CTkTextbox(
            master=self,
            activate_scrollbars=False,
            font=self.textbox_font,
            width=650,
            height=40,
            corner_radius=0,
            wrap="word",
        )

        self.pw_size = 63  # Default password size

        self.textbox_regenerate.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
        self.textbox_regenerate.configure(state="normal")
        self.textbox_regenerate.insert(
            "0.0", f"{core.generate_password(self.pw_size, 0)}\n"
        )  # 0 for Easy characters by default.
        self.textbox_regenerate.configure(state="disabled")

        # Slider

        self.slider = customtkinter.CTkSlider(
            master=self, from_=8, to=63, number_of_steps=55, command=self.slider_event
        )

        self.slider.place(
            relx=0.5,
            rely=0.5,
            anchor=customtkinter.CENTER,
            relwidth=0.82,
            relheight=0.04,
        )

        # Entry

        self.entry = customtkinter.CTkEntry(master=self, placeholder_text="0-63")

        self.entry.place(
            relx=0.15,
            rely=0.57,
            anchor=customtkinter.CENTER,
            relwidth=0.1,
            relheight=0.04,
        )

        self.entry.bind("<Return>", self.enter_text)
        self.entry.bind("<KP_Enter>", self.enter_text)

        # Warning label

        self.warning_label = customtkinter.CTkLabel(
            master=self, text="", text_color="red"
        )
        self.warning_label.place(
            relx=0.3,
            rely=0.57,
            anchor=customtkinter.CENTER,
            relwidth=0.2,
            relheight=0.04,
        )

        # Radio buttons

        # Easy

        self.radio_var = customtkinter.IntVar(value=0)
        self.radiobutton_easy = customtkinter.CTkRadioButton(
            master=self,
            font=self.textbox_font,
            text="Easy characters",
            command=self.radiobutton_event,
            variable=self.radio_var,
            value=0,
        )
        self.radiobutton_easy.place(
            relx=0.2,
            rely=0.66,
            anchor=customtkinter.CENTER,
            relwidth=0.2,
            relheight=0.08,
        )

        # Hard

        self.radiobutton_hard = customtkinter.CTkRadioButton(
            master=self,
            font=self.textbox_font,
            text="Hard characters",
            command=self.radiobutton_event,
            variable=self.radio_var,
            value=1,
        )

        self.radiobutton_hard.place(
            relx=0.2,
            rely=0.72,
            anchor=customtkinter.CENTER,
            relwidth=0.2,
            relheight=0.08,
        )

        # Regenerate

        self.button_regenerate = customtkinter.CTkButton(
            self,
            fg_color="#ff6666",
            hover_color="brown",
            text="Regenerate",
            font=self.button_font,
        )
        self.button_regenerate.place(
            relx=0.2,
            rely=0.9,
            anchor=customtkinter.CENTER,
            relwidth=0.2,
            relheight=0.09,
        )
        self.button_regenerate.bind("<ButtonRelease-1>", self.enter_text)
        # 󱞪 add enter text when someone fills the entry and clicks Regenerate.
        self.button_regenerate.bind("<ButtonRelease-1>", self.regenerate)

        # There's no reason for History button, but let's leave it here for now.

        # self.button2 = customtkinter.CTkButton(self, text="History", font=button_font)
        # self.button2.place(
        #     relx=0.2,
        #     rely=0.9,
        #     anchor=customtkinter.CENTER,
        #     relwidth=0.2,
        #     relheight=0.09,
        # )
        # self.button2.bind("<ButtonRelease-1>", self.button2_history)

        # Copy

        self.button_copy = customtkinter.CTkButton(
            self, text="Copy", font=self.button_font
        )

        self.button_copy.place(
            relx=0.8,
            rely=0.8,
            anchor=customtkinter.CENTER,
            relwidth=0.2,
            relheight=0.09,
        )
        self.button_copy.bind("<ButtonRelease-1>", self.button3_copy)

        # Exit

        self.button_exit = customtkinter.CTkButton(
            self, text="Exit", font=self.button_font
        )
        self.button_exit.place(
            relx=0.8,
            rely=0.9,
            anchor=customtkinter.CENTER,
            relwidth=0.2,
            relheight=0.09,
        )
        self.button_exit.bind("<ButtonRelease-1>", self.button4_exit)

        # QRCode

        self.button_qrcode = customtkinter.CTkButton(
            self, text="QR", font=self.button_font
        )
        self.button_qrcode.place(
            relx=0.75 - 0.002,
            rely=0.7,
            anchor=customtkinter.CENTER,
            relwidth=0.095,
            relheight=0.09,
        )
        self.button_qrcode.bind("<ButtonRelease-1>", self.qrcode)

        self.button_info = customtkinter.CTkButton(
            self, text="Info", font=self.button_font
        )
        self.button_info.place(
            relx=0.85,
            rely=0.7,
            anchor=customtkinter.CENTER,
            relwidth=0.099,
            relheight=0.09,
        )
        self.button_info.bind("<ButtonRelease-1>", self.info)

        # Toplevel Windows

        self.info_window = None  # Create Info Window
        self.qrcode_window = None  # Create QRCode Window

    #
    #
    # ####### METHODS ######
    #
    #

    # Radio buttons

    def radiobutton_event(self):
        print("radiobutton toggled, value:", self.radio_var.get())

    # Slider

    def slider_event(self, slider_value):
        self.pw_size = max(8, min(round(slider_value), 63))  # Input size handling
        self.entry.delete(0, 2)
        self.entry.insert(0, self.pw_size)
        self.entry.delete(2)
        print(self.pw_size)
        self.warning_label.configure(text="")

    # Entry box

    def enter_text(self, event=None):
        self.warning_label.configure(text="")  # clear warning_label
        self.text = self.entry.get()  # will always get 'str'

        try:
            number = int(self.text)
            self.pw_size = max(
                8, min(round(number), 63)
            )  # pw_size will now be text from entry
            print(f"Entry: {self.pw_size}")
            self.slider.set(self.pw_size)
            self.entry.delete(0, 99)
            self.entry.insert(0, self.pw_size)
            self.regenerate(self)  # Regenerate after press Enter
        except ValueError:
            self.warning_label.configure(text="Only numbers are allowed.")

    # Checkbox

    def checkbox_event(self):
        print("checkbox toggled, current value:", self.check_var.get())

    # Regenerate button

    def regenerate(self, event):
        self.textbox_regenerate.destroy()
        self.textbox_regenerate = customtkinter.CTkTextbox(
            master=self,
            activate_scrollbars=False,
            font=self.textbox_font,
            width=650,
            height=40,
            corner_radius=0,
        )
        self.textbox_regenerate.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)
        self.textbox_regenerate.configure(state="normal")
        self.textbox_regenerate.insert(
            "0.0", f"{core.generate_password(self.pw_size, self.radio_var.get())}\n"
        )
        self.textbox_regenerate.configure(state="disabled")
        self.button_copy.configure(text="Copy")  # Copied returns to Copy
        self.warning_label.configure(text="")  # Clear warning_label

    # Copy button

    def button3_copy(self, event):
        print("Copy button clicked")
        self.clipboard_clear()
        self.textbox_regenerate.configure(state="normal")
        password = self.textbox_regenerate.get("0.0", "end").strip()
        self.textbox_regenerate.configure(state="disabled")
        self.clipboard_append(password)
        self.update()
        self.button_copy.configure(text="Copied")
        self.warning_label.configure(text="")  # clear warning_label

    # Exit

    def button4_exit(self, event):
        print("Exiting...")
        self.destroy()

    # QRCode

    def qrcode(self, event):
        if self.qrcode_window is None or not self.qrcode_window.winfo_exists():
            self.qrcode_window = QRCodeWindow()  # create win if its None or destroyed
        else:
            self.qrcode_window.focus()  # if window exists focus it
        print("QRCode")

    # Info

    def info(self, event):
        if self.info_window is None or not self.info_window.winfo_exists():
            self.info_window = InfoWindow()  # create window if its None or destroyed
        else:
            self.info_window.focus()  # if window exists focus it
        print("Info")


app = App()
app.mainloop()
