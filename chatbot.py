import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq = pd.read_csv("faq.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(faq['question'])

def chatbot_response(user_input, threshold=0.25):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    idx = int(similarity.argmax())
    score = float(similarity[0][idx])
    if score >= threshold:
        return faq['answer'][idx]
    return "Sorry boss, I didn’t understand 😅"

if __name__ == "__main__":
    print("AI Chatbot 🤖 (type 'quit' to exit)")
    while True:
        user = input("You: ").strip()
        if user.lower() in {"quit", "exit", "q"}:
            break
        print("Bot:", chatbot_response(user))