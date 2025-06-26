# Wi-Fi Password Generator
![PyPI version](https://img.shields.io/pypi/v/Wi-FiPasswordGenerator) ![Python Versions](https://img.shields.io/badge/python-3.9%2B-blue) [![Coverage Status](https://coveralls.io/repos/github/heit0r/Wi-FiPasswordGenerator/badge.svg?branch=master)](https://coveralls.io/github/heit0r/Wi-FiPasswordGenerator?branch=master) ![Upload to PyPI](https://github.com/heit0r/Wi-FiPasswordGenerator/actions/workflows/pypi.yml/badge.svg) ![License](https://img.shields.io/github/license/heit0r/Wi-FiPasswordGenerator) [![code style: Ruff](https://img.shields.io/badge/code%20style-Ruff-blueviolet)](https://github.com/astral-sh/ruff) 


![screenshot](https://raw.githubusercontent.com/heit0r/Wi-FiPasswordGenerator/refs/heads/master/assets/screenshot.png) 

**Wi-Fi Password Generator** is a cross-platform Python app for generating secure Wi-Fi passwords of up to 63 characters — the maximum allowed by WPA/WPA2 standards. It features a user-friendly GUI and can optionally generate a QR code for easy scanning and sharing.


## Features

- Generate strong random passwords (up to 63 characters)
- Customize password length and character set
- Cross-platform
- Dark and modern UI with CustomTkinter
- Runs locally and offline
- QR code generation


## Installation

It is recommended to install **Wi-Fi Password Generator** directly from **PyPI**:

Install `python` [according to your operating system](https://www.python.org/downloads/).

`python -m venv .venv` - create a virtual environment

`source .venv/bin/activate` - activate your virtual environment

`pip install --upgrade pip` - upgrade pip

`pip install wi-fipasswordgenerator` - install wi-fipasswordgenerator


## Running the App

After installing, run the app using:

```wpg``` or `wifipg` or even `wifipasswordgenerator`


## Dependencies

These will be installed automatically via pip, but here’s what the project uses:

    customtkinter
    pillow
    qrcode


## License

This project is licensed under the MIT License. See the LICENSE file for details.


## Credits

UI powered by [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

QR code generation by [python-qrcode](https://github.com/lincolnloop/python-qrcode)

Image generation by [Pillow](https://github.com/python-pillow/Pillow)


## Contributing

Pull requests, suggestions and forks are welcome. If you improve the project or add features, feel free to share.

