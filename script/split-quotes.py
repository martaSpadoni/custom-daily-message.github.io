import json

def split(file_input):
  
  monthsDays = [31,28,31,30,31,30,31,31,30,31,30,31]
  months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dic"]
  # Carica il file JSON
  with open(file_input, 'r', encoding='utf-8') as f:
    data = json.load(f)

    start = 0
    for m in range(0,12):
        quotes = []
        print("tot: ", len(data), start)
        if(start >= len(data) or start + monthsDays[m] >= len(data)):
           return
        for i in range(0, monthsDays[m]):
           quotes.append(data[i+start])
        start += monthsDays[m]
        print(len(quotes))
        file_output = "res\\quotes\\" + months[m] + "-quotes.json"
        with open(file_output, 'w', encoding='utf-8') as f:
           json.dump(quotes, f, indent=4, ensure_ascii=False)

    if(start < len(data)):
       with open("remaining-quotes.json", 'w', encoding='utf-8') as f:
           json.dump(data[start+1 : ], f, indent=4, ensure_ascii=False)
          
 

# Esempi di utilizzo:
split('res\\quotes\\citazioni_uniche.json')