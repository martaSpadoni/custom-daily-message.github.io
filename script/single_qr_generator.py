import qrcode
import os
from qrcode.image.styledpil import StyledPilImage

# Configura il tuo URL principale
BASE_URL = "https://i.postimg.cc/VvJQy1Ly/Felice-anno-nuovo.png"

# Crea cartella per i QR Code
output_dir = "card"
os.makedirs(output_dir, exist_ok=True)

qr = qrcode.make(BASE_URL)

# Salva il QR Code come immagine
qr_path = os.path.join(output_dir, f"{day:03}.png")
qr.save(qr_path)

print(f"QR Code generato: {qr_path}")