from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from datetime import datetime
import os

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nexatech.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-prod')

# Mail Configuration (configure with real SMTP in production)
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', '')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', '')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER', 'ibrahimathiongane2006@gmail.com')

db = SQLAlchemy(app)
mail = Mail(app)

# =========================
# Database Models
# =========================

class ContactSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20))
    company = db.Column(db.String(100))
    project_type = db.Column(db.String(50))
    budget = db.Column(db.String(50))
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Contact {self.name} - {self.email}>'

class BetaSignup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    properties = db.Column(db.String(20), default='1')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<BetaSignup {self.email}>'

# Create tables
with app.app_context():
    db.create_all()

# =========================
# Email Helper Functions
# =========================

def send_contact_notification(contact):
    """Send email notification for new contact form submission"""
    try:
        if app.config['MAIL_USERNAME']:  # Only send if configured
            msg = Message(
                subject=f"[NexaTech] Nouveau contact: {contact.name}",
                recipients=[app.config['MAIL_DEFAULT_SENDER']],
                body=f"""
Nouveau message de contact reçu :

Nom: {contact.name}
Email: {contact.email}
Téléphone: {contact.phone or 'Non renseigné'}
Société: {contact.company or 'Non renseignée'}
Type de projet: {contact.project_type or 'Non renseigné'}
Budget: {contact.budget or 'Non renseigné'}

Message:
{contact.message}

---
Reçu le: {contact.created_at.strftime('%d/%m/%Y à %H:%M')}
                """
            )
            mail.send(msg)
            return True
    except Exception as e:
        print(f"Email error: {e}")
    return False

def send_beta_welcome(email):
    """Send welcome email to beta signup"""
    try:
        if app.config['MAIL_USERNAME']:  # Only send if configured
            msg = Message(
                subject="Bienvenue dans la beta Immogest ! 🎉",
                recipients=[email],
                body=f"""
Bonjour,

Merci pour votre inscription à la beta d'Immogest !

Vous faites partie des premiers à tester notre plateforme de gestion immobilière révolutionnaire.

Prochaines étapes :
1. Notre équipe va créer votre compte dans les 24h
2. Vous recevrez un email avec vos identifiants
3. 2 mois gratuits pour tester toutes les fonctionnalités !

Des questions ? Répondez directement à cet email.

À très vite,
L'équipe NexaTech
                """
            )
            mail.send(msg)
            return True
    except Exception as e:
        print(f"Email error: {e}")
    return False

# =========================
# Routes
# =========================


# =========================
# Error Handlers
# =========================
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# =========================
# Routes
# =========================

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
@app.route('/favicon.ico')
def static_from_root():
    return app.send_static_file(request.path[1:])

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/produits')
def produits():
    return render_template('produits.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/a-propos')
