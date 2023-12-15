import pyqrcode
message = ' Hai kichu, How are You'
url = pyqrcode.create(message)
url.svg("myqrcode.svg",scale=8)