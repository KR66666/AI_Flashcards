from flask import Flask, render_template, request, jsonify
from models import FlashcardSet
from ai_service import AIFlashcardGenerator
 
app = Flask(__name__)
 
generator = AIFlashcardGenerator()
 
@app.route("/")
def index():

    return render_template("index.html")
 
@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    topic = data.get("topic")
    count = int(data.get("count", 5))
 
    if not topic:
        return jsonify({
            "error": "Zadej téma."
        }), 400
 
    cards = generator.generate(
        topic,
        count
    )
 

    flashcard_set = FlashcardSet(
        topic,
        cards
    )
 
    return jsonify(
        flashcard_set.to_dict()
    )
 
if __name__ == "__main__":
    app.run(debug=True)
 