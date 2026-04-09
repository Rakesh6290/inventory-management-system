from flask import Blueprint, request, jsonify
from models import db, Supplier, Inventory
from sqlalchemy import func

routes = Blueprint('routes', __name__)


@routes.route('/supplier', methods=['POST'])
def add_supplier():
    data = request.get_json()

    if not data or 'name' not in data or 'city' not in data:
        return jsonify({"error": "Missing required fields"}), 400

    supplier = Supplier(
        name=data.get('name'),
        city=data.get('city')
    )

    db.session.add(supplier)
    db.session.commit()

    return jsonify({
        "message": "Supplier added successfully",
        "supplier": supplier.to_dict()
    }), 201


@routes.route('/inventory', methods=['POST'])
def add_inventory():
    data = request.get_json()

    required_fields = ['supplier_id', 'product_name', 'quantity', 'price']

    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    supplier = Supplier.query.get(data.get('supplier_id'))
    if not supplier:
        return jsonify({"error": "Invalid supplier"}), 400

    try:
        quantity = int(data.get('quantity'))
        price = float(data.get('price'))
    except ValueError:
        return jsonify({"error": "Invalid data types"}), 400

    if quantity < 0:
        return jsonify({"error": "Quantity must be >= 0"}), 400

    if price <= 0:
        return jsonify({"error": "Price must be > 0"}), 400

    item = Inventory(
        supplier_id=data.get('supplier_id'),
        product_name=data.get('product_name'),
        quantity=quantity,
        price=price
    )

    db.session.add(item)
    db.session.commit()

    return jsonify({
        "message": "Inventory added successfully",
        "inventory": item.to_dict()
    }), 201


@routes.route('/inventory', methods=['GET'])
def get_inventory():
    items = Inventory.query.all()

    if not items:
        return jsonify({"message": "No inventory found", "data": []}), 200

    result = [item.to_dict() for item in items]

    return jsonify(result), 200


@routes.route('/inventory/summary', methods=['GET'])
def inventory_summary():
    data = db.session.query(
        Supplier.name,
        func.sum(Inventory.quantity * Inventory.price).label('total_value')
    ).join(Inventory).group_by(Supplier.id).order_by(
        func.sum(Inventory.quantity * Inventory.price).desc()
    ).all()

    if not data:
        return jsonify({"message": "No data found", "data": []}), 200

    result = [
        {
            "supplier": row[0],
            "total_value": float(row[1])
        }
        for row in data
    ]

    return jsonify(result), 200