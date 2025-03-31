from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # No password in XAMPP
        database="exam"
    )

# READ: Fetch and Display Users
@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template("users.html", users=users)  # Show users only

# CREATE: Add a New User
@app.route("/add", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        cursor.close()
        conn.close()
        
        return redirect(url_for("get_users"))  # Redirect to users page

    return render_template("add_user.html")  # Show add user form separately

# UPDATE: Update a user's details
@app.route("/update/<int:user_id>", methods=["GET", "POST"])
def update_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")

        cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for("get_users"))

    # Fetch user details if it's a GET request
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    return render_template("update_user.html", user=user)  # Show update form

# DELETE: Remove a user (Only POST for safety)
@app.route("/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for("get_users"))

if __name__ == "__main__":
    app.run(debug=True)