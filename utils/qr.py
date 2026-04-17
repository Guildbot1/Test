import qrcode

def generate_qr(data):
    img = qrcode.make(data)
    path = "qr.png"
    img.save(path)
    return path
