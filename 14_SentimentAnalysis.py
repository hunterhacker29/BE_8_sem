

import pandas as pd 


reviews = [
    "Amazing product",
    "Worst experience",
    "Good service",
    "Not good",
    "Excellent quality",
    "Waste of money"
]


positive_words = ["good", "great", "amazing", "excellent", "love", "nice"]
negative_words = ["bad", "worst", "terrible", "waste", "not"]


sentiment = []

for i in reviews:
    
    words = i.lower().split()
    
    pos = 0
    neg = 0 
    
    for j in words :
        if j in positive_words:
            pos+=1

        elif j in negative_words:
            neg+=1
        
        
    if pos>neg:
        sentiment.append("Positive")
    
    elif neg > pos:
        sentiment.append("Negative")
    else:
        sentiment.append("Neutral")
        
        
print(reviews)
print(sentiment)