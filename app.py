from flask import Flask, render_template, request

app = Flask(__name__)

# رقم الواتساب المؤقت (عدّله لاحقاً برقمك المغربي بصيغة 2126XXXXXXXX)
WHATSAPP_NUMBER = "212600000000"
INSTAGRAM_URL = "https://www.instagram.com/bistouria.ma"
CONTACT_EMAIL = "bistouria.ma@gmail.com"

CONTENT = {
    "fr": {
        "lang_code": "fr",
        "switch_label": "English",
        "switch_url": "/?lang=en",
        "badge": "Simulation Médicale & Chirurgicale — Maroc",
        "hero_title": "Maîtrisez vos gestes chirurgicaux avant vos stages cliniques",
        "hero_sub": "Kits complets de suture chirurgicale et coussinets en silicone 3 couches conçus pour les étudiants en Médecine et Sciences Infirmières.",
        "cta_primary": "Commander maintenant",
        "cta_secondary": "Voir les produits",
        "trust_1": "Paiement à la livraison (COD)",
        "trust_2": "Livraison rapide 24h–48h partout au Maroc",
        "trust_3": "Vérification avant paiement",

        # Section Contenu du Kit
        "kit_box_title": "Que contient le Kit Complet Bistouria ?",
        "kit_box_sub": "Tout le matériel nécessaire pour pratiquer les points simples, Blair-Donati, surjets et nœuds chirurgicaux.",
        "item_1_title": "5 Instruments en Acier Inoxydable",
        "item_1_desc": "Porte-aiguille Mayo-Hegar, pince à disséquer Adson, ciseaux Iris, pince hémostatique et manche de bistouri N°3.",
        "item_2_title": "Coussinet Silicone 3 Couches",
        "item_2_desc": "Simulation réaliste (épiderme, tissu adipeux, muscle) avec maille de renfort anti-déchirure.",
        "item_3_title": "Consommables & Trousse Zippée",
        "item_3_desc": "5 fils de suture stériles avec aiguilles courbes + 5 lames de bistouri + trousse de transport rigide.",

        # Section Produits
        "products_title": "Nos Produits & Modèles",
        "products_sub": "Choisissez le kit complet ou le coussinet d'entraînement adapté à votre niveau.",
        "kit_name": "Kit de Suture Chirurgicale Complet",
        "kit_desc": "Trousse zippée + 5 instruments inox + Coussinet silicone 14 plaies (3 couches) + 5 fils + 5 lames.",
        "kit_price": 250,

        "pad1_name": "Coussinet Silicone — Modèle 1 (Classique 14 Plaies)",
        "pad1_desc": "14 incisions variées (droites, courbes, en V et en Y). Idéal pour débuter et maîtriser les points de base.",
        "pad2_name": "Coussinet Silicone — Modèle 2 (Incisions Multi-angles)",
        "pad2_desc": "Conçu pour s'entraîner sur les plaies complexes, sutures d'angles et tensions asymétriques.",
        "pad3_name": "Coussinet Silicone — Modèle 3 (Plaies Profondes & Larges)",
        "pad3_desc": "Parfait pour pratiquer les sutures en deux plans (plan profond sous-cutané et plan superficiel).",
        "pad4_name": "Coussinet Silicone — Modèle 4 (Entraînement Avancé)",
        "pad4_desc": "Texture haute densité avec découpes chirurgicales diversifiées pour une pratique intensive avant examen.",
        "pad_price": 85,
        "currency": "MAD",
        "select_btn": "Sélectionner",

        # Comparatif des packs
        "comparison_title": "Quel pack choisir pour vos stages ?",
        "comparison_single": "Coussinet Individuel",
        "comparison_single_includes": "Un coussinet en silicone",
        "comparison_single_ideal": "Étudiants ayant déjà les instruments",
        "comparison_kit": "Kit Complet de Suture",
        "comparison_kit_includes": "Coussinet silicone 3 couches + instruments en acier inoxydable + fils de suture + trousse de transport",
        "comparison_kit_ideal": "Pour commencer à pratiquer avec tout le nécessaire",
        "comparison_recommended": "Recommandé",
        "comparison_bundle": "Pack 2 Coussinets",
        "comparison_bundle_includes": "Deux coussinets en silicone différents avec des motifs de plaies variés",
        "comparison_bundle_ideal": "Préparation intensive aux examens ou partage avec un camarade",
        "comparison_includes_label": "Comprend",
        "comparison_ideal_label": "Idéal pour",
        "comparison_choose": "Choisir ce pack",

        # Techniques chirurgicales
        "techniques_title": "Maîtrisez les sutures essentielles avant vos stages",
        "technique_simple_name": "Point simple séparé",
        "technique_simple_desc": "Ferme une plaie avec des points séparés et réguliers.",
        "technique_continuous_name": "Surjet continu",
        "technique_continuous_desc": "Ferme rapidement les plaies linéaires avec un fil continu.",
        "technique_blair_name": "Point de Blair-Donati",
        "technique_blair_desc": "Maintient les berges éversées sous une forte tension.",
        "technique_knot_name": "Nœud de chirurgien",
        "technique_knot_desc": "Un nœud renforcé qui limite le desserrage des sutures.",
        "level_beginner": "Débutant",
        "level_intermediate": "Intermédiaire",
        "level_advanced": "Avancé",
        "techniques_instagram_cta": "Suivez nos démonstrations vidéo réelles sur @bistouria.ma",

        # Section FAQ
        "faq_title": "Questions Fréquentes (FAQ)",
        "faq_1_q": "Puis-je vérifier le kit avant de payer ?",
        "faq_1_a": "Oui. À Tanger, nous proposons une remise en main propre avec vérification complète du contenu. Pour les autres villes, le paiement s'effectue à la livraison (Cash on Delivery).",
        "faq_2_q": "Le coussinet en silicone est-il réutilisable ?",
        "faq_2_a": "Oui, grâce à sa structure en 3 couches renforcée, chaque coussinet supporte des dizaines de séances d'entraînement si vous retirez délicatement les fils.",
        "faq_3_q": "Quels sont les délais de livraison au Maroc ?",
        "faq_3_a": "24h sur Tanger, et entre 24h et 48h ouvrables vers Rabat, Casablanca, Fès, Marrakech, Agadir, Oujda et toutes les villes du Maroc.",

        # Formulaire
        "form_title": "Passer votre commande",
        "form_sub": "Remplissez vos informations, nous confirmons votre commande sur WhatsApp.",
        "lbl_product": "Produit souhaité",
        "opt_kit": "Kit Complet de Suture",
        "opt_pad": "Coussinet Individuel",
        "opt_pack": "Pack 2 Coussinets",
        "lbl_name": "Nom et Prénom",
        "ph_name": "Ex: Youssef Alami",
        "lbl_city": "Ville",
        "city_placeholder": "Sélectionnez votre ville",
        "lbl_phone": "Numéro de téléphone (WhatsApp)",
        "ph_phone": "Ex: 06XXXXXXXX",
        "city_other": "Autre",
        "wa_greeting": "Bonjour Bistouria.ma, je souhaite commander :",
        "wa_name": "Nom",
        "wa_phone": "Téléphone",
        "wa_city": "Ville",
        "wa_product": "Produit",
        "submit_btn": "Commander via WhatsApp",
        "footer_note": "Usage éducatif et simulation médicale uniquement."
    },
    "en": {
        "lang_code": "en",
        "switch_label": "Français",
        "switch_url": "/?lang=fr",
        "badge": "Medical & Surgical Simulation — Morocco",
        "hero_title": "Master Your Surgical Suturing Skills Before Clinical Rotations",
        "hero_sub": "Complete surgical suture kits and 3-layer silicone practice pads designed for Medical and Nursing students.",
        "cta_primary": "Order Now",
        "cta_secondary": "Explore Products",
        "trust_1": "Cash on Delivery (COD)",
        "trust_2": "Fast 24h-48h delivery in Morocco",
        "trust_3": "Inspect before paying",

        # Kit Content Section
        "kit_box_title": "What's Inside the Complete Bistouria Kit?",
        "kit_box_sub": "Everything you need to practice simple interrupted, mattress, continuous sutures, and surgical knots.",
        "item_1_title": "5 Stainless Steel Instruments",
        "item_1_desc": "Mayo-Hegar needle holder, Adson tissue forceps, Iris scissors, hemostat forceps, and #3 scalpel handle.",
        "item_2_title": "3-Layer Silicone Practice Pad",
        "item_2_desc": "Realistic anatomical layers (skin, fat, muscle) with an anti-tear protective mesh.",
        "item_3_title": "Consumables & Zipped Case",
        "item_3_desc": "5 sterile suture threads with curved needles + 5 surgical blades + durable carrying case.",

        # Products Section
        "products_title": "Our Products & Models",
        "products_sub": "Choose the complete kit or the practice pad model suited to your training level.",
        "kit_name": "Complete Surgical Suture Kit",
        "kit_desc": "Zipped case + 5 stainless steel instruments + 14-wound 3-layer silicone pad + 5 threads + 5 blades.",
        "kit_price": 250,

        "pad1_name": "Silicone Pad — Model 1 (Classic 14 Wounds)",
        "pad1_desc": "14 pre-cut wounds (straight, curved, V-shape, Y-shape). Ideal for beginners mastering basic stitches.",
        "pad2_name": "Silicone Pad — Model 2 (Multi-Angle Incisions)",
        "pad2_desc": "Designed for practicing complex wound closures, corner stitches, and asymmetric tension.",
        "pad3_name": "Silicone Pad — Model 3 (Deep & Wide Wounds)",
        "pad3_desc": "Perfect for practicing two-layer closures (deep subcutaneous and superficial skin layers).",
        "pad4_name": "Silicone Pad — Model 4 (Advanced Training)",
        "pad4_desc": "High-density texture with diverse surgical incisions for intensive OSCE & clinical prep.",
        "pad_price": 85,
        "currency": "MAD",
        "select_btn": "Select",

        # Pack comparison
        "comparison_title": "Which kit is right for your clinical rotations?",
        "comparison_single": "Single Silicone Pad",
        "comparison_single_includes": "One silicone pad",
        "comparison_single_ideal": "Students who already own surgical instruments",
        "comparison_kit": "Complete Suture Kit",
        "comparison_kit_includes": "3-layer silicone pad + stainless steel instruments + suture threads + carrying pouch",
        "comparison_kit_ideal": "Complete practice from scratch",
        "comparison_recommended": "Most Popular",
        "comparison_bundle": "2-Pad Bundle",
        "comparison_bundle_includes": "Two different silicone pads with varied wound patterns",
        "comparison_bundle_ideal": "Intensive exam preparation or sharing with a classmate",
        "comparison_includes_label": "Includes",
        "comparison_ideal_label": "Ideal for",
        "comparison_choose": "Choose this pack",

        # Surgical techniques
        "techniques_title": "Master essential surgical sutures before your rotations",
        "technique_simple_name": "Simple Interrupted Suture",
        "technique_simple_desc": "Closes a wound with separate, evenly spaced stitches.",
        "technique_continuous_name": "Continuous Running Suture",
        "technique_continuous_desc": "Quickly closes linear wounds with one continuous thread.",
        "technique_blair_name": "Vertical Mattress (Blair-Donati)",
        "technique_blair_desc": "Keeps wound edges everted under significant tension.",
        "technique_knot_name": "Surgeon's Knot",
        "technique_knot_desc": "A reinforced knot that helps prevent sutures from loosening.",
        "level_beginner": "Beginner",
        "level_intermediate": "Intermediate",
        "level_advanced": "Advanced",
        "techniques_instagram_cta": "Watch real suturing video demos on @bistouria.ma",

        # FAQ Section
        "faq_title": "Frequently Asked Questions (FAQ)",
        "faq_1_q": "Can I inspect the kit before paying?",
        "faq_1_a": "Yes. In Tangier, we offer local hand-delivery with full inspection. For other cities, you pay Cash on Delivery (COD).",
        "faq_2_q": "Is the silicone pad reusable?",
        "faq_2_a": "Yes, thanks to its reinforced 3-layer structure, each pad withstands dozens of practice sessions when sutures are removed carefully.",
        "faq_3_q": "How fast is delivery across Morocco?",
        "faq_3_a": "24h in Tangier, and 24h to 48h business days to Rabat, Casablanca, Fez, Marrakech, Agadir, Oujda, and all Moroccan cities.",

        # Form
        "form_title": "Place Your Order",
        "form_sub": "Fill in your details below to confirm your order directly via WhatsApp.",
        "lbl_product": "Select Product",
        "opt_kit": "Complete Suture Kit",
        "opt_pad": "Individual Practice Pad",
        "opt_pack": "Pack of 2 Pads",
        "lbl_name": "Full Name",
        "ph_name": "Ex: Youssef Alami",
        "lbl_city": "City",
        "city_placeholder": "Select your city",
        "lbl_phone": "Phone Number (WhatsApp)",
        "ph_phone": "Ex: 06XXXXXXXX",
        "city_other": "Other",
        "wa_greeting": "Hello Bistouria.ma, I would like to place an order:",
        "wa_name": "Name",
        "wa_phone": "Phone",
        "wa_city": "City",
        "wa_product": "Product",
        "submit_btn": "Order via WhatsApp",
        "footer_note": "For educational and medical simulation use only."
    }
}

@app.route("/")
def index():
    lang = request.args.get("lang", "fr")
    if lang not in CONTENT:
        lang = "fr"
    return render_template(
        "index.html",
        t=CONTENT[lang],
        whatsapp=WHATSAPP_NUMBER,
        instagram=INSTAGRAM_URL,
        email=CONTACT_EMAIL
    )

if __name__ == "__main__":
    app.run(debug=True)