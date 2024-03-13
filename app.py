from flask import Flask,request
from  flask_restful import Resource,Api
from newspaper import Article

app = Flask(__name__)

api=Api(app)

class newsText(Resource):
    def get(self):
        data=request.json
        toi_article = Article(data['url'], language="en") 

        toi_article.download()
        
        toi_article.parse()

        paragraphs = toi_article.text.split("\n")

        chars_to_remove = ['/', '"']

        cleaned_text_list = []
        for string in paragraphs:
            for char in chars_to_remove:
                string = string.replace(char, "")
            cleaned_text_list.append(string)

        for string in cleaned_text_list:
                if string=="":
                    cleaned_text_list.remove(string)

        return cleaned_text_list
    
api.add_resource(newsText,'/')

if __name__ == '__main__':
    app.run(debug=True)