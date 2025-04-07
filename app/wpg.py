#!/usr/bin/env python


import core
import customtkinter
from tkinter import PhotoImage

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: blue (default), dark-blue, green


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
        self.gear_font = customtkinter.CTkFont(family="Verdana", size=32)
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

        # self.slider.set(20), better not.

        self.slider.place(
            relx=0.5,
            rely=0.5,
            anchor=customtkinter.CENTER,
            relwidth=0.82,
            relheight=0.04,
        )

        # Entry

        self.entry = customtkinter.CTkEntry(master=self, placeholder_text="0-63")

        # self.entry.focus()

        self.entry.place(
            relx=0.15,
            rely=0.57,
            anchor=customtkinter.CENTER,
            relwidth=0.1,
            relheight=0.04,
        )

        self.entry.bind("<Return>", self.enter_text)
        self.entry.bind("<KP_Enter>", self.enter_text)

        # Warning label.

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
            rely=0.7,
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
            rely=0.76,
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
        self.button_regenerate.bind("<ButtonRelease-1>", self.button1_regenerate)

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

        self.button_conf = customtkinter.CTkButton(self, text="⚙️", font=self.gear_font)
        self.button_conf.place(
            relx=0.75 - 0.002,
            rely=0.7,
            anchor=customtkinter.CENTER,
            relwidth=0.095,
            relheight=0.09,
        )
        self.button_conf.bind("<ButtonRelease-1>", self.configure)

        self.button_help = customtkinter.CTkButton(
            self, text="?", font=self.button_font
        )
        self.button_help.place(
            relx=0.85,
            rely=0.7,
            anchor=customtkinter.CENTER,
            relwidth=0.099,
            relheight=0.09,
        )
        self.button_help.bind("<ButtonRelease-1>", self.help)

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
        except ValueError:
            self.warning_label.configure(text="Only numbers are allowed.")

    # Checkbox

    def checkbox_event(self):
        print("checkbox toggled, current value:", self.check_var.get())

    # Regenerate button

    def button1_regenerate(self, event):
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
        self.button_copy.configure(text="Copy")
        # self.warning_label.configure(text="")

    # Copy button

    def button3_copy(self, event):
        print("Copy button clicked")
        self.clipboard_clear()
        self.textbox_regenerate.configure(state="normal")
        password = self.textbox_regenerate.get("0.0", "end").strip()
        self.textbox_regenerate.configure(state="disabled")
        self.clipboard_append(password)
        # print(f"Password copied: {password}") # better not disclose this.
        self.update()
        self.button_copy.configure(text="Copied")
        self.warning_label.configure(text="")  # clear warning_label

    # Exit

    def button4_exit(self, event):
        print("Exiting...")
        self.destroy()

    # Config

    def configure(self, event):
        print("Configure")

    # Help/Info

    def help(self, event):
        print("Help")


app = App()
app.mainloop()
