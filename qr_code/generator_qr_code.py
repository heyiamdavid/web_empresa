import qrcode

texto = ""
qr = qrcode.QRCode(version=1,
                   box_size=10,
                   border=2)

qr.add_data(texto)
qr.make(fit=True)

import_qr = qr.make_image(fill_color="black", 
                          back_color="white")
import_qr.save("assets/qr_image/qr_image.png")