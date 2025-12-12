# Cahier des Charges - Landing Page NexaTech 📋

## **Stack Technique Validée**
- **Backend:** Flask (Python)
- **Frontend:** Tailwind CSS + HTMX
- **Hébergement:** Vercel
- **Domaine:** nexatech.sn

---

## **1. OBJECTIFS DE LA LANDING PAGE**

### **Objectif Principal**
Présenter NexaTech comme une société tech crédible et attirer des premiers clients/leads

### **Objectifs Secondaires**
- Collecter emails pour liste beta Immogest
- Montrer expertise technique
- Établir crédibilité (portfolio, témoignages)
- SEO optimisé pour "développement web Sénégal", "création SaaS Dakar"

### **KPIs de Succès**
- 100+ visiteurs premier mois
- 10+ inscriptions newsletter/beta
- 5+ demandes de devis
- Taux de rebond < 60%

---

## **2. STRUCTURE & PAGES**

### **Pages Nécessaires**

```
nexatech.sn/
├── index.html (Homepage)
├── services.html (Nos Services)
├── produits.html (Nos Produits SaaS)
├── portfolio.html (Réalisations)
├── a-propos.html (À Propos)
├── contact.html (Contact)
└── immogest.html (Page produit Immogest - focus)
```

---

## **3. SPÉCIFICATIONS DÉTAILLÉES PAR PAGE**

### **PAGE 1: Homepage (index.html)**

#### **Section 1: Hero** 
```
[LAYOUT]
- Full viewport height
- Background gradient bleu/noir moderne
- Centré verticalement

[CONTENU]
Titre H1: "NexaTech - Solutions Tech Sur-Mesure pour l'Afrique"
Sous-titre: "Développement web, SaaS innovants et maintenance technique au Sénégal"
CTA primaire: "Découvrir nos services" (bouton bleu)
CTA secondaire: "Parler à un expert" (bouton outline)

[ÉLÉMENTS]
- Logo NexaTech (SVG, coin supérieur gauche)
- Navigation sticky (Services, Produits, Portfolio, À propos, Contact)
- Animation subtile texte (fade in)
```

#### **Section 2: Services (Aperçu)**
```
[LAYOUT]
- 3 colonnes sur desktop, 1 colonne mobile
- Cards avec hover effect

[CONTENU]
Card 1 - Développement Web
- Icône: 💻
- Titre: "Sites & Applications Web"
- Description: "Sites vitrines, e-commerce, applications métier sur-mesure"
- Lien: "En savoir plus →"

Card 2 - SaaS Sur-Mesure
- Icône: 🚀
- Titre: "Solutions SaaS"
- Description: "Développement de logiciels en ligne adaptés à vos besoins"
- Lien: "Découvrir →"

Card 3 - Maintenance
- Icône: 🔧
- Titre: "Support & Maintenance"
- Description: "Hébergement, sécurité, mises à jour et support technique"
- Lien: "Nos offres →"

[STYLE]
- Padding généreux
- Shadow au hover
- Border radius moderne
```

#### **Section 3: Produit Phare (Immogest)**
```
[LAYOUT]
- Split 50/50 desktop (image gauche, texte droite)
- Stack mobile

[CONTENU]
Badge: "Notre Premier SaaS"
Titre H2: "Immogest - Révolutionnez la gestion immobilière"
Description: 
"Automatisez la collection des loyers, gérez vos propriétés et locataires en un seul endroit. Paiements mobile money, notifications automatiques, dashboard temps réel."

Points clés (avec icônes):
✓ Paiement Orange Money/Wave intégré
✓ Dashboard propriétaire en temps réel
✓ Gestion locataires simplifiée
✓ Rappels automatiques

CTA: "Découvrir Immogest" (bouton orange)
CTA: "Rejoindre la beta" (lien)

[IMAGE]
- Mockup dashboard Immogest (screenshot ou design Figma)
- Ou illustration gestion immobilière
```

#### **Section 4: Chiffres Clés**
```
[LAYOUT]
- 4 colonnes desktop, 2x2 mobile
- Background différent (gris clair)

[CONTENU]
Stat 1: "50+" → Projets réalisés (ou prévisible)
Stat 2: "100%" → Satisfaction clients
Stat 3: "24/7" → Support disponible
Stat 4: "3+" → Années d'expérience (ajuste)

[STYLE]
- Chiffres gros (text-6xl)
- Animation counter au scroll (HTMX)
```

