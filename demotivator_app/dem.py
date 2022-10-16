from simpledemotivators import Demotivator


def create_dem(top_text: str, bottom_text: str, pic: str) -> bytes:
    pic = bytearray(pic, encoding='ISO-8859-1')
    with open('dem.png', 'wb') as png:
        png.write(pic)
    dem = Demotivator(top_text, bottom_text)
    dem.create('dem.png')
    with open('demresult.jpg', 'rb') as png:
        return png.read()
