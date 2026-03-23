from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

# PostgreSQL Configuration
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    
    def set_password(self, password):
        self.password = password

    def set_email(self, email):
        """Set email"""
        self.email = email.strip().lower()

    def set_created_at(self, created_at):
        """Set created_at timestamp"""
        self.created_at = created_at
    
    
    def __repr__(self):
        return f'<User {self.email}>'

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
    
    user = User(email=email, password=password)
    user.password = password
    user.email = email
    user.created_at = db.func.now()

    # Add to session and commit
    db.session.add(user)
    db.session.commit()
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

@app.shell_context_processor
def make_shell_context():
    """Make db available in flask shell"""
    return {'db': db, 'User': User}

if __name__ == "__main__":
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()
    
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=False, host="0.0.0.0", port=port)