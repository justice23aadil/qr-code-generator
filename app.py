from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_code = None
    if request.method == 'POST':
        data = request.form['qrdata']
        img = qrcode.make(data)
        
        # Convert to base64
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        qr_code = f"data:image/png;base64,{image_base64}"
    
    return render_template('index.html', qr_code=qr_code)

if __name__ == '__main__':
    app.run(debug=True)