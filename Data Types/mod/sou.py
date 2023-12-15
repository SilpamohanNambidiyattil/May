import pyqrcode
message = ' Haii Sourettaaaiii'
url = pyqrcode.create(message)
url.svg("sou.svg",scale=8)