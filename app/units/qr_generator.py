import qrcode

def create_qr(data):

    img = qrcode.make(data)

    img.save("qr.png")