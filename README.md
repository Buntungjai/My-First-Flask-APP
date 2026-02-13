# My First Flask App

A simple internal service request web application built with Flask.

This project is created for learning purposes and demonstrates how to build
a basic web application with authentication, database integration, and an admin dashboard.

---

## 🎯 Features

- User login system
- Create new service requests
- Admin dashboard
- View all service requests with status
- SQLite database
- Simple HTML templates (Jinja2)

---

## 🖥️ Demo Video

▶️ YouTube walkthrough and demo:  
https://youtu.be/UGb6HtWHbAQ

---

## 🛠️ Tech Stack

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- SQLite
- HTML / Jinja2

---

## 📂 Project Structure

```text
My-First-Flask-APP/
├── app.py # Main Flask application
├── service.db # SQLite database
├── templates/ # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   └── new_request.html
└── README.md

## 🚀 How to Run

1. Clone the repository
bash
git clone https://github.com/Buntungjai/My-First-Flask-APP.git
cd My-First-Flask-APP

2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3. Install dependencies
pip install flask flask-login flask-sqlalchemy

4. Run the application
python app.py
   
5. Open browser
http://127.0.0.1:5000




