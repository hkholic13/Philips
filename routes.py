from flask import Flask, jsonify, request
from models import CartItem

app = Flask(__name__)

# Dummy database (in-memory storage)
cart_items = []

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.json
    name = data['name']
    price = data['price']
    quantity = data['quantity']

    # Create a new cart item
    item = CartItem(name, price, quantity)
    cart_items.append(item)

    return jsonify({'message': 'Item added to cart successfully!'})

@app.route('/view_cart', methods=['GET'])
def view_cart():
    cart = [item.serialize() for item in cart_items]
    return jsonify({'cart': cart})

if __name__ == '__main__':
    app.run(debug=True)
