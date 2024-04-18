from flask import Flask,request,jsonify
from flask_restful import Resource,Api
from newspaper import Article
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api=Api(app)

@app.route('/scrap',methods=['POST'])
def scrap():
    try:
        data=request.json

        toi_article = Article(data['url'], language="en")

        toi_article.download()
        
        toi_article.parse()

        paragraphs = toi_article.text.split("\n")

        chars_to_remove = ['/','"','(' ,')','|']

        cleaned_text_list = []
        news_array = []
        for string in paragraphs:
            for char in chars_to_remove:
                string = string.replace(char, "")
            cleaned_text_list.append(string)

        for string in cleaned_text_list:
            if string=="":
                continue
            news_array.append(string)
            
        return jsonify({'status':'true','news_array':news_array})
    except:
        return jsonify({'status':'false'})

if __name__ == '__main__':
    app.run(debug=True)