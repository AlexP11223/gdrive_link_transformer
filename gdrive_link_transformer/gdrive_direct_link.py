import argparse
import sys
import os
from urllib.parse import urlparse, parse_qs


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

def resource_dir():
    RESOURCE_DIR_NAME = 'resources'
    file_dir_path = os.path.dirname(os.path.realpath(__file__))
    if os.path.isdir(os.path.join(file_dir_path, RESOURCE_DIR_NAME)):
        return os.path.join(file_dir_path, RESOURCE_DIR_NAME)
    return os.path.normpath(os.path.join(file_dir_path, '..', RESOURCE_DIR_NAME))


def main():
    parser = argparse.ArgumentParser(description='Generate direct Google Drive links from standard sharing links.',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog='''Example:
    gdrive_direct_link.py https://drive.google.com/file/d/qwe123456/view
    gdrive_direct_link.py https://drive.google.com/open?id=qwe123456
    gdrive_direct_link.py # use clipboard''')
    parser.add_argument('url', nargs='?', default=None)

    args = parser.parse_args()

    if args.url:
        if not is_sharing_link(args.url):
            sys.exit(1)
        converted_url = convert_to_direct_link(args.url)
        print(converted_url)
    else:
        import pyperclip
        from plyer import notification
        from plyer.utils import platform
        content = pyperclip.paste()
        if is_sharing_link(content):
            converted_url = convert_to_direct_link(content)
            pyperclip.copy(converted_url)
            notification.notify(
                title='Google Drive direct link',
                app_icon=os.path.join(resource_dir(), 'icon') + ('.ico' if platform == "win" else '.png'),
                message='Direct Google Drive link copied to clipboard: ' + converted_url)


if __name__ == '__main__':
    main()
