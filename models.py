class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.known = False
    def mark_known(self):
        self.known = True
    def mark_unknown(self):
        self.known = False
    def to_dict(self):
        return {
            "question": self.question,
            "answer": self.answer,
            "known": self.known
        }
 
class FlashcardSet:
    def __init__(self, topic, cards):
        self.topic = topic
        self.cards = cards

    def get_score(self):
        return sum(
            card.known
            for card in self.cards
        )
 
    def get_total(self):
        return len(self.cards)
    def get_percentage(self):
        if not self.cards:
            return 0
        return round(
            self.get_score()
            / self.get_total()
            * 100,
            1
        )
 
    def to_dict(self):
        return {
            "topic": self.topic,
            "cards": [
                card.to_dict()
                for card in self.cards
            ],
            "score": self.get_score(),
            "total": self.get_total(),
            "percentage": self.get_percentage()
        }
 