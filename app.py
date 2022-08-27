from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model_qda = pickle.load(open("start_qda.pkl", "rb"))
model_rf = pickle.load(open("start_rf.pkl", "rb"))
@app.route('/form')
def form():
    return render_template('form.html')

@app.route("/")
#@cross_origin()
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    
    if request.method == 'POST':
        print(request.form)
        founded_at = int(request.form['founded_at'])
        first_funding_at = float(request.form["first_funding_at"])
        last_funding_at = float(request.form["last_funding_at"])
        funding_rounds = float(request.form["funding_rounds"])
        funding_total_usd = float(request.form["funding_total_usd"])
        first_milestone_at = float(request.form["first_milestone_at"])
        last_milestone_at = int(request.form["last_milestone_at"])
        milestones = int(request.form["milestones"])
        relationships = int(request.form["relationships"])

        # Sector
        sector=request.form['sector']
        if(sector=='advertising'):
            advertising = 1
            biotech = 0
            consulting = 0
            ecommerce = 0
            education = 0
            enterprise = 0
            games_video = 0
            hardware = 0
            mobile = 0
            network_hosting = 0
            other = 0
            public_relations = 0 
            search = 0
            software = 0 
            web = 0

        elif(sector=='biotech'):
            advertising = 0
            biotech = 1
            consulting = 0
            ecommerce = 0
            education = 0
            enterprise = 0
            games_video = 0
            hardware = 0
            mobile = 0
            network_hosting = 0
            other = 0
            public_relations = 0 
            search = 0
            software = 0 
            web = 0

        elif(sector=='consulting'):
            advertising = 0
            biotech = 0
            consulting = 1
            ecommerce = 0
            education = 0
            enterprise = 0
            games_video = 0
            hardware = 0
            mobile = 0
            network_hosting = 0
            other = 0
            public_relations = 0 
            search = 0
            software = 0 
            web = 0

        elif(sector=='ecommerce'):
            advertising = 0
            biotech = 0
            consulting = 0
            ecommerce = 1
            education = 0
            enterprise = 0
            games_video = 0
            hardware = 0
            mobile = 0
            network_hosting = 0
            other = 0
            public_relations = 0 
            search = 0
            software = 0 
            web = 0

        elif(sector=='education'):
            advertising = 0
            biotech = 0
            consulting = 0
            ecommerce = 0
            education = 1
            enterprise = 0
            games_video = 0
            hardware = 0
            mobile = 0
            network_hosting = 0
            other = 0
            public_relations = 0 
            search = 0
            software = 0 
            web = 0

        elif(sector=='enterprise'):
            advertising = 0
            biotech = 0
            consulting = 0
            ecommerce = 0
            education = 0
            enterprise = 1
            games_video = 0
            hardware = 0
            mobile = 0
            network_hosting = 0
            other = 0
            public_relations = 0 
            search = 0
            software = 0 
            web = 0

        
        elif(sector=='games_video'):
            advertising = 0
            biotech = 0
            consulting = 0
            ecommerce = 0
            education = 0
            enterprise = 0
            games_video = 1
            hardware = 0
            mobile = 0
            network_hosting = 0
            other = 0
            public_relations = 0 
            search = 0
            software = 0 
            web = 0
            
        elif(sector=='hardware'):
            advertising = 0
            biotech = 0
            consulting = 0
            ecommerce = 0
            education = 0
            enterprise = 0
            games_video = 0
            hardware = 1
            mobile = 0
            network_hosting = 0
            other = 0
            public_relations = 0 
            search = 0
            software = 0 
            web = 0
            
        elif(sector=='mobile'):
            advertising = 0
            biotech = 0
            consulting = 0
            ecommerce = 0
            education = 0
            enterprise = 0
            games_video = 0
            hardware = 0
            mobile = 1
            network_hosting = 0
            other = 0
            public_relations = 0 
            search = 0
            software = 0 
            web = 0
            
        elif(sector=='network_hosting'):
            advertising = 0
            biotech = 0
            consulting = 0
            ecommerce = 0
            education = 0
            enterprise = 0
            games_video = 0
            hardware = 0
            mobile = 0
            network_hosting = 1
            other = 0
            public_relations = 0 
            search = 0
            software = 0 
            web = 0

        elif(sector=='other'):
            advertising = 0
            biotech = 0
            consulting = 0
            ecommerce = 0
            education = 0
            enterprise = 0
            games_video = 0
            hardware = 0
            mobile = 0
            network_hosting = 0
            other = 1
            public_relations = 0 
            search = 0
            software = 0 
            web = 0

        elif(sector=='public_relations'):
            advertising = 0
            biotech = 0
            consulting = 0
            ecommerce = 0
            education = 0
            enterprise = 0
            games_video = 0
            hardware = 0
            mobile = 0
            network_hosting = 0
            other = 0
            public_relations = 1 
            search = 0
            software = 0 
            web = 0

        elif(sector=='search'):
            advertising = 0
            biotech = 0
            consulting = 0
            ecommerce = 0
            education = 0
            enterprise = 0
            games_video = 0
            hardware = 0
            mobile = 0
            network_hosting = 0
            other = 0
            public_relations = 0 
            search = 1
            software = 0 
            web = 0

        elif(sector=='software'):
            advertising = 0
            biotech = 0
            consulting = 0
            ecommerce = 0
            education = 0
            enterprise = 0
            games_video = 0
            hardware = 0
            mobile = 0
            network_hosting = 0
            other = 0
            public_relations = 0 
            search = 0
            software = 1
            web = 0
            
        elif(sector=='web'):
            advertising = 0
            biotech = 0
            consulting = 0
            ecommerce = 0
            education = 0
            enterprise = 0
            games_video = 0
            hardware = 0
            mobile = 0
            network_hosting = 0
            other = 0
            public_relations = 0 
            search = 0
            software = 0
            web = 1

        else:
            advertising = 0
            biotech = 0
            consulting = 0
            ecommerce = 0
            education = 0
            enterprise = 0
            games_video = 0
            hardware = 0
            mobile = 0
            network_hosting = 0
            other = 0
            public_relations = 0 
            search = 0
            software = 0 
            web = 0

         

        # country

        country = request.form["country"]
        if (country == 'AUS'):
            AUS = 1
            CAN = 0
            DEU = 0
            ESP = 0
            FRA = 0
            GBR = 0
            IND = 0
            USA = 0
            other = 0


        elif (country == 'CAN'):
            AUS = 0
            CAN = 1
            DEU = 0
            ESP = 0
            FRA = 0
            GBR = 0
            IND = 0
            USA = 0
            other = 0

        elif (country == 'DEU'):
            AUS = 0
            CAN = 0
            DEU = 1
            ESP = 0
            FRA = 0
            GBR = 0
            IND = 0
            USA = 0
            other = 0

        elif (country == 'ESP'):
            AUS = 0
            CAN = 0
            DEU = 0
            ESP = 1
            FRA = 0
            GBR = 0
            IND = 0
            USA = 0
            other = 0

        elif (country == 'FRA'):
            AUS = 0
            CAN = 0
            DEU = 0
            ESP = 0
            FRA = 1
            GBR = 0
            IND = 0
            USA = 0
            other = 0

        elif (country == 'GBR'):
            AUS = 0
            CAN = 0
            DEU = 0
            ESP = 0
            FRA = 0
            GBR = 1
            IND = 0
            USA = 0
            other = 0

        elif (country == 'IND'):
            AUS = 0
            CAN = 0
            DEU = 0
            ESP = 0
            FRA = 0
            GBR = 0
            IND = 1
            USA = 0
            other = 0

        elif (country == 'USA'):
            AUS = 0
            CAN = 0
            DEU = 0
            ESP = 0
            FRA = 0
            GBR = 0
            IND = 0
            USA = 1
            other = 0

        elif (country == 'other'):
            AUS = 0
            CAN = 0
            DEU = 0
            ESP = 0
            FRA = 0
            GBR = 0
            IND = 0
            USA = 0
            other = 1

        else:
            AUS = 0
            CAN = 0
            DEU = 0
            ESP = 0
            FRA = 0
            GBR = 0
            IND = 0
            USA = 0
            other = 0

       

        active_days = abs(founded_at - 2021) * 365
        print(active_days)
        prediction_qda = model_qda.predict([[founded_at,first_funding_at,last_funding_at,funding_rounds,funding_total_usd,first_milestone_at,last_milestone_at,milestones,relationships,advertising,biotech,consulting,ecommerce,education,enterprise,games_video,hardware,mobile,network_hosting,other,public_relations,search,software,web,AUS,CAN,DEU,ESP,FRA,GBR,IND,USA,other,active_days]])
        prediction_rf = model_rf.predict([[founded_at,first_funding_at,last_funding_at,funding_rounds,funding_total_usd,first_milestone_at,last_milestone_at,milestones,relationships,advertising,biotech,consulting,ecommerce,education,enterprise,games_video,hardware,mobile,network_hosting,other,public_relations,search,software,web,AUS,CAN,DEU,ESP,FRA,GBR,IND,USA,other,active_days]])
        output_qda=(prediction_qda[0])
        output_rf=(prediction_rf[0])
        print("output_qda:",output_qda)
        print("output_rf:",output_rf)
        if output_qda==1 & output_rf==1:
           return render_template('form.html',pred='company is opened and its operating!',bhai="well done")
        elif output_qda==1 & output_rf==2:
           return render_template('form.html',pred='company is opened and it is in IPO.!',bhai="well done")
        elif output_rf==3 & output_qda==0:
           return render_template('form.html',pred='company is closed and it is in acquired !!',bhai="sorry failed to success")
        elif output_rf==0 & output_qda==0:
           return render_template('form.html',pred='company is closed!!!!Danger',bhai="sorry failed to success")
        else:
           return render_template('form.html',pred='Please enter the value again !!',bhai="sorry failed to success")
    else:
        return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)

