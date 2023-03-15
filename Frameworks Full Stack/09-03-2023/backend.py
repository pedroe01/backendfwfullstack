from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

# @app.route('/<param1>/<param2>')
# def params_page(param1, param2):
#     text = f'Os parâmetros enviados foram {param1} e {param2} e a soma deles é {int(param1) + int(param2)}'
#     return text

@app.route('/media')
def media():
    n1 = request.args.get('n1')
    n2 = request.args.get('n2')
    resultado = ''
    media = ''
    if n1 and n2:
        media = (float(n1) + float(n2)) / 2
        if media > 10: media = 10
        if media >= 7.0:
            resultado = f'Aluno aprovado | Média: {media}'
        elif media > 4 and media < 7:
            resultado = f'Aluno em exame | Média: {media}'
        else:
            resultado = f'Aluno reprovado | Média: {media}'

    return render_template('media.html', resultado=resultado, media=media)

if __name__ == '__main__':
    app.run(debug=True)