#### **Section 5: Pourquoi NexaTech**
```
[LAYOUT]
- Liste points avec icônes
- Centré, max-width 800px

[CONTENU]
Titre H2: "Pourquoi choisir NexaTech ?"

Points (6 max):
🎯 Expertise locale, vision internationale
💎 Code de qualité, architectures scalables
🤝 Accompagnement de A à Z
⚡ Délais respectés, transparence totale
🇸🇳 Basés à Dakar, disponibles 7j/7
🚀 Technologies modernes et performantes

[STYLE]
- Grid 2 colonnes desktop
- Icônes couleur primaire
```

#### **Section 6: Témoignages** (optionnel si tu as)
```
[LAYOUT]
- Carousel ou grid 3 colonnes
- Cards témoignages

[CONTENU PAR CARD]
- Photo client (ou avatar)
- Nom + fonction
- Société
- Texte témoignage (3-4 lignes max)
- 5 étoiles

Note: Si pas de vrais témoignages, SAUTE cette section
```

#### **Section 7: CTA Final**
```
[LAYOUT]
- Full width, background primaire (bleu)
- Centré

[CONTENU]
Titre H2: "Prêt à digitaliser votre activité ?"
Sous-titre: "Discutons de votre projet autour d'un café"
CTA: "Demander un devis gratuit" (bouton blanc)
CTA secondaire: "Appeler maintenant" (lien téléphone)

[ÉLÉMENTS]
- Affiche numéro WhatsApp
- Affiche email
```

#### **Section 8: Footer**
```
[LAYOUT]
- 4 colonnes desktop (collapse mobile)
- Background noir

[CONTENU]
Colonne 1: À propos
- Logo NexaTech
- Tagline court
- Réseaux sociaux (icônes)

Colonne 2: Services
- Développement Web
- SaaS Sur-Mesure
- Maintenance
- Consulting

Colonne 3: Produits
- Immogest
- [Bientôt]

Colonne 4: Contact
- Email: contact@nexatech.sn
- Tél: +221 XX XXX XX XX
- Adresse: Dakar, Sénégal
- WhatsApp (lien direct)

Bottom:
- © 2024 NexaTech. Tous droits réservés.
- Mentions légales | Politique de confidentialité
```

---

### **PAGE 2: Services (services.html)**

#### **Section Hero**
```
Titre H1: "Nos Services"
Sous-titre: "Des solutions techniques complètes pour votre transformation digitale"
```

#### **Service 1: Développement Web**
```
[CONTENU]
Titre H2: "Développement Web Sur-Mesure"
Description détaillée (2 paragraphes)

Sous-services:
- Sites vitrines professionnels
- E-commerce (boutiques en ligne)
- Applications web métier
- Portails & intranets
- APIs REST

Technologies utilisées:
Flask, React, Next.js, Tailwind CSS, PostgreSQL, MongoDB

Pricing indicatif:
- Site vitrine: À partir de 500,000 FCFA
- E-commerce: À partir de 1,500,000 FCFA
- Application custom: Sur devis

CTA: "Demander un devis"
```

#### **Service 2: SaaS Sur-Mesure**
```
[CONTENU]
Titre H2: "Développement SaaS Personnalisé"
Description: Création de logiciels en ligne pour automatiser vos processus

Exemples d'usage:
- Gestion de stock/inventaire
- CRM sur-mesure
- Plateformes de réservation
- Systèmes de gestion (écoles, cliniques, etc.)
- Marketplaces

Process:
1. Analyse de vos besoins
2. Prototype & validation
3. Développement itératif
4. Déploiement & formation
5. Support continu

CTA: "Parlons de votre idée"
```

#### **Service 3: Maintenance & Support**
```
[CONTENU]
Titre H2: "Maintenance & Support Technique"

Forfaits:
Basic (50,000 FCFA/mois):
- Hébergement inclus
- Mises à jour sécurité
- Monitoring 24/7
- Support email (48h)

Pro (100,000 FCFA/mois):
- Tout du Basic +
- Sauvegardes quotidiennes
- Support prioritaire (24h)
- Optimisations mensuelles
- 2h modifications/mois

Premium (200,000+ FCFA/mois):
- Tout du Pro +
- Support WhatsApp temps réel
- Modifications illimitées
- Hébergement haute performance
- SLA 99.9%

CTA: "Choisir un forfait"
```

