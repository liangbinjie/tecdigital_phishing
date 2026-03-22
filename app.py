from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "your-secret-key-change-this")
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    """Handle login form submission"""
    
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()
    print(f"Login attempt: email={email}, password={'*' * len(password)}")  # Debugging, do not log passwords in production
    # Validation
    if not email or not password:
        flash("Email y contraseña son requeridos", "error")
        return redirect(url_for("home"))
    
    if "@" not in email:
        flash("Por favor ingresa un email válido", "error")
        return redirect(url_for("home"))
    
    # TODO: Add authentication logic here (database check, LDAP, etc.)
    # For now, just store in session
    session.permanent = True
    session["user_email"] = email
    
    flash(f"Sesión iniciada como {email}", "success")
    return redirect("https://tecdigital.tec.ac.cr/dotlrn")

@app.route("/dashboard")
def dashboard():
    """Protected route - user must be logged in"""
    if "user_email" not in session:
        flash("Debes iniciar sesión primero", "error")
        return redirect(url_for("home"))
    
    return f"Bienvenido, {session['user_email']}!"

@app.route("/logout")
def logout():
    """Handle logout"""
    session.clear()
    flash("Sesión cerrada correctamente", "success")
    return redirect(url_for("home"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)