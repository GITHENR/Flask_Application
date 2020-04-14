from flask import Flask, render_template, request
from azure.cosmosdb.table import TableService

table_service = TableService(account_name='cloudshell703046314', account_key='fTJlnFKqcwkuu4BCIJiOnIqGEB3aNBkY/yaZ55tm7UWKtzuTv5/pdHgzL2HunOGu8IuMHEEV92nMY0wi2ZANGw==')
#task = {'PartitionKey': 'first', 'RowKey': '002',
#        'ID': '0002', 'address': 'India','stock':40}
#table_service.update_entity('customer', task)
app = Flask(__name__)


@app.route("/")
def index():
    return "hi from home page"

@app.route("/user/<name>")
def profile(name):
#    task = {'PartitionKey': 'First', 'RowKey': '1000','description': 'product1', 'priority': 200}
#    table_service.update_entity('product', task)
    return render_template('hello.html', name=name)

@app.route("/submit",methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        stock = request.form['stock']
        material = request.form['material']
        task = {'PartitionKey': 'First', 'RowKey': '1000', 'description': material, 'stock': stock}
        table_service.update_entity('product', task)
        return render_template('stock.html',stock=stock,material=material)
    else:
        return render_template('inputform.html')

