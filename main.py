from flask import Flask, jsonify, send_file, render_template_string
import markdown

import linearregression


# Inicializar la aplicación de Flask
app = Flask(__name__)

@app.route('/')
def documentation():
    documentation = open('README.md', 'r', encoding='utf-8')
    html = markdown.markdown(documentation.read())
    html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Documentación</title>
            <style>
                body {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    margin: 0;
                    min-height: 100vh;
                    padding: 20px;
                    background-color: #f0f0f0;
                }}
                .content {{
                    max-width: 800px;
                    background-color: #ffffff;
                    padding: 20px;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                    text-align: left;
                }}
            </style>
        </head>
        <body>
            <div class="content">
                {html}
            </div>
        </body>
        </html>
        """

    return render_template_string(html_template)

@app.route('/dataset')
def dataset():
    return send_file('studentsperformance.csv')

@app.route('/predictions')
def predictiongraph():
    linearregression.predictions()
    return send_file('predictions.png')

@app.route('/metrics')
def metrics():
    error, reg, feature_names = linearregression.predictions()
    coefficients = dict(zip(feature_names, reg.coef_))

    response_data = {
        "Mean square error": error,
        "coefficients": coefficients,
        "Intercept": reg.intercept_
    }
    response_json = jsonify(response_data)
    response_json.headers['Content-Type'] = 'application/json; charset=utf-8'

    return response_json

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)