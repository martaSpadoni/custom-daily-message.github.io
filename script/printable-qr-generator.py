import os
import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from PIL import Image

# Configurazione
OUTPUT_FOLDER = "qr_codes"  # Cartella per salvare i QR
PDF_FILE = "qr_codes_reprint.pdf"   # File PDF finale
QR_PER_PAGE = 48  # Numero di QR per pagina

# Funzione per creare il PDF con i QR Code
def create_pdf_with_qrs(qr_paths, pdf_file, qr_per_page):
    c = canvas.Canvas(pdf_file, pagesize=A4)
    page_width, page_height = A4

    # Configurazione posizioni QR Code
    qr_size = 25 * mm  # Dimensione QR Code (4x4 cm)
    margin = 1 * cm   # Margine della pagina
    spacing_x = 5 * mm  # Spaziatura orizzontale
    spacing_y = 1 * cm  # Spaziatura verticale (più spazio per la didascalia)

    # Numero di QR per riga e colonna
    num_cols = (page_width - 2 * margin) // (qr_size + spacing_x)
    num_rows = (page_height - 2 * margin) // (qr_size + spacing_y)
    qr_per_page = int(num_cols * num_rows)

    x_start = margin
    y_start = page_height - margin - qr_size

    x, y = x_start, y_start
    qr_count = 0

    monthsDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    month = 1;
    dayMonth = 1;

    for i, qr_path in enumerate(qr_paths):
        print("Analyzing", dayMonth, month)
        if ((dayMonth == 28 or dayMonth ==27) and month == 8) or (dayMonth == 10 and month == 12):
            print("printing", dayMonth, month)
            # Aggiunge il QR Code al PDF
            c.drawImage(qr_path, x, y, width=qr_size, height=qr_size)

            # Aggiunge la didascalia sotto il QR Code
            caption = f"QR {dayMonth}/{month}"
            caption_x = x + (qr_size / 2)  # Centra la didascalia sotto il QR
            caption_y = y - 0.5 * cm       # Posizione sotto il QR Code
            c.setFont("Helvetica", 9)     # Imposta il font della didascalia
            c.drawCentredString(caption_x, caption_y, caption)

            qr_count += 1
            
            # Calcola la prossima posizione
            x += qr_size + spacing_x
            if x + qr_size > page_width - margin:
                x = x_start
                y -= qr_size + spacing_y

            # Nuova pagina se necessario
            if qr_count == qr_per_page or i == len(qr_paths) - 1:
                c.showPage()
                x, y = x_start, y_start
                qr_count = 0
            
        if(dayMonth == monthsDays[month-1]):
            dayMonth = 1
            month += 1
        else :
            dayMonth += 1
    c.save()
    print(f"File PDF creato: {pdf_file}")

# Main
if __name__ == "__main__":
    base_path = "c:\\Users\\m.spadoni\\Desktop\\Personali\\custom-daily-message.github.io\\qr_codes\\"
    qr_paths=[]
    for i in range(1, 366):
        qr_paths.append(base_path + f"{i:03}.png")
    # Crea PDF con i QR Code
    print("Creazione del PDF con i QR Code...")
    create_pdf_with_qrs(qr_paths, PDF_FILE, QR_PER_PAGE)

    print("Operazione completata!")
