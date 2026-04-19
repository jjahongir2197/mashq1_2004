from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def kontakt():
    res = None

    if request.method == 'POST':
        ism = request.form.get('ism', '').strip()
        email = request.form.get('email', '').strip()
        xabar = request.form.get('xabar', '').strip()
      
        if len(ism) > 2 and '@' in email and len(xabar) >= 15:
            res = [ism, email, xabar]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('index.html', res=res)

if __name__ == '__main__':
    app.run(debug=True)
