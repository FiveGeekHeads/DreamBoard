from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/register')
def register():
    return render_template('register.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@main.route('/goals')
def goals():
    return render_template('goals.html')

@main.route('/tasks')
def tasks():
    return render_template('tasks.html')

@main.route('/gallery')
def gallery():
    return render_template('gallery.html')

@main.route('/profile')
def user_profile():
    return render_template('profile.html')