import qrcode
from textwrap import fill

# data you wanna show in your qrcode
data = "https://www.youtube.com/channel/UC9jC6JioHpjwZtENC6YUPNQ?sub_confirmation=1"


qr = qrcode.QRCode(version=1, box_size=15, border=5)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

img.save("C:/qrcode/qrcode.png")
