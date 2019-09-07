import pytest

from gdrive_link_transformer.gdrive_direct_link import is_sharing_link, convert_to_direct_link


def test_link_detection():
    assert is_sharing_link('https://drive.google.com/file/d/abcdef12345-6_qwe/view?usp=drivesdk')
    assert is_sharing_link('https://drive.google.com/open?id=abcdef12345-6_qwe')
    assert not is_sharing_link('https://drive.google.com/')
    assert not is_sharing_link('https://yandex.ru/open?id=abcdef12345-6_qwe')


def test_creates_link():
    assert convert_to_direct_link('https://drive.google.com/file/d/abcdef12345-6_qwe/view?usp=drivesdk') == 'https://drive.google.com/uc?export=download&id=abcdef12345-6_qwe'
    assert convert_to_direct_link('https://drive.google.com/open?id=abcdef12345-6_qwe') == 'https://drive.google.com/uc?export=download&id=abcdef12345-6_qwe'