---

### **PAGE 3: Produits (produits.html)**

#### **Section Hero**
```
Titre H1: "Nos Produits SaaS"
Sous-titre: "Des solutions innovantes pour le marché africain"
```

#### **Produit 1: Immogest** (featured)
```
[LAYOUT]
- Large card ou section complète
- Screenshots multiples

[CONTENU]
Logo Immogest
Titre: "Immogest - Gestion Immobilière Automatisée"
Tagline: "Collectez vos loyers en 2 clics"

Description complète:
"Immogest est la première plateforme sénégalaise de gestion immobilière automatisée. Conçue pour les bailleurs et gestionnaires de patrimoine, elle simplifie la collection des loyers via mobile money, la gestion des locataires et le suivi de vos propriétés."

Features:
✓ Paiement mobile money (Orange Money, Wave, Free Money)
✓ Dashboard propriétaire temps réel
✓ Rappels automatiques SMS/WhatsApp
✓ Gestion des locataires et baux
✓ Historique complet des transactions
✓ Génération automatique de reçus
✓ Signalement de problèmes par locataires
✓ Réseau de prestataires vérifiés

Pricing:
- 5% de commission sur loyers collectés
- OU Forfait 10,000 FCFA/propriété/mois
- 2 premiers mois GRATUITS

Status: Beta ouverte
CTA primaire: "Rejoindre la beta"
CTA secondaire: "Voir la démo"

[IMAGES]
- Screenshot dashboard
- Screenshot app mobile
- Video démo (optionnel)
```

#### **Produits Futurs**
```
Card 1: [Nom TBD] - Gestion Scolaire
Status: En développement
Description courte
"Notifié au lancement"

Card 2: [Nom TBD] - E-commerce
Status: Planifié
Description courte
"Notifié au lancement"
```

---

### **PAGE 4: Portfolio (portfolio.html)**

#### **Section Hero**
```
Titre H1: "Nos Réalisations"
Sous-titre: "Des projets concrets, des résultats mesurables"

[Filtre - HTMX]
Boutons: Tous | Web | SaaS | Mobile | E-commerce
```

#### **Grid Projets**
```
[LAYOUT]
- Grid 3 colonnes desktop, 1 mobile
- Cards hover effect

[STRUCTURE PAR PROJET]
- Image/screenshot projet
- Titre projet
- Client (si public) ou "Client confidentiel"
- Tags technos (badges): Flask, React, Tailwind, etc.
- Description courte (2-3 lignes)
- Lien: "Voir le projet" (modal ou page détail)

[EXEMPLES DE PROJETS]
(Ajuste selon tes vrais projets ou crée projets fictifs réalistes)

Projet 1: Immogest (Beta)
- Type: SaaS
- Screenshot: Dashboard
- Techno: Flask, React, PostgreSQL, Mobile Money APIs
- Description: "Plateforme de gestion immobilière avec paiement automatisé"

Projet 2: Site E-commerce [Nom]
- Type: E-commerce
- Screenshot
- Techno: Flask, Stripe, Tailwind
- Description: "Boutique en ligne avec gestion stock et paiements"

Projet 3: Application Gestion [Secteur]
- Type: Web App
- Screenshot
- Techno: Flask, HTMX, Chart.js
- Description: "Dashboard de gestion avec reporting temps réel"

(Ajoute 6-9 projets minimum)
```

#### **CTA Section**
```
Titre: "Votre projet sera le prochain ?"
CTA: "Discutons-en"
```

---

### **PAGE 5: À Propos (a-propos.html)**

#### **Section Story**
```
Titre H1: "À Propos de NexaTech"

[CONTENU]
Paragraphe 1: Origine
"NexaTech est née de la conviction que l'Afrique mérite des solutions tech de classe mondiale, conçues localement. Fondée à Dakar en [année], nous combinons expertise technique internationale et connaissance profonde du marché sénégalais."

Paragraphe 2: Mission
"Notre mission : démocratiser l'accès aux technologies de pointe pour les entreprises africaines, de la startup au grand groupe. Nous créons des solutions qui résolvent de vrais problèmes, pas des gadgets."

Paragraphe 3: Vision
"Devenir le partenaire tech de référence en Afrique de l'Ouest, en développant des produits SaaS qui transforment des secteurs entiers tout en accompagnant nos clients dans leur transformation digitale."
```

