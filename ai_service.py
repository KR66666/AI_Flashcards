from models import Flashcard
 
class AIFlashcardGenerator:
    def generate(self, topic, count): 
        cards = []
        for i in range(count):
            question = (
                f"Co je důležité vědět "
                f"o tématu {topic}? "
                f"Otázka {i + 1}"
            )
            answer = (
                f"Toto je ukázková odpověď "
                f"k tématu {topic}. "
                f"Odpověď {i + 1}"
            )
            card = Flashcard(
                question,
                answer
            )
            
            cards.append(card)
        return cards
 