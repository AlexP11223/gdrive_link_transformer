Generates direct Google Drive link (`https://drive.google.com/uc?export=download&id=<ID>`) from standard sharing links (`https://drive.google.com/file/d/<ID>/view` or `https://drive.google.com/open?id=<ID>`).

The script takes the link from the clipboard, checks if it is a Google Drive sharing link and copies direct link to the clipboard.

# Usage

Requirements:

- Python 3.7+
- [pipenv](https://pipenv.readthedocs.io/en/latest/)

Install dependencies by executing `pipenv install`. 

Use PyTest to run tests: `pipenv run python -m pytest -v test.py` or in PyCharm.

Use `pipenv run gdrive_direct_link.py` to run the script when you have a Google Drive sharing link in the clipboard. 

# TODO

- Create binaries.  
