from fastapi import FastAPI

app = FastAPI()

def sentimentAnalysis(sentence):
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    returnString = "Sentiment score: " + str(sia.polarity_scores(sentence))
    return returnString

@app.get("/")
def home():
    return {"about": "nothing to see here"}

@app.post("/sentiment")
def sentiment(sentence: str):
    return {"sentiment": sentimentAnalysis(sentence)}