from flask import Flask , render_template , request
import requests

app = Flask(__name__)

"""
@app.route('/')
def homepage():
    return render_template("index.html")
"""
@app.route('/', methods= ['POST', 'GET'])
def get_weatherdata():
    if request.method == 'POST':
        url = "https://api.openweathermap.org/data/2.5/weather?APPID=b88e766f790c7dc1ed596dcb8d4390d6&units=metric"
        param = {
            'q': request.form['city']
            #'q': request.form.get('city'),
            #'appid':request.form.get('appid'), #b88e766f790c7dc1ed596dcb8d4390d6
        # 'units':request.form.get('units')
        }
        response = requests.get(url, params =param)
        #city_name = request.form['name']
        #response = requests.get(url.format(city_name))
        data = response.json()
        try:
            temps = data['main']['temp']
            #desp = data['weather'][0]['description']
            print(temps)
            print('hello')
            return render_template('index.html',temp=temps)
            #return f"data : {data}, {temp}"
        
        except Exception:
            return "You have entered the wrong city"
        
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 5000, debug=True)


