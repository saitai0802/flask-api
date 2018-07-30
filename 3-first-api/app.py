from flask import Flask,jsonify,request,render_template

app = Flask(__name__) # __name__ file unique name

stores = [{
    'name': 'My Store',
    'items': [{'name':'my item', 'price': 15.99 }]
}]

# ---------------- Start -----------------------
# This part uses for web page redering.
@app.route('/') # decorator
def home():
  return render_template('index.html')
# ---------------- End -----------------------

#post /store data: {name :}
@app.route('/store' , methods=['POST'])
def create_store():
  request_data = request.get_json() # Set the JSon data back
  new_store = {
    'name':request_data['name'],
    'items':[]
  }
  stores.append(new_store)
  return jsonify(new_store)
  #pass

#get /store/<name> data: {name :}
@app.route('/store/<string:name>')
def get_store(name):
  for store in stores:
    if store['name'] == name:
          return jsonify(store)
  return jsonify ({'message': 'store not found'}) # 保底 error message
  #pass

#get /store
@app.route('/store')
def get_stores():
  return jsonify({'stores': stores})
  #pass

#post /store/<name> data: {name :}
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
  request_data = request.get_json()
  for store in stores:
    if store['name'] == name:
        new_item = {
            'name': request_data['name'],
            'price': request_data['price']
        }
        store['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'store not found'})
  #pass

#get /store/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
  for store in stores:
    if store['name'] == name:
        return jsonify( {'items':store['items'] } )
  return jsonify ({'message':'store not found'})

  #pass

# if __name__ == '__main__':
# app.env = "development"
# app.debug = True

# Since I am using vagrant now, so please check the Vagrantfile to get the Public IP
# config.vm.network "public_network", ip: "192.168.19.240", bridge: 'en1: Wi-Fi (AirPort)'
app.run(host = '0.0.0.0', port=5000)
