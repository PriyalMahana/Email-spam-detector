import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

print("Spam Detection Program")

data = pd.read_csv("spam.csv", encoding="latin-1")

data = data[["v1", "v2"]]
data.columns = ["type", "text"]

data["type"] = data["type"].map({"ham": 0, "spam": 1})

x = data["text"]
y = data["type"]

tfidf = TfidfVectorizer(stop_words="english", max_features=5000, ngram_range=(1, 2))
x = tfidf.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

nb = MultinomialNB()
nb.fit(x_train, y_train)

pred = nb.predict(x_test)
print("Accuracy:", accuracy_score(y_test, pred))

extra_words = [
    "free", "win", "winner", "urgent", "money", "offer",
    "click", "buy now", "limited time", "call now",
    "lottery", "prize", "cash", "reward"
]

def clean_text(t):
    t = t.lower()
    for w in extra_words:
        if w in t:
            t += " " + w
    return t

while True:
    msg = input("Enter message (type exit to stop): ")

    if msg.lower() == "exit":
        break

    msg = clean_text(msg)
    vec = tfidf.transform([msg])
    res = nb.predict(vec)

    if res[0] == 1:
        print("Spam")
    else:
        print("Not Spam")
