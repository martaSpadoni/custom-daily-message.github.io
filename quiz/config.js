// Configurazione del quiz: modifica solo questo file.
// I percorsi delle immagini sono relativi alla cartella "quiz".
window.QUIZ_CONFIG = {
  title: "Scegli il tuo regalo",
  subtitle: "Rispondi d'istinto, nessuna risposta è sbagliata!",
  startButton: "Iniziamo!",

  // Numero di domande da usare (le prime N della lista). null = tutte.
  totalQuestions: null,

  // Opzione che vince in caso di parità: "A" oppure "B".
  tieBreaker: "A",

  // Regali associati alle opzioni vincenti.
  gifts: {
    A: {
      title: "Bernina Express",
      message: "Hai scelto la neve e il freddo incantevole!",
      image: "../res/images/quiz/trenino.jpg"
    },
    B: {
      title: "Weekend a Napoli",
      message: "Il destino ha parlato...pizza e presepi!",
      image: "../res/images/quiz/napoli.jpg"
    }
  },

  // background: percorso di un'immagine oppure un valore CSS
  // (colore, linear-gradient(...), radial-gradient(...)).
  // Se omesso viene usato defaultBackground.
  defaultBackground: "linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%)",

  questions: [
    {
      question: "Cosa preferisci?",
      optionA: "Stasi glaciale",
      optionB: "Teatro di strada"
    },
    {
      question: "Cosa preferisci?",
      optionA: "Silenzio panoramico",
      optionB: "Caos vitale"
    },
    {
      question: "Cosa preferisci?",
      optionA: "Bolla di vetro",
      optionB: "Palcoscenico aperto"
    },
    {
      question: "Cosa preferisci?",
      optionA: "Isolamento zen",
      optionB: "Goliardia rumorosa"
    },
    {
      question: "Cosa preferisci?",
      optionA: "Vette innevate",
      optionB: "Fuoco e fiamme"
    },
    {
      question: "Cosa preferisci?",
      optionA: "Tempo sospeso",
      optionB: "Movimento continuo"
    },
    {
      question: "Cosa preferisci?",
      optionA: "Contemplazione muta",
      optionB: "Dramma collettivo"
    },
    {
      question: "Cosa preferisci?",
      optionA: "Rigore nordico",
      optionB: "Istinto meridiano"
    },
    {
      question: "Cosa preferisci?",
      optionA: "Eremita chic",
      optionB: "Capopopolo improvvisato"
    },
    {
      question: "Cosa preferisci?",
      optionA: "Paesaggio cartolina",
      optionB: "Set cinematografico"
    },
    {
      question: "Cosa preferisci?",
      optionA: "Cioccolato Svizzero",
      optionB: "Pizza"
    }
  ]
};
