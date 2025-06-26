import qrcode

data = input("Enter text or URL to generate QR code: ")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qrcode.png")

print("QR Code successfully saved as my_qrcode.png")


# Need to install (pip install qrcode[pil])