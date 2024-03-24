# save this as app.py
#Importing neccessary modules for flask and sqlalchemy
from flask import Flask, escape, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy 

#creating an instance of flask object and points to the folder of our templates
app = Flask(__name__, template_folder='web_templates') 

#connecting the sqlalchemy database with sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///goblin_cakes.db'

#binding the instance of the connection to flask application
db = SQLAlchemy(app) 

#db.Model is the baseclass for the models and sqlalchemy instace. This creates GoblinCakeSales class and also by using SQLAlchemy.create_all() method in the python shell also creates tables and database
class GoblinCakeSales(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	Product = db.Column(db.String(25))
	Product_Type = db.Column(db.String(25))
	Price_per = db.Column(db.Integer)
	Unit_Sold = db.Column(db.Integer)
	Quarter = db.Column(db.Integer)

	#def __repr__(self): 
		#return f"GoblinCakeSales('{self.Product}', '{self.Product_Type}', '{self.Price_per}', '{self.Unit_Sold}', '{self.Quarter}')"

	#creating a constructor of the class GoblinCakeSales that initializes the variables
	def __init__(self, Product, Product_Type, Price_per, Unit_Sold, Quarter):
	   self.Product = Product
	   self.Product_Type = Product_Type
	   self.Price_per = Price_per
	   self.Unit_Sold = Unit_Sold
	   self.Quarter = Quarter
 


@app.route('/')#decorator that informs flask which url should be active
@app.route('/first')#decorator that activates the first url
def firstQuarter():
    return render_template('home.html', GoblinCakeSales = GoblinCakeSales.query.filter_by(Product_Type= 'Cake',Quarter = 1).all())#query to select neccessary field as per project requirements

@app.route('/')
@app.route('/second')#decorator that activates the second url
def secondQuarter():
    return render_template('home.html', GoblinCakeSales = GoblinCakeSales.query.filter_by(Product_Type= 'Cake',Quarter = 2).all())#query to select neccessary field as per project requirements

@app.route('/')
@app.route('/third')#decorator that activates the third url
def thirdQuarter():
    return render_template('home.html', GoblinCakeSales = GoblinCakeSales.query.filter_by(Product_Type= 'Cake',Quarter = 3).all())#query to select neccessary field as per project requirements


@app.route('/')
@app.route('/fourth')#decorator that activates the fourth url
def fourthQuarter():
    return render_template('home.html', GoblinCakeSales = GoblinCakeSales.query.filter_by(Product_Type= 'Cake',Quarter = 4).all())#query to select neccessary field as per project requirements


@app.route('/First')
def First():
	#GoblinCakeSales = GoblinCakeSales.query.filter_by(Quarter = 1).all()
    return redirect(url_for('firstQuarter'))


@app.route('/Second')
def Second():
    return redirect(url_for('secondQuarter'))



@app.route('/Third')
def Third():
    return redirect(url_for('thirdQuarter'))


@app.route('/Fourth')
def Fourth():
    return redirect(url_for('fourthQuarter'))




#this is used to run the application on port 4444 because the defualt port 5000 was unable to connect after first trial
if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))