def a_propos():
    return render_template('a-propos.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Extract form data
        contact_data = ContactSubmission(
            name=request.form.get('name'),
            email=request.form.get('email'),
            phone=request.form.get('phone'),
            company=request.form.get('company'),
            project_type=request.form.get('project_type'),
            budget=request.form.get('budget'),
            message=request.form.get('message')
        )
        
        # Save to database
        db.session.add(contact_data)
        db.session.commit()
        
        # Send email notification
        send_contact_notification(contact_data)
        
        print(f"✅ Contact saved: {contact_data.name} ({contact_data.email})")
        
        return render_template('partials/contact_success.html')
    return render_template('contact.html')

@app.route('/immogest')
def immogest():
    return render_template('immogest.html')

@app.route('/immogest/beta', methods=['POST'])
def immogest_beta():
    email = request.form.get('email')
    properties = request.form.get('properties', '1')
    
    # Check if already registered
    existing = BetaSignup.query.filter_by(email=email).first()
    if existing:
        return render_template('partials/beta_success.html', email=email, already_registered=True)
    
    # Save to database
    signup = BetaSignup(email=email, properties=properties)
    db.session.add(signup)
    db.session.commit()
    
    # Send welcome email
    send_beta_welcome(email)
    
    print(f"✅ Beta signup: {email}, {properties} properties")
    
    return render_template('partials/beta_success.html', email=email)

@app.route('/portfolio/filter/<category>')
def filter_portfolio(category):
    # Define all projects
    all_projects = [
        {
            'title': 'Immogest - Gestion Immo',
            'client': 'Interne',
            'category': 'saas',
            'tags': ['SaaS', 'React', 'Flask'],
            'description': 'Plateforme de gestion immobilière avec paiement automatisé via Mobile Money.',
            'link': '/immogest',
            'color': 'orange'
        },
        {
            'title': 'Boutique Mode en Ligne',
            'client': 'ModeSN',
            'category': 'web',
            'tags': ['E-commerce', 'Stripe'],
            'description': 'Site e-commerce complet avec gestion de stock, panier dynamique et paiements sécurisés.',
            'color': 'purple'
        },
        {
            'title': 'Dashboard Clinique',
            'client': 'Confidentiel',
            'category': 'web',
            'tags': ['WebApp', 'Dashboard'],
            'description': 'Application de gestion de patients, rendez-vous et stocks de médicaments.',
            'color': 'red'
        },
        {
            'title': 'Site Vitrine Restaurant',
            'client': 'Le Lagon',
            'category': 'web',
            'tags': ['Web', 'Réservations'],
            'description': 'Site vitrine avec système de réservation en ligne et menu interactif.',
            'color': 'green'
        },
        {
            'title': 'App Mobile Livraison',
            'client': 'DeliverySN',
            'category': 'mobile',
            'tags': ['Mobile', 'React Native'],
            'description': 'Application mobile de livraison à la demande avec tracking GPS temps réel.',
            'color': 'blue'
        },
        {
            'title': 'Plateforme E-learning',
            'client': 'EduTech',
            'category': 'saas',
            'tags': ['SaaS', 'Education'],
            'description': 'Plateforme de cours en ligne avec gestion des étudiants et suivi de progression.',
            'color': 'indigo'
        },
        {
            'title': 'CRM Sur-Mesure',
            'client': 'SalesPlus',
            'category': 'saas',
            'tags': ['SaaS', 'CRM'],
            'description': 'Système de gestion de la relation client adapté aux PME sénégalaises.',
            'color': 'pink'
        }
    ]
    
    # Filter projects by category
    if category.lower() == 'tous':
        filtered_projects = all_projects
    else:
        filtered_projects = [p for p in all_projects if p['category'] == category.lower()]
    
    return render_template('partials/projects_grid.html', projects=filtered_projects)

@app.route('/stats')
def stats():
    return render_template('partials/stats.html')

# =========================
# Admin Routes & Auth
# =========================

import functools

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('admin_login'))
        return view(**kwargs)
    return wrapped_view

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        password = request.form.get('password')
        # Simple env-based password check (default: admin123)
        admin_pass = os.environ.get('ADMIN_PASSWORD', 'admin123')
        
        if password == admin_pass:
            session['logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('admin/login.html', error="Mot de passe incorrect")
            
    return render_template('admin/login.html')

@app.route('/admin/logout')
def admin_logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))

@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    query = request.args.get('q', '').strip()
    project_type = request.args.get('type', '').strip()
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # --- Contacts Query ---
    contacts_query = ContactSubmission.query
    
    # Search Filter
    if query:
        search_filter = f"%{query}%"
        contacts_query = contacts_query.filter(
            db.or_(
                ContactSubmission.name.ilike(search_filter),
                ContactSubmission.email.ilike(search_filter),
                ContactSubmission.company.ilike(search_filter),
                ContactSubmission.message.ilike(search_filter)
            )
        )
    
    # Category Filter
    if project_type:
        contacts_query = contacts_query.filter(ContactSubmission.project_type == project_type)
        
    # Execute Pagination
    contacts = contacts_query.order_by(ContactSubmission.created_at.desc())\
        .paginate(page=page, per_page=per_page, error_out=False)
        
    # --- Signups Query ---
    signups_query = BetaSignup.query
    
    if query:
        signups_query = signups_query.filter(BetaSignup.email.ilike(f"%{query}%"))
        
    signups = signups_query.order_by(BetaSignup.created_at.desc())\
        .paginate(page=page, per_page=per_page, error_out=False)
    
    return render_template('admin/dashboard.html', 
                         contacts=contacts, 
                         signups=signups, 
                         query=query,
                         current_type=project_type)

# Kept for API reference if needed, but protected now
@app.route('/api/admin/contacts')
@login_required
def api_admin_contacts():
    contacts = ContactSubmission.query.order_by(ContactSubmission.created_at.desc()).all()
    return jsonify([{
        'id': c.id,
        'name': c.name,
        'email': c.email,
        'created_at': c.created_at.isoformat()
    } for c in contacts])

if __name__ == '__main__':
    app.run(debug=True)
