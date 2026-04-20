from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ism = request.form.get('ism') 
        baho = request.form.get('baho') 
        sharh = request.form.get('sharh') 

        if len(ism) > 2 and baho in ['1', '2', '3', '4', '5'] and len(sharh) >= 10:
            res = [ism, baho, sharh]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

        return render_template('result4.html', res=res)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
