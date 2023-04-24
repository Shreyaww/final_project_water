from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html') 

@app.route('/form1', methods=['GET'])
def form1():
    return render_template('form1.html')

@app.route('/form2', methods=['GET'])
def form2():
    return render_template('form2.html')  

@app.route('/auth', methods=['GET'])
def auth():
    return render_template('auth.html')  
    
def load_model():
    with open('./saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model = data["model"]
le_state = data["le_state"]
le_temp = data["le_temp"]
le_do = data["le_do"]
le_ph = data["le_ph"]
le_bod = data["le_bod"]
le_ni = data["le_ni"]

@app.route('/researchers', methods=['POST'])
def researchers():
    if request.method == 'POST':
    
        state = request.form['state']
        temp = request.form['temp']
        do = request.form['do']
        ph = request.form['ph']
        bod = request.form['bod']
        ni = request.form['ni']

        X = np.array([[state, temp, do, ph, bod, ni]])
        X[:,0] = le_state.transform(X[:,0])
        X[:,1] = le_temp.transform(X[:,1])
        X[:,2] = le_do.transform(X[:,2])
        X[:,3] = le_ph.transform(X[:,3])
        X[:,4] = le_bod.transform(X[:,4])
        X[:,5] = le_ni.transform(X[:,5])
        X = X.astype(float)

        quality = model.predict(X)
        if quality == 0:
            print(quality)
            return render_template('form2.html',result=f"The predicted quality is VERY POOR! You are strongly adviced not to consume it",state=state,temp=temp,do=do,ph=ph,bod=bod,ni=ni) 
            
        if quality>0 and quality<=1:
            print(quality)
            return render_template('form2.html',result=f"The predicted quality is Poor but can be drinkable if you follow the following steps:\n"
                                "1. Boiling and Filtering by filter paper\n"
                                "2. Bleach Disinfection\n"
                                "3. Disinfect through chlorine dioxide tablets",state=state,temp=temp,do=do,ph=ph,bod=bod,ni=ni)
        
        if quality>1 and quality<=1.5:
            print(quality)
            return render_template('form2.html',result=f"The predicted quality is Good and you can drink it by simply boiling it",state=state,temp=temp,do=do,ph=ph,bod=bod,ni=ni)
            
        if quality>1.5:
            print(quality)
            return render_template('form2.html',result=f"The predicted quality is Excellent and you can drink it directly",state=state,temp=temp,do=do,ph=ph,bod=bod,ni=ni)
           
        
        return "not healthy"

def load_model():
    with open('saved_steps1.pkl', 'rb') as file:
        data1 = pickle.load(file)
    return data1

data1 = load_model()

regressor = data1["model"]
le_state = data1["le_state"]
le_temp = data1["le_temp"]

@app.route('/naive', methods=['POST'])
def naive():
    if request.method == 'POST':
        state = request.form['state']
        temp = request.form['temp']

        X = np.array([[state, temp]])
        X[:,0] = le_state.transform(X[:,0])
        X[:,1] = le_temp.transform(X[:,1])
        X = X.astype(float)

        quality = regressor.predict(X)
        if quality == 0:
            print(quality)
            return render_template('form1.html',result=f"The predicted quality is VERY POOR! You are strongly adviced not to consume it",temp=temp,state=state) 
            
        if quality>0 and quality<=1:
            print(quality)
            return render_template('form1.html',result=f"The predicted quality is Poor but can be drinkable if you follow the following steps:\n"
                                "1. Boiling and Filtering by filter paper\n"
                                "2. Bleach Disinfection\n"
                                "3. Disinfect through chlorine dioxide tablets",temp=temp,state=state)
        
        if quality>1 and quality<=1.5:
            print(quality)
            return render_template('form1.html',resuly=f"The predicted quality is Good and you can drink it by simply boiling it",temp=temp,state=state)
            
        if quality>1.5:
            print(quality)
            return render_template('form1.html',resuly=f"The predicted quality is Excellent and you can drink it directly",temp=temp,state=state)
        
     

if __name__ == '__main__':
    app.run(debug=True)
