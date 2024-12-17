import os

# Cartella di output per i file HTML
output_folder = "days"
os.makedirs(output_folder, exist_ok=True)  # Crea la cartella se non esiste

# Contenuto HTML base con un segnaposto per il giorno
html_template = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Un messaggio per Mimmino</title>
    <style>
        body {{
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            background-image: url('../res/background/bg{bg}.jpg');
            background-size: cover; /* Adatta l'immagine alle dimensioni della pagina */
            background-position: center; /* Centra l'immagine */
            background-repeat: no-repeat; /* Evita che l'immagine si ripeta */
            color: black; /* Colore del testo */
            font-family: Arial, sans-serif;
        }}

        h1 {{
            font-size: 1em;
            text-align: center;
            margin-left: 5em;
            margin-right: 5em;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.384); /* Aggiunge un'ombra al testo per maggiore leggibilità */
        }}

        p {{
            font-size: 9pt;
            text-align: center;
            margin-left: 5em;
            margin-right: 5em;
        }}
    </style>
</head>
<body>
    <h1 id="quote">Caricando la frase del giorno...</h1>

    <p id="author"> Mimmina </p>

        <script>
            async function fetchDailyQuote() {{
                const FILE_DAY = {day};
                const FILE_MONTH = {month};
                const today = new Date();
                const day = today.getDate();
                const monthNumber = today.getMonth();
                const month = today.toLocaleString('default', {{ month: 'short' }});
                const filename = month+'-quotes.json';

                if(day != FILE_DAY || monthNumber != FILE_MONTH){{
                    return {{
                        quote:"Non c'è niente per te qui oggi! Riprova nel giorno " + FILE_DAY + "/" + (FILE_MONTH+1),
                        author:"Mimmina"
                    }}
                }}
                
                console.log("Retrieving quotes from ", filename)
                const response = await fetch(filename);
                const data = await response.json();
                const quote = data[day - 1];

                if (quote) {{
                return quote;
                }}else {{
                console.error(`Citazione non trovata per il giorno ${day} ${month}`);
                return null;
                }}
            }}
            // Funzione per recuperare la citazione dall'API
            async function caricaFrase() {{
                try {{
                    const data = await fetchDailyQuote();
                    if (data == null) throw new Error('Errore nel recupero della citazione');
                    
                
                    document.getElementById('quote').textContent = data.quote;
                    document.getElementById('author').textContent = data.author;
                }}catch (error) {{
                    console.error('Errore nel caricamento della citazione:', error);
                    document.getElementById('quote').textContent = 'Impossibile caricare una citazione.';
                }}
            }}

            caricaFrase();
        </script>
</body>
</html>
"""
monthsDays = [31,28,31,30,31,30,31,31,30,31,30,31]

dayNumber = 0
for m in range(0,12):
    for i in range(1, monthsDays[m]+1):
        dayNumber += 1
        file_name = f"{dayNumber:03}.html"  # Nomi file: 001.html, 002.html, ..., 365.html
        file_path = os.path.join(output_folder, file_name)

        content = html_template.format(day=i, month=m, bg=((i%7)+1))

        # Scrivi il contenuto nel file HTML
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

print("Generazione completata!")