#### **Section Équipe** (optionnel si solo)
```
Si solo:
"NexaTech, c'est aujourd'hui [ton nom], développeur full-stack passionné avec [X] années d'expérience. Je m'entoure d'un réseau de freelances experts selon les besoins projets."

Si équipe:
Cards membres avec:
- Photo
- Nom
- Rôle
- Mini-bio (2 lignes)
- LinkedIn
```

#### **Section Valeurs**
```
Titre H2: "Nos Valeurs"

4 valeurs en grid:

1. Excellence Technique
Icône: 💎
"Code propre, architectures scalables, bonnes pratiques systématiques"

2. Transparence
Icône: 🤝
"Communication claire, pas de surprises, budgets respectés"

3. Innovation Locale
Icône: 🌍
"Solutions adaptées au contexte africain, pas de copier-coller"

4. Impact Réel
Icône: 🚀
"On mesure notre succès aux résultats de nos clients"
```

#### **Section Technologies**
```
Titre H2: "Notre Stack Technique"

Categories:

Backend:
- Python (Flask, FastAPI)
- Node.js
- PostgreSQL, MongoDB

Frontend:
- React, Next.js
- Tailwind CSS
- HTMX

Mobile:
- React Native
- Flutter

DevOps:
- Docker
- Vercel, AWS
- CI/CD

Intégrations:
- Mobile Money (Orange Money, Wave)
- Payment gateways
- APIs tierces
```

---

### **PAGE 6: Contact (contact.html)**

#### **Section Hero**
```
Titre H1: "Contactez-nous"
Sous-titre: "Discutons de votre projet autour d'un café (virtuel ou réel)"
```

#### **Section Formulaire**
```
[LAYOUT]
- Split 50/50: Formulaire gauche, Infos droite

[FORMULAIRE - HTMX]
Champs:
- Nom complet* (input text)
- Email* (input email)
- Téléphone (input tel)
- Société (input text)
- Type de projet* (select)
  Options: 
  - Site web
  - Application web
  - SaaS sur-mesure
  - Maintenance
  - Immogest (démo/beta)
  - Autre
- Budget indicatif (select)
  Options:
  - < 500,000 FCFA
  - 500,000 - 1,000,000 FCFA
  - 1,000,000 - 3,000,000 FCFA
  - 3,000,000+ FCFA
  - À discuter
- Message* (textarea, 5 lignes)
- [Checkbox] J'accepte d'être contacté par NexaTech

Bouton: "Envoyer" (HTMX submit, feedback inline)

[VALIDATION]
- HTML5 validation
- Backend validation Flask
- Messages erreur inline (HTMX)
- Success message: "Merci ! On vous contacte sous 24h"
```

#### **Section Infos Contact**
```
[CONTENU]

📧 Email
contact@nexatech.sn
hello@nexatech.sn

📱 Téléphone / WhatsApp
+221 XX XXX XX XX
(Lien direct WhatsApp)

📍 Adresse
Dakar, Sénégal
[Quartier précis si tu veux]

⏰ Disponibilité
Lun-Ven: 9h-18h
Sam: 10h-14h
Urgences: 24/7 (clients maintenance)

🌐 Réseaux Sociaux
- LinkedIn (lien)
- Facebook (lien)
- Instagram (lien)
- Twitter (lien)
```

#### **Section FAQ Rapide**
```
Titre H3: "Questions Fréquentes"

Q1: Quel est votre délai moyen ?
R: Site vitrine: 2-3 semaines. Application web: 6-12 semaines. Variable selon complexité.

Q2: Vous travaillez avec quels types de clients ?
R: Startups, PME, ONGs, entrepreneurs. De 1 à 100+ employés.

Q3: Vous proposez des facilités de paiement ?
R: Oui, paiement en plusieurs fois possible. Discutons-en.

Q4: Vous faites de la maintenance ?
R: Oui, forfaits à partir de 50,000 FCFA/mois.

Q5: Immogest est déjà disponible ?
R: En beta actuellement. Inscrivez-vous pour early access.
```

---

### **PAGE 7: Immogest (immogest.html)** - Page Dédiée

