# @pytest.fixture 
# def interface():
#     return App


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


