Generates direct Google Drive link (`https://drive.google.com/uc?export=download&id=<ID>`) from standard sharing links (`https://drive.google.com/file/d/<ID>/view` or `https://drive.google.com/open?id=<ID>`).

The script takes the link from the clipboard, checks if it is a Google Drive sharing link and copies direct link to the clipboard.

Also it can be used as a normal CLI app taking the link from the arguments and outputting the result.

# Usage

Requirements:

- Python 3.7+
- [poetry](https://poetry.eustace.io/docs/)

Install dependencies by executing `poetry install`. 

For Linux you may also need to install one of the packages listed here https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error for clipboard management, such as `sudo apt-get install xclip`.

Use PyTest to run tests: `poetry run pytest` or in PyCharm.

Use `poetry run gdrive-direct-link` to run the script when you have a Google Drive sharing link in the clipboard, or `poetry run gdrive-direct-link https://drive.google.com/file/d/qwe123456/view`  

# TODO

- Create binaries.  