#### **Section Hero**
```
[LAYOUT]
- Background gradient orange/bleu (couleurs Immogest)
- Split 60/40 (texte/image)

[CONTENU]
Logo Immogest (grand)
Titre H1: "Collectez vos loyers en 2 clics"
Sous-titre: "La première plateforme sénégalaise de gestion immobilière automatisée"

CTA primaire: "Rejoindre la beta gratuite"
CTA secondaire: "Voir la démo (2 min)"

Badge: "🎉 Beta ouverte - 2 premiers mois gratuits"

[IMAGE]
- Mockup app mobile + dashboard
- Ou video démo en background
```

#### **Section Problème**
```
Titre H2: "Vous en avez marre de..."

Grid 3 colonnes (problèmes communs):

❌ Courir après les loyers chaque mois
❌ Gérer des dizaines d'Excel désorganisés
❌ Ne pas savoir qui a payé, qui doit
❌ Perdre des reçus papier
❌ Passer des heures en appels locataires
❌ Chercher un plombier à 23h pour urgence

Texte: "Immogest résout tout ça. Automatiquement."
```

#### **Section Solution**
```
Titre H2: "Comment Immogest transforme votre gestion"

[FEATURE 1]
Icône: 💰
Titre: "Collection Automatique"
Description: "Vos locataires paient en 2 clics via Orange Money, Wave ou Free Money. Vous recevez l'argent instantanément. Rappels automatiques 3 jours avant échéance."
Image: Screenshot paiement mobile

[FEATURE 2]
Icône: 📊
Titre: "Dashboard Temps Réel"
Description: "Visualisez tous vos loyers, paiements, retards en un coup d'œil. Graphiques clairs, exports Excel en 1 clic. Accès mobile et web."
Image: Screenshot dashboard

[FEATURE 3]
Icône: 👥
Titre: "Gestion Locataires Simplifiée"
Description: "Fiches locataires complètes, historique paiements, documents de bail stockés. Génération automatique de quittances et reçus."
Image: Screenshot gestion locataires

[FEATURE 4]
Icône: 🔧
Titre: "Maintenance Intégrée"
Description: "Locataire signale un problème dans l'app. Système dispatche un prestataire vérifié. Vous suivez l'intervention en temps réel."
Image: Screenshot tickets

[FEATURE 5]
Icône: 📱
Titre: "Communication Centralisée"
Description: "Chat intégré bailleur-locataire. Notifications SMS/WhatsApp automatiques. Historique complet accessible."
Image: Screenshot messagerie

[FEATURE 6]
Icône: 📈
Titre: "Reporting Intelligent"
Description: "Taux de collecte, revenus mensuels, tendances. Prêt pour votre comptable ou la banque."
Image: Screenshot rapports
```

#### **Section Pricing**
```
Titre H2: "Tarification Simple et Transparente"

[OPTION 1 - Recommandée]
Titre: "Commission"
Prix: 5% sur loyers collectés
Description: "Vous payez uniquement sur ce qui est collecté"
Exemple: "Loyer 200,000 FCFA → Vous payez 10,000 FCFA"
Inclus:
✓ Toutes les fonctionnalités
✓ Support WhatsApp
✓ Mises à jour gratuites
✓ Formation incluse
Badge: "Le plus populaire"

[OPTION 2]
Titre: "Forfait"
Prix: 10,000 FCFA/propriété/mois
Description: "Pas de commission, tarif fixe"
Inclus:
✓ Toutes les fonctionnalités
✓ Support prioritaire
✓ Idéal pour petits loyers

[OFFRE SPÉCIALE]
"🎁 Beta : 2 premiers mois GRATUITS"
"Aucune carte bancaire requise"

CTA: "Commencer gratuitement"
```

#### **Section Témoignages** (si tu as beta testers)
```
3 témoignages courts de bailleurs beta
Sinon: skip ou mets "Témoignages bientôt disponibles"
```

