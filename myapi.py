# !pip install paralleldots

import paralleldots
 
class API:
    def __init__(self):
        paralleldots.set_api_key('API') # Enter your API key
        
        
    def sentiment_analysis(self, text):    
            response = paralleldots.sentiment(text)
            return response
    
    def ner_analysis(self, text):    
            response = paralleldots.ner(text)
            return response
    
    def emp_analysis(self, text):    
            response = paralleldots.emotion(text)
            return response


# obj = API()
# print(obj.sentiment_analysis("Look what's just come on the market in #ValThorens! A recently renovated, charming 6 bed duplex apartment in the heart of the resort with superb views!"))
