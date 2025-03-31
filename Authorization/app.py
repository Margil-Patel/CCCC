from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for session management

# Function to connect to MySQL Database in XAMPP
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # No password in XAMPP
        database="exam"
    )

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# User Registration with Proper Error Handling
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        role = request.form.get("role", "user")  # Default role is user

        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Check if email already exists
        cursor.execute("SELECT * FROM authorization WHERE email = %s", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash("Email already registered. Please log in.", "warning")
            return redirect(url_for("login"))

        # Insert new user into the database
        cursor.execute(
            "INSERT INTO authorization (name, email, password, role) VALUES (%s, %s, %s, %s)",
            (name, email, hashed_password, role),
        )
        conn.commit()

        # Fetch the newly created user
        cursor.execute("SELECT * FROM authorization WHERE email = %s", (email,))
        new_user = cursor.fetchone()

        cursor.close()
        conn.close()

        # Auto-login: Store user info in session
        session["user_id"] = new_user["id"]
        session["user_name"] = new_user["name"]
        session["role"] = new_user["role"]

        flash(f"Welcome, {new_user['name']}! You are now logged in.", "success")

        # Redirect based on user role
        if new_user["role"] == "admin":
            return redirect(url_for("admin_dashboard"))
        else:
            return redirect(url_for("user_dashboard"))

    return render_template("register.html")



# User Login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM authorization WHERE email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            print("Login Debug - User Found:", user)  # Debugging

            if "password" in user and check_password_hash(user["password"], password):
                session["user_id"] = user["id"]
                session["user_name"] = user["name"]
                session["role"] = user["role"]

                print("Session Data After Login:", session)  # Debugging

                flash("Login successful!", "success")

                if user["role"] == "admin":
                    return redirect(url_for("admin_dashboard"))
                else:
                    return redirect(url_for("user_dashboard"))
            else:
                flash("Invalid email or password. Please try again.", "danger")
        else:
            flash("User not found. Please register first.", "danger")

    return render_template("login.html")

# User Dashboard (Protected Route)
@app.route("/user_dashboard")
def user_dashboard():
    if "user_id" not in session:
        flash("Please log in to access the user dashboard.", "danger")
        return redirect(url_for("login"))

    print("Session Data on User Dashboard:", session)  # Debugging

    return render_template("user.html", user=session)

# Admin Dashboard (Protected Route)
@app.route("/admin_dashboard")
def admin_dashboard():
    if "user_id" not in session or session.get("role") != "admin":
        flash("Admin access only!", "danger")
        return redirect(url_for("login"))

    print("Session Data on Admin Dashboard:", session)  # Debugging

    return render_template("admin.html", user=session)

# Logout
@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)