#### **Section FAQ Immogest**
```
Titre H2: "Questions Fréquentes"

Q: C'est vraiment gratuit les 2 premiers mois ?
R: Oui, totalement. Aucune carte bancaire demandée. Vous annulez quand vous voulez.

Q: Mes locataires doivent installer une app ?
R: Oui, une app mobile simple (2 minutes d'installation). On les forme.

Q: Et si mes locataires n'ont pas de smartphone ?
R: Ils peuvent payer via code USSD (comme Orange Money classique).

Q: Vous touchez mon argent ?
R: Non. Les loyers vont directement sur votre compte mobile money. On ne touche jamais votre argent.

Q: Je peux arrêter quand je veux ?
R: Oui, aucun engagement. Cancel en 1 clic depuis votre dashboard.

Q: Vous gérez combien de propriétés max ?
R: Illimité. De 1 à 1000+ propriétés.

Q: Support technique disponible ?
R: Oui, WhatsApp 7j/7 pendant la beta. Email 24/7.

Q: Mes données sont sécurisées ?
R: Oui. Chiffrement bancaire, hébergement sécurisé, backups quotidiens.
```

#### **Section CTA Final**
```
Background: Orange vif
Titre H2: "Rejoignez les bailleurs modernes"
Sous-titre: "2 premiers mois gratuits • Configuration en 10 minutes • Support inclus"

Formulaire inline:
- Email
- Nombre de propriétés (select)
- Bouton "Commencer gratuitement"

Texte petit: "En vous inscrivant, vous acceptez nos CGU et Politique de confidentialité"
```

---

## **4. COMPOSANTS RÉUTILISABLES**

### **Navigation (Component)**
```html
Sticky top
Logo NexaTech (gauche)
Menu desktop (centre):
- Services
- Produits
- Portfolio
- À Propos
- Contact

Bouton CTA (droite): "Démo Immogest" (orange)

Mobile: Hamburger menu → slide-in
```

### **Boutons (Variants)**
```
.btn-primary (bleu, hover plus foncé)
.btn-secondary (outline bleu)
.btn-accent (orange - pour Immogest)
.btn-ghost (transparent, border)

Toujours:
- Padding généreux (px-6 py-3)
- Border radius (rounded-lg)
- Transition smooth
- Disabled state
- Loading state (spinner HTMX)
```

### **Cards (Variants)**
```
.card-service (shadow, hover lift)
.card-project (image top, content bottom)
.card-testimonial (quote icon, text, author)
.card-pricing (border accent, featured highlighted)
```

### **Form Input (Component)**
```
Label au-dessus
Input avec border
Focus state (border couleur primaire)
Error state (border rouge, message dessous)
Success state (border vert, checkmark)
```

### **Section Container**
```
Max-width: 1280px
Padding horizontal: px-4 md:px-8
Margin: centré
Spacing vertical: py-16 md:py-24
```

---

## **5. FONCTIONNALITÉS HTMX**

### **Formulaire Contact (HTMX)**
```python
# Route Flask
@app.route('/contact', methods=['POST'])
def contact():
    # Validation
    # Envoi email
    # Sauvegarde DB
    return """
    <div class="success-message">
        Merci ! On vous contacte sous 24h.
    </div>
    """
```

```html
<!-- HTML -->
<form hx-post="/contact" 
      hx-target="#form-feedback"
      hx-swap="innerHTML">
    <!-- champs -->
    <button type="submit">Envoyer</button>
</form>
<div id="form-feedback"></div>
```

### **Portfolio Filter (HTMX)**
```python
@app.route('/portfolio/filter/<category>')
def filter_portfolio(category):
    projects = get_projects(category)
    return render_template('partials/projects_grid.html', projects=projects)
```

```html
<button hx-get="/portfolio/filter/web" 
        hx-target="#projects-grid"
        hx-swap="innerHTML">
    Web
</button>
```

### **Inscription Beta Immogest (HTMX)**
```python
@app.route('/immogest/beta', methods=['POST'])
def beta_signup():
    email = request.form.get('email')
    properties = request.form.get('properties')
    # Save to DB
    # Send confirmation email
    return "<div class='success'>Inscription confirmée ! Check vos emails.</div>"
```

### **Scroll Animations (Intersection Observer + HTMX)**
```html
<div hx-trigger="revealed" 
     hx-get="/stats/counter"
     class="fade-in">
    <!-- Stats apparaissent au scroll -->
</div>
```

---

## **6. STYLE GUIDE TAILWIND**

### **Couleurs (tailwind.config.js)**
```javascript
colors: {
  primary: {
    50: '#eff6ff',
    100: '#dbeafe',
    500: '#3b82f6', // Bleu principal
    600: '#2563eb',
    700: '#1d4ed8',
    900: '#1e3a8a',
  },
  accent: {
    500: '#f97316', // Orange Immogest
    600: '#ea580c',
  },
  dark: {
    800: '#1e293b',
    900: '#0f172a',
  }
}
```

