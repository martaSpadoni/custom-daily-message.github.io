import qrcode
import os
from qrcode.image.styledpil import StyledPilImage

# Configura il tuo URL principale
BASE_URL = "https://martaspadoni.github.io/custom-daily-message.github.io/days/"

# Crea cartella per i QR Code
output_dir = "qr_codes"
os.makedirs(output_dir, exist_ok=True)

# Genera un QR per ogni giorno
for day in range(1, 366):  # 365 giorni (o 366 per anno bisestile)
    day_filename = f"{day:03}.html"  # 001.html, 002.html, ecc.
    full_url = f"{BASE_URL}{day_filename}"

    # qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    # qr.add_data(full_url)
    # qr = qr.make_image(image_factory=StyledPilImage, embeded_image_path="C:\\Users\\m.spadoni\\Desktop\\Personali\\custom-daily-message.github.io\\res\\images\\hearts.jpg")

    qr = qrcode.make(full_url)
    
    # Salva il QR Code come immagine
    qr_path = os.path.join(output_dir, f"{day:03}.png")
    qr.save(qr_path)

    print(f"QR Code generato: {qr_path}")