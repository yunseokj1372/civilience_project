from fastapi import FastAPI
import uvicorn

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

if __name__ == "__main__":
    #main is the name of the file
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)