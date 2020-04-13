from flask import Flask, render_template, request
from azure.cosmosdb.table import TableService

table_service = TableService(account_name='cloudshell1200761026', account_key='e8CBA/8hhwpondb//pYIJuC0OlRU7VrzyRYbRNAm1BfPPI54e5oQ/iWzXlWEpiNW6hN4fvFmbNJ7ht0nPDXtiA==')
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

if __name__ == "__main__":
    app.run()