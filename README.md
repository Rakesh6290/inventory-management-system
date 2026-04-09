# 📦 Inventory Management System

A backend application built using Flask to manage suppliers and inventory, with RESTful APIs and database integration.

---

## 🚀 Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* SQLite
* Docker (optional)

---

## 📁 Project Structure

```
inventory_app/
│
├── app.py
├── models.py
├── routes.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── instance/
    └── database.db
```

---

## ⚙️ Features

* Add new suppliers
* Add inventory items linked to suppliers
* Fetch all inventory items
* Get inventory summary grouped by supplier
* Input validation and error handling
* RESTful API design

---

## 🗄️ Database Design

### Suppliers Table

* id (Primary Key)
* name
* city

### Inventory Table

* id (Primary Key)
* supplier_id (Foreign Key)
* product_name
* quantity
* price

### Relationship

* One supplier → many inventory items

---

## 📡 API Endpoints

### ➤ Add Supplier

**POST /supplier**

Request:

```json
{
  "name": "ABC Traders",
  "city": "Hyderabad"
}
```

---

### ➤ Add Inventory

**POST /inventory**

Request:

```json
{
  "supplier_id": 1,
  "product_name": "Laptop",
  "quantity": 10,
  "price": 50000
}
```

---

### ➤ Get All Inventory

**GET /inventory**

---

### ➤ Inventory Summary (Important)

**GET /inventory/summary**

Returns inventory grouped by supplier, sorted by total value (quantity × price)

---

## ▶️ How to Run Locally

### 1. Clone Repository

```
git clone <your-repo-link>
cd inventory_app
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Application

```
python app.py
```

Server will run at:

```
http://127.0.0.1:5000/
```

---

## 🧪 Testing

APIs can be tested using:

* Thunder Client (VS Code)
* Postman

---

## 🐳 Docker Setup (Optional)

### Build Image

```
docker build -t inventory-app .
```

### Run Container

```
docker run -p 5000:5000 inventory-app
```

---

## 🧠 Design Decisions

* Used SQLite for simplicity and quick setup
* Used SQLAlchemy ORM for database abstraction
* Followed modular structure (models, routes, app factory)
* Implemented input validation to ensure data integrity

---

## ⚡ Improvements (Future Scope)

* Add pagination for large datasets
* Add authentication (JWT)
* Add update and delete APIs
* Use PostgreSQL for production
* Add caching for performance

---

## 📸 Screenshots

(Thunder Client / Postman screenshots)

---
Add Supplier API
(POST /supplier request and response)
![alt text](<Screenshot (32).png>)

Add Inventory API
(POST /inventory with validation checks)
![alt text](<Screenshot (33).png>)

Get Inventory
(GET /inventory showing all items)
![alt text](<Screenshot (34).png>)

Inventory Summary
(Grouped by supplier, sorted by total value)
![alt text](<Screenshot (35).png>)

