Generates direct Google Drive links (`https://drive.google.com/uc?export=download&id=<ID>`) from standard sharing links (`https://drive.google.com/file/d/<ID>/view` or `https://drive.google.com/open?id=<ID>`).

The script takes the link from the clipboard, checks if it is a Google Drive sharing link and copies direct link to the clipboard, shows notification.

![Windows 10 screenshot](https://i.imgur.com/MiBGXFO.png)

![Pop_OS 19.10 screenshot](https://i.imgur.com/Mvhy85a.png)

Also it can be used as a normal CLI app taking the link from the arguments and outputting the result.

![Terminal screenshot](https://i.imgur.com/cq7kx74.png)

Should work on Windows, Linux and (not tested) Mac OS.

# Usage

Download the binaries for your OS from the [Releases](https://github.com/AlexP11223/gdrive_link_transformer/releases) page or see the section below to run from source code.

For Linux you may need to install one of the packages listed here https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error for clipboard management, such as `sudo apt-get install xclip`.

Run `gdrive-direct-link` (`gdrive-direct-link.exe` for Windows) when you have a Google Drive sharing link in the clipboard, or `gdrive-direct-link https://drive.google.com/file/d/qwe123456/view` in terminal.

# Running from source code

Requirements:

- Python 3.7+
- [poetry](https://poetry.eustace.io/docs/)

Install dependencies by executing `poetry install`. For Linux use `poetry install --extras dbus` (unless you need just the CLI mode).

Use PyTest to run tests: `poetry run pytest` or in PyCharm.

Use `poetry run gdrive-direct-link` to run the script as described in the Usage section.

## Building binary

Run `poetry run pyinstaller gdrive-direct-link.spec`

The result will be in the `dist` dir: `dist/gdrive-direct-link/gdrive-direct-link`
