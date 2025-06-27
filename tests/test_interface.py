import customtkinter
import pytest
from wi_fipasswordgenerator import wpg

def test_imports():
    from tkinter import PhotoImage
    from wi_fipasswordgenerator import core
    from wi_fipasswordgenerator import wpg
    import customtkinter
    import os
    import qrcode
 
    assert PhotoImage
    assert core
    assert customtkinter
    assert os
    assert qrcode
    assert wpg

@pytest.fixture 
def interface():
    return wpg.InfoWindow

def test_infowindow():
    root = customtkinter.CTk()
    root.withdraw()

    info_win = wpg.InfoWindow()

    assert isinstance(info_win, customtkinter.CTkToplevel)

