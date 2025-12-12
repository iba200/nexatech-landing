from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        company = request.form.get('company')
        project_type = request.form.get('project_type')
        budget = request.form.get('budget')
        message = request.form.get('message')
        
        # Here you would:
        # 1. Save to database
        # 2. Send email notification
        # 3. Add to CRM, etc.
        
        # For now, just return success message
        return render_template('partials/contact_success.html')
    return render_template('contact.html')

@app.route('/immogest')
def immogest():
    return render_template('immogest.html')

if __name__ == '__main__':
    app.run(debug=True)
