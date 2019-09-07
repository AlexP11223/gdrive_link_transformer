from urllib.parse import urlparse, parse_qs

import pyperclip
from plyer import notification


def is_sharing_link(url):
    parsed_url = urlparse(url)
    return parsed_url.hostname == 'drive.google.com' \
           and any(part in parsed_url.path.split('/') for part in ['file', 'open'])


def direct_link(id):
    return 'https://drive.google.com/uc?export=download&id=' + id


def convert_to_direct_link(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')
    if 'file' in path_parts:
        return direct_link(path_parts[3])
    if 'open' in path_parts:
        return direct_link(parse_qs(parsed_url.query)['id'][0])

    return None


def main():
    content = pyperclip.paste()
    if is_sharing_link(content):
        url = convert_to_direct_link(content)
        pyperclip.copy(url)
        notification.notify(
            title='Google Drive link',
            message='Direct Google Drive link copied to clipboard: ' + url)


if __name__ == '__main__':
    main()
