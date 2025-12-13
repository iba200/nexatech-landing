# NexaTech Landing Page 🚀

Plateforme web officielle de **NexaTech**, une agence de développement web et SaaS basée à Dakar, Sénégal. Ce projet inclut également la landing page du produit phare **Immogest**.

## 🛠️ Stack Technique

- **Backend**: Flask (Python 3.10+)
- **Frontend**: Tailwind CSS (v3), HTML5
- **Interactivité**: HTMX, Alpine.js (supposé ou Vanilla JS)
- **Base de Données**: SQLite (Dev), PostgreSQL (Prod - compatible SQLAlchemy)
- **Emails**: Flask-Mail

## 📥 Installation

### 1. Prérequis
- Python 3.x
- Node.js & NPM (pour Tailwind CSS)
- Git

### 2. Cloner le projet
```bash
git clone https://github.com/votre-username/nexatech-landing.git
cd nexatech-landing
```

### 3. Backend (Python/Flask)
Créez un environnement virtuel et installez les dépendances :

```bash
# Windows
py -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

# Installer les paquets
pip install -r requirements.txt
```

### 4. Frontend (Tailwind CSS)
Installez les dépendances Node pour compiler le CSS :

```bash
npm install
```

## 🚀 Démarrage

### Mode Développement
Pour lancer le serveur Flask et le compilateur Tailwind en parallèle :

**Terminal 1 (Tailwind Watch) :**
```bash
npx tailwindcss -i ./static/css/input.css -o ./static/css/style.css --watch
```

**Terminal 2 (Flask Server) :**
```bash
# Windows
py app.py

# Mac/Linux
flask run --debug
```

Le site sera accessible à l'adresse : `http://127.0.0.1:5000`

## ⚙️ Configuration (Variables d'environnement)

Pour la production ou pour activer l'envoi d'emails, définissez les variables d'environnement suivantes dans un fichier `.env` ou dans votre hébergeur :

```ini
SECRET_KEY=votre-cle-secrete-tres-longue
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=votre-email@gmail.com
MAIL_PASSWORD=votre-mot-de-passe-application
MAIL_DEFAULT_SENDER=votre-email@gmail.com
```

## 📦 Déploiement

### Vercel (Recommandé)
Ce projet est prêt à être déployé sur Vercel :
1. Installez Vercel CLI : `npm i -g vercel`
2. Lancez le déploiement : `vercel`
3. Configurez les variables d'environnement dans le dashboard Vercel.

*Note : Un fichier `vercel.json` est peut-être nécessaire pour configurer le runtime Python.*

### Autres (Render, Railway)
Utilisez le `requirements.txt` et la commande de démarrage `gunicorn app:app` (ajoutez gunicorn aux requirements si nécessaire pour la prod).

## ✨ Fonctionnalités Clés

- **Navigation SPA-like** : Transitions fluides.
- **Formulaires HTMX** : Soumissions AJAX sans rechargement de page (Contact, Beta Signup).
- **Filtres Portfolio** : Filtrage dynamique des projets via HTMX.
- **Admin API Light** : Endpoints JSON pour récupérer les contacts et inscrits (à sécuriser).
- **Mockups CSS** : Visuels pure css pour la performance.

## 👥 Auteur

**NexaTech Team** - Dakar, Sénégal.
