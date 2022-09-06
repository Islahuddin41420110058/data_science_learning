import re
from flask import Flask, jsonify, request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__)

app.json_encoder = LazyJSONEncoder
swagger_template = dict(
    info = {
        'title': LazyString(lambda:'API documentation for Data Processing and Modeling'),
        'version': LazyString(lambda:'1.0.0'),
        'description': LazyString(lambda:'Dokumentasi Untuk Data Processing dan Modelling'),
    },
    host = LazyString(lambda: request.host)
    )
swagger_config = {
    "headers": [],
    "specs":[
        {
            "endpoint": 'docs',
            "route": '/docs.json',
        }
    ],
    "static_url_path":'/flasgger_static',
    "swagger_ui":True,
    "specs_route":"/docs/"
}

swagger = Swagger(app, template=swagger_template, config=swagger_config)

@swag_from('docs/hello_world.yml', methods=['GET'])
@app.route('/', methods=['GET'])
def hello_world():
    json_response={
        'status_code': 200,
        'description':'Menyapa Hello World, percobaan islahuddin',
        'data':'Hello World',
    }

    response_data = jsonify(json_response)
    return response_data

@swag_from("docs/text_processing.yml", methods=['POST'])
@app.route('/text_processing', methods=['POST'])
def text_processing():
    text = request.form.get('text')

    json_response = { 
        'status_code':200, 
        'description':'teks yang sudah diproses, percobaan islahuddin', 
        'data': re.sub(r'[^a-zA-Z0-9]', ' ', text)
        }

    response_data = jsonify(json_response)
    return response_data
if __name__ == '__main__':
    app.run()



