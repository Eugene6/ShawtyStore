# 🛍️ ShawtyStore

**ShawtyStore** is a modern and lightweight e-commerce platform built with the Django framework. This project features a clean UI and core functional blocks essential for an online store.

---

## 🚀 Key Features

* **Product Catalog** - Dynamic display of products filtered by categories.
* **User Authentication** - Full-fledged registration, login, and session management system.
* **Shopping Cart** - Dynamic cart functionality allowing users to add, update, or remove items.
* **Database Management** - Connected database enabling full CRUD operations (adding, updating, and deleting products) directly from the Django admin panel.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.x, Django
* **Database:** SQLite (default for development)
* **Frontend:** HTML5, CSS3, JavaScript (Django Templates)

---

## 💻 How to Run the Project Locally

Follow these quick steps in your terminal to set up and run the application:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd ShawtyStore
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # For Windows:
   venv\Scripts\activate
   # For macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Django:**
   ```bash
   pip install django
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the local server:**
   ```bash
   python manage.py runserver
   ```
   Open your browser and visit: `http://127.0.0`
