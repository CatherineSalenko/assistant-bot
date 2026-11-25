import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

phrases = []
commands_name = []


with open("data/intents.json", encoding="utf-8") as file:
    data = json.load(file)


for command, examples in data.items():
    for example in examples:
        phrases.append(example)
        commands_name.append(command)


model = make_pipeline(TfidfVectorizer(), LogisticRegression(C=10))
model.fit(phrases, commands_name)


def recognize_command(text: str) -> tuple[str, float]:
    prediction = model.predict([text])[0]
    probability = model.predict_proba([text])[0].max()
    return str(prediction), float(probability)

