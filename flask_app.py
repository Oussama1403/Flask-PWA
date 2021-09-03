from flask import Flask,render_template, url_for,send_from_directory
import os

app = Flask(__name__)
secret_key = os.urandom(24)
app.secret_key = secret_key


@app.route('/',methods=['POST','GET'])
@app.route('/home',methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/sw.js',methods=["GET","POST"])
def service_worker():
    from flask import make_response
    response = make_response(send_from_directory('.',path='sw.js'))
    response.headers['Content-Type'] = 'application/javascript'
    response.headers['Service-Worker-Allowed'] = '/'
    return response
    
if __name__ == '__main__':
    app.run(debug=True)
   
