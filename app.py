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

        single_paragraph = " ".join(paragraphs)

        return single_paragraph
    
api.add_resource(newsText,'/')

if __name__ == '__main__':
    app.run(debug=True)