### **Typographie**
```
Titres:
- H1: text-5xl md:text-6xl font-bold
- H2: text-4xl md:text-5xl font-bold
- H3: text-3xl font-semibold
- H4: text-2xl font-semibold

Body:
- Base: text-base (16px)
- Large: text-lg
- Small: text-sm

Font family: 
- Inter (Google Fonts) pour UI
- ou system-ui stack
```

### **Spacing**
```
Sections: py-16 md:py-24
Cards gap: gap-8
Containers: px-4 md:px-8
Max-width: max-w-7xl
```

### **Responsive**
```
Mobile-first approach:

Base: mobile (< 640px)
sm: 640px
md: 768px
lg: 1024px
xl: 1280px
```

---

## **7. STRUCTURE FICHIERS**

```
nexatech-landing/
├── app.py (Flask main)
├── requirements.txt
├── vercel.json (config Vercel)
├── .env (variables environnement)
├── static/
│   ├── css/
│   │   └── output.css (Tailwind compiled)
│   ├── js/
│   │   ├── htmx.min.js
│   │   └── main.js (custom JS si besoin)
│   └── images/
│       ├── logo.svg
│
├── hero-bg.jpg
│       ├── immogest-dashboard.png
│       └── projects/ (screenshots projets)
├── templates/
│   ├── base.html (template parent)
│   ├── components/
│   │   ├── nav.html
│   │   ├── footer.html
│   │   ├── button.html
│   │   └── card.html
│   ├── pages/
│   │   ├── index.html
│   │   ├── services.html
│   │   ├── produits.html
│   │   ├── portfolio.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   └── immogest.html
│   └── partials/ (HTMX partials)
│       ├── projects_grid.html
│       └── contact_form_success.html
└── utils/
    ├── email.py (envoi emails)
    └── db.py (database helpers si besoin)
```

---

## **8. CONFIGURATION TECHNIQUE**

### **requirements.txt**
```
Flask==3.0.0
python-dotenv==1.0.0
flask-mail==0.9.1 (pour emails)
gunicorn==21.2.0 (pour Vercel)
```

### **vercel.json**
```json
{
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    },
    {
      "src": "static/**",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

### **Tailwind Setup**
```bash
# tailwind.config.js
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        // couleurs custom
      }
    }
  }
}

# Build command
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
```

### **.env**
```
FLASK_ENV=production
SECRET_KEY=your-secret-key
MAIL_SERVER=smtp.gmail.com (si emails)
MAIL_PORT=587
MAIL_USERNAME=contact@nexatech.sn
MAIL_PASSWORD=your-password
```

---

## **9. SEO & PERFORMANCE**

### **Meta Tags (base.html)**
```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- SEO -->
    <title>{% block title %}NexaTech - Solutions Tech au Sénégal{% endblock %}</title>
    <meta name="description" content="{% block description %}Développement web, SaaS et maintenance au Sénégal{% endblock %}">
    <meta name="keywords" content="développement web Sénégal, SaaS Dakar, création site web">
    
    <!-- Open Graph -->
    <meta property="og:title" content="NexaTech">
    <meta property="og:description" content="Solutions tech sur-mesure">
    <meta property="og:image" content="/static/images/og-image.jpg">
    <meta property="og:url" content="https://nexatech.sn">
    
    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    
    <!-- Favicon -->
    <link rel="icon" href="/static/images/favicon.ico">
    
    <!-- CSS -->
    <link rel="stylesheet" href="/static/css/output.css">
    
    <!-- HTMX -->
    <script src="/static/js/htmx.min.js"></script>
