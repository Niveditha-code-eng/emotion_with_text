print("ANALYSIS THE EMOTION OF THE POEM")

from textblob import TextBlob

def analyze_poem(poem_text):
    blob = TextBlob(poem_text)
    sentiment = blob.sentiment
    print(f"Poem Sentiment Score: {sentiment.polarity}")
    if sentiment.polarity > 0.1:
        return "This poem carries a uplifting and hopeful tone."
    elif sentiment.polarity < -0.1:
        return "This poem carries a sad and hopeless tone."
    else:
        return "This poem carries a calm and neutral tone."

my_poem = input("Enter your poem: ")
print(analyze_poem(my_poem))