import json

def rimuovi_duplicati(file_input, file_output, campo_chiave='quote'):
  # Carica il file JSON
  with open(file_input, 'r', encoding='utf-8') as f:
    data = json.load(f)

  # Crea un set per tenere traccia delle citazioni uniche
  citazioni_uniche = set()
  risultati = []

  # Iteriamo sugli oggetti del JSON e aggiungiamo solo quelli unici
  for item in data:
    chiave = item[campo_chiave]
    if chiave not in citazioni_uniche:
      citazioni_uniche.add(chiave)
      risultati.append(item)

  # Scriviamo i risultati in un nuovo file JSON
  with open(file_output, 'w', encoding='utf-8') as f:
    json.dump(risultati, f, indent=4, ensure_ascii=False)

# Esempi di utilizzo:
rimuovi_duplicati('C:\\Users\\m.spadoni\\Desktop\\Personali\\custom-daily-message.github.io\\script\\citazioni.json', 'res\\quotes\\citazioni_uniche.json')  # Rimuove duplicati basati sulla citazione