</head>
```

### **Performance**
```
- Images: WebP format, lazy loading
- CSS: Purge Tailwind (production)
- JS: Minimisé, defer loading
- Fonts: Preload critical fonts
- Caching headers (Flask-Caching)
```

### **Analytics**
```html
<!-- Google Analytics (optionnel) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
```

---

## **10. CHECKLIST PRÉ-LANCEMENT**

### **Contenu**
- [ ] Tous les textes finaux en place
- [ ] Images optimisées (< 200KB chacune)
- [ ] Logo haute qualité (SVG ou PNG)
- [ ] Screenshots Immogest (ou mockups)
- [ ] Photos projets portfolio (min 6)
- [ ] Témoignages (si disponibles)
- [ ] Coordonnées contact à jour
- [ ] Liens réseaux sociaux fonctionnels

### **Technique**
- [ ] Formulaire contact fonctionne
- [ ] Emails envoyés correctement
- [ ] HTMX interactions testées
- [ ] Responsive mobile parfait
- [ ] Performance score >90 (Lighthouse)
- [ ] SEO meta tags toutes pages
- [ ] Sitemap.xml généré
- [ ] robots.txt configuré
- [ ] 404 page custom
- [ ] SSL/HTTPS actif
- [ ] Domain nexatech.sn pointé

### **Legal**
- [ ] Mentions légales
- [ ] Politique confidentialité
- [ ] CGU (si e-commerce/SaaS)
- [ ] Cookies banner (si EU traffic)

### **Marketing**
- [ ] Google My Business créé
- [ ] Google Search Console setup
- [ ] Google Analytics (optionnel)
- [ ] Facebook Pixel (optionnel)
- [ ] Schema.org markup (LocalBusiness)

---

## **11. TIMELINE DE DÉVELOPPEMENT**

### **Semaine 1 : Setup & Design**
**Jour 1-2 :**
- Setup projet Flask
- Config Tailwind
- Structure fichiers
- Design système (couleurs, typo)

**Jour 3-5 :**
- Design Figma/wireframes (optionnel mais recommandé)
- Composants réutilisables
- Template base.html

**Jour 6-7 :**
- Page homepage (80% complète)
- Navigation + footer

### **Semaine 2 : Pages Principales**
**Jour 8-10 :**
- Page Services (complète)
- Page Produits (complète)
- Page Immogest (complète)

**Jour 11-13 :**
- Page Portfolio
- Page À propos
- Page Contact + formulaire HTMX

**Jour 14 :**
- Responsive mobile toutes pages
- Testing cross-browser

### **Semaine 3 : Polish & Deploy**
**Jour 15-17 :**
- Optimisation images
- SEO meta tags
- Performance optimization
- Contenu final

**Jour 18-19 :**
- Testing complet
- Fix bugs
- Legal pages (mentions, confidentialité)

**Jour 20-21 :**
- Deploy Vercel
- Config domaine nexatech.sn
- Test production
- Lancement ! 🚀

---

## **12. APRÈS LE LANCEMENT**

### **Semaine 1 post-launch**
- Monitor analytics
- Fix bugs urgents
- Collecter premiers feedbacks

### **Mois 1**
- A/B test CTAs
- Ajouter blog (optionnel)
- SEO local optimize
- Google My Business posts

### **Mois 2-3**
- Ajouter nouveaux projets portfolio
- Témoignages clients
- Case studies détaillées
- Content marketing (articles)

---

## **RESSOURCES & LIENS UTILES**

### **Design Inspiration**
- https://tailwindui.com/components (composants Tailwind)
- https://www.awwwards.com (inspiration design)
- https://dribbble.com/tags/landing-page (designs landing)

### **Images Gratuites**
- https://unsplash.com (photos haute qualité)
- https://www.pexels.com
- https://undraw.co (illustrations SVG)
- https://heroicons.com (icônes)

### **Outils**
- https://tailwindcss.com/docs (doc Tailwind)
- https://htmx.org/docs (doc HTMX)
- https://flask.palletsprojects.com (doc Flask)
- https://pagespeed.web.dev (test performance)

### **Fonts**
- https://fonts.google.com
  - Inter (recommandé)
  - Poppins
  - Work Sans

---

## **RÉSUMÉ ACTIONS IMMÉDIATES**

**Aujourd'hui :**
1. ✅ Créer dossier projet
2. ✅ Setup Flask + Tailwind
3. ✅ Créer structure fichiers
4. ✅ Design logo simple (Canva)

**Cette semaine :**
1. ✅ Code homepage complète
2. ✅ Navigation + footer
3. ✅ Page Immogest (priorité)
4. ✅ Responsive mobile

**Semaine prochaine :**
1. ✅ Autres pages
2. ✅ Formulaires HTMX
3. ✅ Deploy Vercel
4. ✅ LANCEMENT ! 🎉

---

**Tu veux que je te crée le code de démarrage (app.py + base.html + config Tailwind) en artifact pour démarrer immédiatement ?**