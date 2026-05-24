"""
CropSense — AI Crop Disease Detector
Built by Mokshi Jain
"""

import os
import numpy as np
import streamlit as st
from PIL import Image

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CropSense — AI Crop Doctor",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "page" not in st.session_state:
    st.session_state.page = "Home"

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL CSS
# Palette: --yellow #F5C518, --green #2D6A4F, --green-light #52B788,
#          --green-pale #D8F3DC, --off-white #F9FAF7, --black #111
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Outfit:wght@300;400;500;600&display=swap');

:root {
    --yellow:       #F5C518;
    --yellow-pale:  #FFFBE8;
    --yellow-mid:   #E6B800;
    --green:        #2D6A4F;
    --green-mid:    #40916C;
    --green-light:  #52B788;
    --green-pale:   #D8F3DC;
    --off-white:    #F9FAF7;
    --white:        #FFFFFF;
    --black:        #111111;
    --ink:          #222222;
    --muted:        #555555;
    --line:         #E4EBE6;
    --shadow:       rgba(45,106,79,0.08);
}

* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { font-family: 'Outfit', sans-serif; }
h1, h2, h3, h4 { font-family: 'Playfair Display', serif; }

/* ── APP BACKGROUND ── */
.stApp {
    background: var(--off-white);
}
.block-container {
    padding: 0 2.5rem 4rem !important;
    max-width: 1240px !important;
    margin: 0 auto !important;
}
#MainMenu, footer, header { visibility: hidden; }

/* ── SIDEBAR ── */
section[data-testid="stSidebar"] {
    background: var(--green) !important;
    border-right: none !important;
    min-width: 240px !important;
    max-width: 240px !important;
}
section[data-testid="stSidebar"] > div:first-child {
    padding-top: 0 !important;
}
/* Hide the collapse/toggle button */
button[data-testid="collapsedControl"],
button[kind="header"] {
    display: none !important;
}
section[data-testid="stSidebar"] * {
    color: rgba(255,255,255,0.88) !important;
    font-family: 'Outfit', sans-serif !important;
}
section[data-testid="stSidebar"] .stRadio > label { display: none !important; }
section[data-testid="stSidebar"] .stRadio [role="radiogroup"] label {
    display: flex !important;
    align-items: center !important;
    background: transparent !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.7rem 1.1rem !important;
    margin-bottom: 0.2rem !important;
    font-size: 0.88rem !important;
    cursor: pointer !important;
    transition: background 0.15s !important;
    color: rgba(255,255,255,0.75) !important;
    letter-spacing: 0.01em !important;
}
section[data-testid="stSidebar"] .stRadio [role="radiogroup"] label:hover {
    background: rgba(255,255,255,0.1) !important;
    color: white !important;
}
section[data-testid="stSidebar"] .stRadio [role="radiogroup"] [aria-checked="true"] {
    background: rgba(245,197,24,0.18) !important;
    color: var(--yellow) !important;
}
section[data-testid="stSidebar"] hr {
    border: none !important;
    border-top: 1px solid rgba(255,255,255,0.12) !important;
    margin: 1rem 0 !important;
}
.sb-brand {
    padding: 2rem 1.2rem 1.6rem;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 1rem;
}
.sb-brand-name {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.45rem !important;
    font-weight: 700 !important;
    color: white !important;
    letter-spacing: -0.3px;
    line-height: 1;
}
.sb-brand-sub {
    font-size: 0.68rem !important;
    letter-spacing: 0.14em !important;
    text-transform: uppercase !important;
    color: rgba(255,255,255,0.4) !important;
    margin-top: 0.3rem;
}
.sb-nav-label {
    font-size: 0.65rem !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
    color: rgba(255,255,255,0.35) !important;
    padding: 0 1.1rem !important;
    margin-bottom: 0.4rem !important;
    display: block !important;
}
.sb-helpline {
    margin: 0 1rem 0.5rem;
    background: rgba(245,197,24,0.12);
    border-left: 3px solid var(--yellow);
    border-radius: 6px;
    padding: 0.8rem 1rem;
}
.sb-helpline-num {
    color: white !important;
    font-size: 1.15rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px;
}
.sb-helpline-label {
    color: var(--yellow) !important;
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.05em !important;
    text-transform: uppercase !important;
}
.sb-helpline-sub {
    color: rgba(255,255,255,0.4) !important;
    font-size: 0.68rem !important;
    margin-top: 0.15rem !important;
}
.sb-footer {
    padding: 1rem 1.2rem 0.5rem;
    border-top: 1px solid rgba(255,255,255,0.08);
}
.sb-footer-text {
    color: rgba(255,255,255,0.3) !important;
    font-size: 0.7rem !important;
    line-height: 1.7 !important;
}
.sb-footer-text a {
    color: var(--yellow) !important;
    text-decoration: none !important;
}

/* ── PAGE HEADER ── */
.page-header {
    padding: 2.8rem 0 2rem;
    border-bottom: 1px solid var(--line);
    margin-bottom: 2.5rem;
}
.page-header-chip {
    display: inline-block;
    background: var(--green-pale);
    color: var(--green);
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 0.3rem 0.9rem;
    border-radius: 2rem;
    margin-bottom: 1rem;
}
.page-header h1 {
    font-size: clamp(2rem, 4vw, 3rem) !important;
    color: var(--black) !important;
    line-height: 1.1 !important;
    letter-spacing: -0.5px !important;
    margin-bottom: 0.7rem !important;
}
.page-header h1 em { color: var(--green-mid); font-style: italic; }
.page-header p {
    color: var(--muted);
    font-size: 1rem;
    max-width: 560px;
    line-height: 1.7;
}

/* ── HERO BANNER ── */
.hero {
    background: var(--green);
    border-radius: 16px;
    padding: 3.5rem;
    margin-bottom: 2.5rem;
    position: relative;
    overflow: hidden;
}
.hero::after {
    content: '🌿';
    position: absolute;
    right: 3rem;
    top: 50%;
    transform: translateY(-50%);
    font-size: 9rem;
    opacity: 0.07;
    pointer-events: none;
}
.hero-chip {
    display: inline-block;
    background: var(--yellow);
    color: var(--black);
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    padding: 0.3rem 0.9rem;
    border-radius: 2rem;
    margin-bottom: 1.4rem;
}
.hero h1 {
    font-family: 'Playfair Display', serif;
    color: white !important;
    font-size: clamp(2rem, 3.8vw, 3.2rem) !important;
    line-height: 1.1 !important;
    letter-spacing: -0.4px !important;
    margin-bottom: 1rem !important;
}
.hero h1 em { color: var(--yellow); font-style: italic; }
.hero-desc {
    color: rgba(255,255,255,0.75);
    font-size: 0.97rem;
    line-height: 1.8;
    max-width: 500px;
    margin-bottom: 0.5rem;
}
.hero-hi {
    color: rgba(255,255,255,0.4);
    font-size: 0.85rem;
    margin-top: 0.4rem;
}

/* ── STAT CARDS ── */
.stat-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.2rem;
    margin-bottom: 2.5rem;
}
.stat-card {
    background: var(--white);
    border-radius: 12px;
    padding: 1.6rem;
    border: 1px solid var(--line);
    border-top: 3px solid var(--yellow);
}
.stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    font-weight: 700;
    color: var(--black);
    line-height: 1;
    margin-bottom: 0.4rem;
}
.stat-label { font-size: 0.84rem; color: var(--muted); line-height: 1.55; }
.stat-src { font-size: 0.66rem; color: var(--green-light); margin-top: 0.5rem; }

/* ── SECTION HEADING ── */
.sec-label {
    display: block;
    font-size: 0.66rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--green-light);
    margin-bottom: 0.35rem;
}
.sec-title {
    font-family: 'Playfair Display', serif !important;
    font-size: clamp(1.4rem, 2.4vw, 1.9rem) !important;
    color: var(--black) !important;
    margin-bottom: 1.5rem !important;
    line-height: 1.2 !important;
}
.sec-title em { color: var(--green-mid); font-style: italic; }

/* ── CROP GRID ── */
.crop-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-bottom: 2rem;
}
.crop-card {
    background: var(--white);
    border-radius: 12px;
    padding: 1.4rem;
    border: 1px solid var(--line);
    transition: all 0.2s;
}
.crop-card:hover {
    border-color: var(--yellow);
    box-shadow: 0 6px 24px rgba(245,197,24,0.12);
    transform: translateY(-2px);
}
.crop-emoji { font-size: 1.8rem; margin-bottom: 0.5rem; }
.crop-name { font-family: 'Playfair Display', serif; font-size: 0.95rem; color: var(--black); margin-bottom: 0.15rem; }
.crop-name-hi { font-size: 0.76rem; color: var(--muted); margin-bottom: 0.55rem; }
.dtag {
    display: inline-block;
    background: var(--green-pale);
    color: var(--green);
    font-size: 0.67rem;
    font-weight: 600;
    padding: 0.16rem 0.5rem;
    border-radius: 2rem;
    margin: 0.1rem 0.06rem 0 0;
}
.dtag.warn { background: #FEF3C7; color: #92400E; }
.dtag.danger { background: #FEE2E2; color: #991B1B; }

/* ── HOW IT WORKS ── */
.how-card {
    background: var(--white);
    border-radius: 12px;
    padding: 1.8rem 1.4rem;
    border: 1px solid var(--line);
    text-align: center;
    transition: border-color 0.2s;
}
.how-card:hover { border-color: var(--yellow); }
.how-icon { font-size: 2.2rem; margin-bottom: 0.8rem; }
.how-title { font-family: 'Playfair Display', serif; font-size: 1rem; color: var(--black); margin-bottom: 0.5rem; }
.how-desc { font-size: 0.84rem; color: var(--muted); line-height: 1.65; }

/* ── CTA BANNER ── */
.cta-banner {
    background: var(--yellow-pale);
    border: 1.5px solid #E6D200;
    border-radius: 12px;
    padding: 1.8rem 2rem;
    text-align: center;
    margin: 1.5rem 0 0.5rem;
}
.cta-banner h3 { font-size: 1.2rem; color: var(--black); margin-bottom: 0.5rem; }
.cta-banner p { color: var(--muted); font-size: 0.9rem; line-height: 1.6; }

/* ── STEP CARD ── */
.step-card {
    background: var(--white);
    border-radius: 12px;
    padding: 1.2rem 1.4rem;
    border: 1px solid var(--line);
    margin-bottom: 0.75rem;
    display: flex;
    gap: 1rem;
    align-items: flex-start;
    transition: border-color 0.2s;
}
.step-card:hover { border-color: var(--green-light); }
.step-num {
    background: var(--yellow);
    color: var(--black);
    font-family: 'Playfair Display', serif;
    font-size: 1rem;
    font-weight: 700;
    width: 38px;
    height: 38px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.step-content h4 { color: var(--black); font-size: 0.92rem; font-weight: 600; margin-bottom: 0.2rem; font-family: 'Outfit', sans-serif; }
.step-content p  { color: var(--muted); font-size: 0.83rem; line-height: 1.6; }

/* ── TIP CARD ── */
.tip-card {
    background: var(--white);
    border-radius: 10px;
    padding: 1.1rem 1.3rem;
    border: 1px solid var(--line);
    border-left: 3px solid var(--yellow);
    margin-bottom: 0.7rem;
}
.tip-card h4 { color: var(--black); font-size: 0.9rem; margin-bottom: 0.2rem; font-family: 'Outfit', sans-serif; font-weight: 600; }
.tip-card p  { color: var(--muted); font-size: 0.83rem; line-height: 1.6; }

/* ── FAIL CARD ── */
.fail-card {
    background: #FFF5F5;
    border-radius: 10px;
    padding: 1.1rem;
    border: 1px solid #FECACA;
    border-top: 3px solid #F87171;
    margin-bottom: 0.75rem;
}
.fail-card h4 { color: #7F1D1D; font-size: 0.88rem; margin-bottom: 0.3rem; font-family: 'Outfit', sans-serif; font-weight: 600; }
.fail-card p  { color: var(--muted); font-size: 0.83rem; line-height: 1.6; }

/* ── DISEASE GUIDE ── */
.dg-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-bottom: 2rem;
}
.dg-card {
    background: var(--white);
    border-radius: 12px;
    padding: 1.3rem;
    border: 1px solid var(--line);
    border-top: 3px solid var(--green-light);
}
.dg-card h4 { font-family: 'Playfair Display', serif; font-size: 1rem; color: var(--black); margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem; }
.dg-item { display: flex; gap: 0.5rem; margin-bottom: 0.45rem; }
.dg-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--yellow); margin-top: 0.4rem; flex-shrink: 0; }
.dg-text strong { font-size: 0.82rem; color: var(--black); font-weight: 600; }
.dg-text span { font-size: 0.78rem; color: var(--muted); display: block; line-height: 1.45; margin-top: 0.05rem; }

/* ── UPLOAD ── */
.upload-wrap {
    background: var(--yellow-pale);
    border: 2px dashed var(--yellow-mid);
    border-radius: 14px;
    padding: 2rem 1.6rem 1rem;
    text-align: center;
    margin-bottom: 1rem;
}
.upload-wrap h3 { font-family: 'Playfair Display', serif; color: var(--black); margin-bottom: 0.4rem; font-size: 1.1rem; }
.upload-wrap p { color: var(--muted); font-size: 0.84rem; margin-bottom: 0.25rem; }

/* ── RESULT ── */
.result-banner {
    background: var(--green);
    border-radius: 12px;
    padding: 1.5rem 1.8rem;
    margin-bottom: 0.9rem;
    color: white;
}
.result-banner h2 { color: white !important; font-size: 1.6rem !important; margin-bottom: 0.2rem !important; }
.result-banner p { opacity: 0.7; font-size: 0.87rem; }
.conf-row {
    background: var(--yellow-pale);
    border: 1px solid #E6D200;
    border-radius: 8px;
    padding: 0.8rem 1.1rem;
    margin-bottom: 0.9rem;
    display: flex;
    align-items: center;
    gap: 0.7rem;
    flex-wrap: wrap;
}
.badge {
    display: inline-block;
    padding: 0.2rem 0.7rem;
    border-radius: 2rem;
    font-size: 0.72rem;
    font-weight: 600;
}
.b-healthy { background: var(--green-pale); color: var(--green); }
.b-low     { background: var(--green-pale); color: var(--green); }
.b-medium  { background: #FEF3C7; color: #92400E; }
.b-high    { background: #FEE2E2; color: #991B1B; }
.b-gold    { background: var(--yellow); color: var(--black); }
.top3 {
    background: #F4FAF5;
    border: 1px solid var(--line);
    border-radius: 10px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.9rem;
}
.top3 h5 {
    font-family: 'Outfit', sans-serif;
    font-size: 0.67rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--green-light);
    margin-bottom: 0.7rem;
}
.pred-row { display: flex; align-items: center; gap: 0.7rem; margin-bottom: 0.5rem; }
.pred-lbl { font-size: 0.81rem; color: var(--ink); flex: 1.2; }
.pred-track { flex: 1.5; height: 5px; background: var(--line); border-radius: 3px; overflow: hidden; }
.pred-fill { height: 100%; border-radius: 3px; }
.pred-pct { font-size: 0.79rem; font-weight: 600; color: var(--black); min-width: 38px; text-align: right; }
.unknown-box {
    background: var(--yellow-pale);
    border: 2px solid var(--yellow-mid);
    border-radius: 12px;
    padding: 2rem;
    text-align: center;
    margin-bottom: 1rem;
}
.unknown-box h3 { color: var(--black); font-size: 1.1rem; margin-bottom: 0.5rem; }
.unknown-box p { color: var(--muted); font-size: 0.86rem; line-height: 1.7; }
.tcard {
    background: var(--white);
    border-radius: 10px;
    padding: 1.1rem 1.3rem;
    border: 1px solid var(--line);
    margin-bottom: 0.7rem;
}
.tcard.cause    { border-left: 3px solid var(--green); }
.tcard.organic  { border-left: 3px solid var(--green-light); }
.tcard.chemical { border-left: 3px solid var(--yellow-mid); }
.tcard.prevent  { border-left: 3px solid #60A5FA; }
.tcard h4 {
    font-family: 'Outfit', sans-serif;
    font-size: 0.67rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--green-mid);
    margin-bottom: 0.45rem;
}
.tcard p  { font-size: 0.86rem; color: var(--ink); line-height: 1.7; margin-bottom: 0.25rem; }
.tcard .hi { color: var(--muted); font-size: 0.8rem; }
.helpline {
    background: var(--green);
    color: white;
    padding: 1rem 1.5rem;
    border-radius: 10px;
    text-align: center;
    font-size: 0.88rem;
    margin-top: 1rem;
    border-left: 4px solid var(--yellow);
}

/* ── ABOUT ── */
.about-card {
    background: var(--green);
    border-radius: 16px;
    padding: 2.8rem;
    color: white;
    margin-bottom: 2rem;
    border-left: 5px solid var(--yellow);
}
.about-card h2 { color: var(--yellow) !important; margin-bottom: 1rem !important; font-size: 1.7rem !important; }
.about-card p  { opacity: 0.8; line-height: 1.9; font-size: 0.94rem; margin-bottom: 0.9rem; }
.about-sig { color: var(--yellow) !important; font-weight: 600 !important; font-size: 0.9rem !important; opacity: 1 !important; }

/* ── FOOTER ── */
.footer {
    text-align: center;
    color: var(--muted);
    font-size: 0.78rem;
    padding: 2rem 0 0.5rem;
    border-top: 1px solid var(--line);
    margin-top: 3rem;
}
.footer a { color: var(--green-mid); text-decoration: none; font-weight: 500; }
.footer a:hover { color: var(--green); }

/* ── RESPONSIVE ── */
@media (max-width: 768px) {
    .stat-row, .crop-grid, .dg-grid { grid-template-columns: 1fr 1fr; }
    .hero { padding: 2.2rem 1.6rem; }
}
@media (max-width: 480px) {
    .stat-row, .crop-grid, .dg-grid { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

@st.cache_resource(show_spinner=False)
def load_model():
    import tensorflow as tf
    return tf.keras.models.load_model("cropsense_model.h5")

@st.cache_resource(show_spinner=False)
def load_class_names():
    return sorted(os.listdir("plantvillage dataset/color"))

def preprocess(image):
    img = image.resize((224, 224))
    arr = np.array(img, dtype=np.float32) / 255.0
    return np.expand_dims(arr, axis=0)

def clean_label(raw):
    return raw.replace("___", " — ").replace("_", " ").title()

def severity_badge_class(severity):
    return {
        "None":    "b-healthy",
        "Low":     "b-low",
        "Medium":  "b-medium",
        "High":    "b-high",
        "Unknown": "b-medium",
    }.get(severity, "b-medium")


# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class='sb-brand'>
        <div class='sb-brand-name'>🌿 CropSense</div>
        <div class='sb-brand-sub'>AI Crop Doctor</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<span class='sb-nav-label'>Menu</span>", unsafe_allow_html=True)

    page_choice = st.radio(
        "nav",
        ["🏠  Home", "📖  How to Use", "🔬  Detect Disease", "👤  About"],
        index=["🏠  Home", "📖  How to Use", "🔬  Detect Disease", "👤  About"].index(
            {
                "Home":   "🏠  Home",
                "Guide":  "📖  How to Use",
                "Detect": "🔬  Detect Disease",
                "About":  "👤  About",
            }.get(st.session_state.page, "🏠  Home")
        ),
        label_visibility="collapsed"
    )

    st.session_state.page = {
        "🏠  Home":           "Home",
        "📖  How to Use":     "Guide",
        "🔬  Detect Disease": "Detect",
        "👤  About":          "About",
    }[page_choice]

    st.markdown("---")

    st.markdown("<span class='sb-nav-label'>📞 Helpline</span>", unsafe_allow_html=True)
    st.markdown("""
    <div class='sb-helpline'>
        <div class='sb-helpline-label'>Kisan Call Centre</div>
        <div class='sb-helpline-num'>1800-180-1551</div>
        <div class='sb-helpline-sub'>Free · 24/7 · Hindi available</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div class='sb-footer'>
        <div class='sb-footer-text'>
            Built by <strong style='color:rgba(255,255,255,0.6)'>Mokshi Jain</strong><br>
            <a href='https://mokshi-repository.vercel.app' target='_blank'>Portfolio</a> ·
            <a href='https://github.com/jainmokshii' target='_blank'>GitHub</a> ·
            <a href='https://www.linkedin.com/in/mokshijain/' target='_blank'>LinkedIn</a>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 1 — HOME
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.page == "Home":

    st.markdown("""
    <div class='hero'>
        <span class='hero-chip'>AI-Powered · Bilingual · Free · For Every Indian Farmer</span>
        <h1>Meet <em>CropSense</em> —<br>Your AI Crop Doctor</h1>
        <p class='hero-desc'>
            Upload a photo of any crop leaf and get an instant disease diagnosis
            with treatment advice in Hindi & English. Built for real-world conditions —
            basic phones, imperfect lighting, no expertise needed.
        </p>
        <p class='hero-hi'>किसी भी फसल की पत्ती की फोटो अपलोड करें — तुरंत निदान पाएं।</p>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown("""
    <div class='stat-row'>
        <div class='stat-card'>
            <div class='stat-num'>35%</div>
            <div class='stat-label'>of India's annual crop production lost to pests and disease</div>
            <div class='stat-src'>ICAR · PlantDoc, IIT Gandhinagar (2019)</div>
        </div>
        <div class='stat-card'>
            <div class='stat-num'>54,000+</div>
            <div class='stat-label'>leaf images across 14 plant species used to train the AI model</div>
            <div class='stat-src'>PlantVillage Dataset · Hughes & Salathé, Penn State (2015)</div>
        </div>
        <div class='stat-card'>
            <div class='stat-num'>38</div>
            <div class='stat-label'>disease classes detected — both healthy and diseased conditions</div>
            <div class='stat-src'>PlantVillage Dataset · Kaggle (CC BY-NC-SA 4.0)</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # How it works
    st.markdown("<span class='sec-label'>The process</span>", unsafe_allow_html=True)
    st.markdown("<h2 class='sec-title'>How it <em>Works</em></h2>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="medium")
    for col, icon, title, desc in [
        (c1, "📸", "Upload a Leaf Photo", "Take a close-up of the affected leaf in natural daylight. Any smartphone camera works."),
        (c2, "🧠", "AI Analyses It", "ResNet50 scans the leaf against 38 disease patterns in seconds and returns a confidence-scored result."),
        (c3, "💊", "Get Actionable Advice", "Diagnosis, cause, organic & chemical treatments, and prevention — in Hindi and English."),
    ]:
        with col:
            st.markdown(f"""
            <div class='how-card'>
                <div class='how-icon'>{icon}</div>
                <div class='how-title'>{title}</div>
                <div class='how-desc'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Crops we detect
    st.markdown("<span class='sec-label'>Supported crops</span>", unsafe_allow_html=True)
    st.markdown("<h2 class='sec-title'>What CropSense <em>Knows</em></h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class='crop-grid'>
        <div class='crop-card'>
            <div class='crop-emoji'>🍅</div>
            <div class='crop-name'>Tomato — टमाटर</div>
            <div class='crop-name-hi'>8 conditions detected</div>
            <span class='dtag danger'>Early Blight</span>
            <span class='dtag danger'>Late Blight</span>
            <span class='dtag warn'>Leaf Mold</span>
            <span class='dtag warn'>Mosaic Virus</span>
            <span class='dtag'>Septoria Spot</span>
            <span class='dtag'>Spider Mites</span>
            <span class='dtag danger'>Yellow Leaf Curl</span>
        </div>
        <div class='crop-card'>
            <div class='crop-emoji'>🥔</div>
            <div class='crop-name'>Potato — आलू</div>
            <div class='crop-name-hi'>3 conditions detected</div>
            <span class='dtag danger'>Early Blight</span>
            <span class='dtag danger'>Late Blight</span>
            <span class='dtag'>Healthy</span>
        </div>
        <div class='crop-card'>
            <div class='crop-emoji'>🌽</div>
            <div class='crop-name'>Corn — मक्का</div>
            <div class='crop-name-hi'>4 conditions detected</div>
            <span class='dtag warn'>Common Rust</span>
            <span class='dtag'>Gray Leaf Spot</span>
            <span class='dtag danger'>N. Leaf Blight</span>
        </div>
        <div class='crop-card'>
            <div class='crop-emoji'>🍎</div>
            <div class='crop-name'>Apple — सेब</div>
            <div class='crop-name-hi'>4 conditions detected</div>
            <span class='dtag danger'>Apple Scab</span>
            <span class='dtag danger'>Black Rot</span>
            <span class='dtag warn'>Cedar Rust</span>
        </div>
        <div class='crop-card'>
            <div class='crop-emoji'>🍇</div>
            <div class='crop-name'>Grape — अंगूर</div>
            <div class='crop-name-hi'>4 conditions detected</div>
            <span class='dtag danger'>Black Rot</span>
            <span class='dtag warn'>Esca</span>
            <span class='dtag'>Leaf Blight</span>
        </div>
        <div class='crop-card'>
            <div class='crop-emoji'>🫑</div>
            <div class='crop-name'>Bell Pepper — शिमला मिर्च</div>
            <div class='crop-name-hi'>2 conditions detected</div>
            <span class='dtag warn'>Bacterial Spot</span>
            <span class='dtag'>Healthy</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # CTA
    st.markdown("""
    <div class='cta-banner'>
        <h3>Ready to diagnose your crop?</h3>
        <p>Navigate to <strong>🔬 Detect Disease</strong> in the sidebar and upload your first leaf photo.</p>
        <p style='color: var(--green-mid); margin-top: 0.4rem; font-size: 0.84rem'>
            पत्ती की फोटो अपलोड करें → तुरंत निदान पाएं
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='footer'>
        Built by <strong>Mokshi Jain</strong> &nbsp;·&nbsp;
        <a href='https://mokshi-repository.vercel.app' target='_blank'>Portfolio</a> &nbsp;·&nbsp;
        <a href='https://github.com/jainmokshii' target='_blank'>GitHub</a>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 2 — HOW TO USE
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.page == "Guide":

    st.markdown("""
    <div class='page-header'>
        <span class='page-header-chip'>User Guide</span>
        <h1>How to Use <em>CropSense</em></h1>
        <p>Step-by-step instructions and best practices for accurate results.</p>
    </div>
    """, unsafe_allow_html=True)

    col_steps, col_tips = st.columns([1.15, 1], gap="large")

    with col_steps:
        st.markdown("<span class='sec-label'>Step by step</span>", unsafe_allow_html=True)
        st.markdown("<h2 class='sec-title'>Getting <em>Started</em></h2>", unsafe_allow_html=True)

        for num, title, desc in [
            ("1", "Open the Detect page", "Click '🔬 Detect Disease' in the left sidebar to go to the upload page."),
            ("2", "Take a clear leaf photo", "Use your phone in natural daylight. Let the diseased leaf fill most of the frame. Avoid flash."),
            ("3", "Upload the image", "Click 'Browse files' or drag and drop your photo. JPG, JPEG, and PNG all work."),
            ("4", "Wait a few seconds", "The AI analyses your leaf and returns its top prediction with a confidence score."),
            ("5", "Read the diagnosis", "You get the disease name, cause, organic and chemical treatments, and prevention tips — in Hindi & English."),
            ("6", "Low confidence shown?", "If confidence is below 45%, the photo isn't clear enough. Retake in better lighting, closer to the leaf."),
            ("7", "Still unsure? Call the helpline", "Dial 1800-180-1551 (free, 24/7) and speak with a Kisan expert in Hindi."),
        ]:
            st.markdown(f"""
            <div class='step-card'>
                <div class='step-num'>{num}</div>
                <div class='step-content'>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

        if st.button("🔬 Go to Detect Disease →", type="primary"):
            st.session_state.page = "Detect"
            st.rerun()

    with col_tips:
        st.markdown("<span class='sec-label'>Best practices</span>", unsafe_allow_html=True)
        st.markdown("<h2 class='sec-title'>Photo <em>Tips</em></h2>", unsafe_allow_html=True)

        for icon, title, desc in [
            ("☀️", "Natural daylight only", "Sunlight gives the most accurate colours. Indoor lighting distorts the green tones the model relies on."),
            ("📏", "15–20 cm distance", "Hold your phone about 15–20 cm from the leaf so it fills most of the frame."),
            ("🍃", "One leaf per photo", "Multiple leaves in one shot significantly reduce accuracy. Focus on one clearly affected leaf."),
            ("🔄", "Check both sides", "Many diseases appear differently on the top and bottom. Photograph both if symptoms differ."),
            ("🎯", "Tap to focus first", "Wait for your camera to lock focus before shooting. Blur is the top cause of wrong predictions."),
            ("⏱️", "Detect early", "Upload photos as soon as you notice unusual colour, spots, or texture — early detection saves crops."),
        ]:
            st.markdown(f"""
            <div class='tip-card'>
                <h4>{icon} {title}</h4>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    # Limitations
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<span class='sec-label'>Honest limitations</span>", unsafe_allow_html=True)
    st.markdown("<h2 class='sec-title'>Known <em>Failure Cases</em></h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: var(--muted); font-size: 0.9rem; margin-bottom: 1.3rem; max-width: 660px'>CropSense is built for real-world use. Here are the cases where accuracy drops — and why.</p>", unsafe_allow_html=True)

    fc1, fc2, fc3 = st.columns(3)
    for col, title, desc in [
        (fc1, "🌑 Poor lighting", "Images taken indoors or at night lack the colour and texture signals the model trained on. Always photograph in daylight."),
        (fc2, "📷 Blurry or overexposed", "Blur destroys edge features; overexposure washes out colour. Both cause low confidence or wrong predictions."),
        (fc3, "🌾 Unsupported crops", "CropSense knows 14 crops. Uploading wheat, rice, or sugarcane will return a misleading result."),
        (fc1, "🖼️ Non-leaf images", "Uploading soil, fruit, or a whole plant bypasses leaf detection and returns a meaningless result."),
        (fc2, "🦠 Very early symptoms", "Diseases with extremely mild symptoms may be classified as 'Healthy'. Visible symptoms are needed."),
        (fc3, "🔬 Lab vs. field gap", "PlantVillage images were taken in controlled conditions. Real farm photos with dirt or water drops score lower confidence."),
    ]:
        with col:
            st.markdown(f"""
            <div class='fail-card'>
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div style='background: var(--green-pale); border: 1px solid #95D5B2; border-radius: 10px;
                padding: 1.1rem 1.5rem; margin-top: 0.5rem'>
        <p style='color: var(--green); font-size: 0.88rem; line-height: 1.75; margin: 0'>
        <strong>📌 Important:</strong> CropSense is a decision-support tool, not a replacement for an agricultural expert.
        If the result doesn't match what you see in the field, contact your local
        <strong>Krishi Vigyan Kendra (KVK)</strong> or call <strong>1800-180-1551</strong> (free, 24/7).
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Quick disease guide — embedded here on the guide page
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<span class='sec-label'>Reference</span>", unsafe_allow_html=True)
    st.markdown("<h2 class='sec-title'>Quick Disease <em>Guide</em></h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: var(--muted); font-size: 0.9rem; margin-bottom: 1.3rem'>Common symptoms for key crops — useful when identifying issues in the field before uploading.</p>", unsafe_allow_html=True)

    st.markdown("""
    <div class='dg-grid'>
        <div class='dg-card'>
            <h4>🍅 Tomato</h4>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Early Blight</strong><span>Concentric brown rings on lower leaves first</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Late Blight</strong><span>Dark water-soaked lesions, spreads rapidly</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Leaf Mold</strong><span>Yellow patches above, mold growth on underside</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Mosaic Virus</strong><span>Mottled yellow-green patterns, stunted growth</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Spider Mites</strong><span>Fine webbing on leaf, bronze discolouration</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Septoria Spot</strong><span>Small circular spots with dark border</span></div></div>
        </div>
        <div class='dg-card'>
            <h4>🥔 Potato &amp; 🌽 Corn</h4>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Potato Early Blight</strong><span>Circular brown spots on older leaves</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Potato Late Blight</strong><span>Most destructive — dark lesions + tuber rot</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Corn Common Rust</strong><span>Oval rust-coloured pustules on both leaf surfaces</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Gray Leaf Spot</strong><span>Long rectangular grey-brown lesions</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Northern Leaf Blight</strong><span>Long cigar-shaped grey-green lesions</span></div></div>
        </div>
        <div class='dg-card'>
            <h4>🍎 Apple</h4>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Apple Scab</strong><span>Olive-green to black spots on leaves and fruit</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Black Rot</strong><span>Brown concentric rings on fruit; frog-eye spots on leaves</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Cedar Apple Rust</strong><span>Bright orange spots on upper leaf surface</span></div></div>
        </div>
        <div class='dg-card'>
            <h4>🍇 Grape &amp; 🫑 Pepper</h4>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Grape Black Rot</strong><span>Reddish-brown spots, shrivelled black berries</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Esca (Black Measles)</strong><span>Tiger-stripe leaf pattern, wood decay</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Grape Leaf Blight</strong><span>Irregular brown spots with yellow halos</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Pepper Bacterial Spot</strong><span>Water-soaked spots turning yellow-brown</span></div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='footer'>
        Built by <strong>Mokshi Jain</strong> &nbsp;·&nbsp;
        <a href='https://mokshi-repository.vercel.app' target='_blank'>Portfolio</a> &nbsp;·&nbsp;
        <a href='https://github.com/jainmokshii' target='_blank'>GitHub</a>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 3 — DETECT DISEASE
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.page == "Detect":

    st.markdown("""
    <div class='page-header'>
        <span class='page-header-chip'>AI Diagnosis</span>
        <h1>Detect <em>Disease</em></h1>
        <p>Upload a clear leaf photo for an instant AI-powered diagnosis. · पत्ती की फोटो अपलोड करें।</p>
    </div>
    """, unsafe_allow_html=True)

    col_up, col_res = st.columns([1, 1.6], gap="large")

    with col_up:
        st.markdown("""
        <div class='upload-wrap'>
            <div style='font-size: 2.4rem; margin-bottom: 0.6rem'>🌿</div>
            <h3>Upload Leaf Photo</h3>
            <p>Drag & drop or browse</p>
            <p style='color: var(--green-light); font-size: 0.78rem'>JPG · JPEG · PNG supported</p>
        </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "Choose leaf image",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed"
        )

        if uploaded_file:
            image = Image.open(uploaded_file).convert("RGB")
            st.image(image, use_container_width=True, caption="Uploaded leaf")
            w, h = image.size
            st.markdown(f"<div style='font-size:0.73rem;color:var(--muted);margin-top:0.25rem'>📐 {w}×{h}px · {uploaded_file.size//1024} KB</div>", unsafe_allow_html=True)

    with col_res:
        if not uploaded_file:
            st.markdown("""
            <div style='padding: 5rem 2rem; text-align: center; background: var(--white);
                        border-radius: 14px; border: 1px solid var(--line); margin-top: 0.5rem'>
                <div style='font-size: 3rem; margin-bottom: 1rem'>🔬</div>
                <h3 style='font-family: Playfair Display, serif; color: var(--black); margin-bottom: 0.4rem'>Results appear here</h3>
                <p style='color: var(--muted); font-size: 0.86rem'>Upload a leaf photo on the left to get started</p>
                <p style='color: var(--green-light); font-size: 0.82rem; margin-top: 0.3rem'>पत्ती की फोटो अपलोड करें → यहाँ परिणाम देखें</p>
                <div style='margin-top: 1.5rem; display: flex; justify-content: center; gap: 1.2rem; flex-wrap: wrap'>
                    <span style='font-size:0.8rem;color:var(--muted)'>🍅 Tomato</span>
                    <span style='font-size:0.8rem;color:var(--muted)'>🥔 Potato</span>
                    <span style='font-size:0.8rem;color:var(--muted)'>🌽 Corn</span>
                    <span style='font-size:0.8rem;color:var(--muted)'>🍎 Apple</span>
                    <span style='font-size:0.8rem;color:var(--muted)'>🍇 Grape</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            with st.spinner("🔍 Analysing your crop... / विश्लेषण हो रहा है..."):
                try:
                    model   = load_model()
                    classes = load_class_names()
                    arr     = preprocess(image)
                    preds   = model.predict(arr, verbose=0)[0]
                    top_idx = int(np.argmax(preds))
                    conf    = float(preds[top_idx])
                    pred_cls = classes[top_idx]
                    top3    = [(classes[i], float(preds[i])) for i in np.argsort(preds)[::-1][:3]]

                    THRESHOLD = 0.45

                    if conf < THRESHOLD:
                        st.markdown(f"""
                        <div class='unknown-box'>
                            <div style='font-size: 2rem; margin-bottom: 0.6rem'>⚠️</div>
                            <h3>Unable to identify disease confidently</h3>
                            <p>
                                Confidence: <strong>{conf*100:.1f}%</strong> — below the {int(THRESHOLD*100)}% threshold.<br><br>
                                This usually means the image is blurry, too dark, shows multiple leaves, or the crop
                                is not in the current dataset.<br><br>
                                <strong>बेहतर रोशनी में एक पत्ती की साफ फोटो लें और दोबारा अपलोड करें।</strong>
                            </p>
                        </div>
                        """, unsafe_allow_html=True)

                        st.markdown("<div class='top3'><h5>Top guesses (low confidence)</h5>", unsafe_allow_html=True)
                        for i, (cn, prob) in enumerate(top3):
                            w = max(int(prob * 100), 1)
                            st.markdown(f"""
                            <div class='pred-row'>
                                <div class='pred-lbl'>{clean_label(cn)}</div>
                                <div class='pred-track'><div class='pred-fill' style='width:{w}%;background:#D1D5DB'></div></div>
                                <div class='pred-pct' style='color:var(--muted)'>{prob*100:.1f}%</div>
                            </div>
                            """, unsafe_allow_html=True)
                        st.markdown("</div>", unsafe_allow_html=True)

                    else:
                        from treatment_data import get_treatment
                        t = get_treatment(pred_cls)
                        b_cls = severity_badge_class(t["severity"])

                        st.markdown(f"""
                        <div class='result-banner'>
                            <h2>{t['name_en']}</h2>
                            <p>{t['name_hi']} &nbsp;·&nbsp; {t['crop_en']} ({t['crop_hi']})</p>
                        </div>
                        <div class='conf-row'>
                            <span class='badge {b_cls}'>{t['severity']} Risk</span>
                            <span class='badge b-gold'>Confidence: {conf*100:.1f}%</span>
                            <span style='font-size:0.77rem;color:var(--muted)'>Yield loss risk: {t['yield_loss']}</span>
                        </div>
                        """, unsafe_allow_html=True)

                        bar_colors = [var for var in ["#2D6A4F", "#52B788", "#95D5B2"]]
                        st.markdown("<div class='top3'><h5>📊 Top 3 predictions</h5>", unsafe_allow_html=True)
                        for i, (cn, prob) in enumerate(top3):
                            w = max(int(prob * 100), 1)
                            lbl_style = "font-weight:600;color:var(--black)" if i == 0 else ""
                            pct_style = "color:var(--black);font-weight:600" if i == 0 else ""
                            st.markdown(f"""
                            <div class='pred-row'>
                                <div class='pred-lbl' style='{lbl_style}'>{"✅ " if i==0 else ""}{clean_label(cn)}</div>
                                <div class='pred-track'><div class='pred-fill' style='width:{w}%;background:{bar_colors[i]}'></div></div>
                                <div class='pred-pct' style='{pct_style}'>{prob*100:.1f}%</div>
                            </div>
                            """, unsafe_allow_html=True)
                        st.markdown("</div>", unsafe_allow_html=True)

                        st.markdown(f"""
                        <div class='tcard cause'>
                            <h4>🔬 Cause / कारण</h4>
                            <p>{t['cause_en']}</p>
                            <p class='hi'>{t['cause_hi']}</p>
                        </div>
                        """, unsafe_allow_html=True)

                        tc1, tc2 = st.columns(2)
                        with tc1:
                            st.markdown(f"""
                            <div class='tcard organic'>
                                <h4>🌱 Organic / जैविक</h4>
                                <p>{t['organic_en']}</p>
                                <p class='hi'>{t['organic_hi']}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        with tc2:
                            st.markdown(f"""
                            <div class='tcard chemical'>
                                <h4>⚗️ Chemical / रासायनिक</h4>
                                <p>{t['chemical_en']}</p>
                                <p class='hi'>{t['chemical_hi']}</p>
                            </div>
                            """, unsafe_allow_html=True)

                        st.markdown(f"""
                        <div class='tcard prevent'>
                            <h4>🛡️ Prevention / रोकथाम</h4>
                            <p>{t['prevention_en']}</p>
                            <p class='hi'>{t['prevention_hi']}</p>
                        </div>
                        <div class='helpline'>
                            📞 <strong>Kisan Call Centre: 1800-180-1551</strong>
                            &nbsp;·&nbsp; Free / निशुल्क &nbsp;·&nbsp; 24/7 &nbsp;·&nbsp; Hindi & Regional Languages
                        </div>
                        """, unsafe_allow_html=True)

                except FileNotFoundError:
                    st.info("""
                    🔄 **Model not found yet.**

                    Run `train.py` (and optionally `finetune.py`) to generate `cropsense_model.h5`, then deploy.
                    The full UI and detection logic are ready and waiting.

                    *मॉडल अभी ट्रेनिंग में है। ट्रेनिंग पूरी होने पर यहाँ परिणाम आएगा।*
                    """)
                except Exception as e:
                    st.error(f"Unexpected error: {e}")
                    st.info("Check that `cropsense_model.h5` and `treatment_data.py` are in the same directory.")

    st.markdown("""
    <div class='footer'>
        Built by <strong>Mokshi Jain</strong> &nbsp;·&nbsp;
        <a href='https://mokshi-repository.vercel.app' target='_blank'>Portfolio</a> &nbsp;·&nbsp;
        <a href='https://github.com/jainmokshii' target='_blank'>GitHub</a>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 4 — ABOUT
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.page == "About":

    st.markdown("""
    <div class='page-header'>
        <span class='page-header-chip'>Builder's Note</span>
        <h1>The <em>Why</em> Behind CropSense</h1>
        <p>A personal note from the person who built this.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='about-card'>
        <h2>A Note from the Builder</h2>
        <p>
        India is an agricultural nation. Over 60% of our population depends on farming for their livelihood.
        Yet every year, farmers across India lose entire harvests to crop diseases they cannot identify
        early enough — not because the knowledge doesn't exist, but because it isn't accessible to them.
        </p>
        <p>
        I built CropSense because most existing agricultural AI tools are English-only, require expensive
        equipment, and are built for perfect studio-quality images. A farmer with a basic Android phone
        and an imperfect photo shouldn't be left without help.
        </p>
        <p>
        CropSense gives that farmer an instant diagnosis in Hindi, with practical treatment advice they
        can actually act on — no cost, no English required, no technical knowledge needed.
        </p>
        <p>
        This is not just an AI model project. It is an AI product system designed under real-world
        constraints: low-quality images, regional language needs, and users with zero technical background.
        The gap between "lab accuracy" and "field reality" is the problem I spent the most time thinking about.
        </p>
        <p class='about-sig'>— Mokshi Jain</p>
    </div>
    """, unsafe_allow_html=True)

    col_prob, col_sol = st.columns(2, gap="large")

    with col_prob:
        st.markdown("<span class='sec-label'>The challenge</span>", unsafe_allow_html=True)
        st.markdown("<h2 class='sec-title'>Real <em>Problems</em></h2>", unsafe_allow_html=True)

        for icon, title, desc in [
            ("📉", "Massive crop losses", "Over 35% of India's annual crop production is lost to pests and disease — most of it preventable with early detection."),
            ("🌐", "Language barrier", "Most agricultural AI tools are English-only. The majority of Indian farmers are far more comfortable in Hindi or regional languages."),
            ("📱", "Technology gap", "Existing tools assume high-quality cameras and stable internet. Most smallholder farmers use basic Android phones with 2G/3G data."),
            ("⏱️", "Delayed action", "By the time a farmer reaches an agricultural expert, the disease has already spread — and the window for effective action has closed."),
        ]:
            st.markdown(f"""
            <div class='step-card'>
                <div class='step-num' style='background:var(--green-pale);color:var(--green);font-size:1.2rem'>{icon}</div>
                <div class='step-content'>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_sol:
        st.markdown("<span class='sec-label'>Our approach</span>", unsafe_allow_html=True)
        st.markdown("<h2 class='sec-title'>The <em>Solutions</em></h2>", unsafe_allow_html=True)

        for icon, title, desc in [
            ("🗣️", "Bilingual by design", "Every diagnosis, treatment, and tip is available in Hindi and English — no translation step needed."),
            ("📷", "Real-world images", "Trained with heavy augmentation (rotation, blur, brightness variation) to handle real phone camera photos."),
            ("💊", "Actionable advice", "We don't just name the disease — we give organic remedies, chemical options, yield loss estimates, and prevention tips."),
            ("🧠", "Transparent uncertainty", "When the model isn't confident, it says so clearly. No false positives that could mislead a farmer into wrong treatment."),
            ("⚡", "Instant and free", "No sign-up, no cost, no app download. Upload from any browser and get a structured diagnosis in seconds."),
        ]:
            st.markdown(f"""
            <div class='step-card'>
                <div class='step-num' style='background:var(--yellow);color:var(--black);font-size:1.1rem'>{icon}</div>
                <div class='step-content'>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<span class='sec-label'>Under the hood</span>", unsafe_allow_html=True)
    st.markdown("<h2 class='sec-title'>Tech <em>Stack</em></h2>", unsafe_allow_html=True)

    ts1, ts2, ts3, ts4 = st.columns(4)
    for col, icon, label, detail in [
        (ts1, "🧠", "Model", "ResNet50 · Transfer Learning · TensorFlow 2.13 · Keras"),
        (ts2, "🖼️", "Data", "PlantVillage Dataset · 54,000+ images · 38 classes"),
        (ts3, "🌐", "App", "Streamlit · PIL · NumPy · OpenCV"),
        (ts4, "🚀", "Deploy", "Hugging Face Spaces / Streamlit Cloud"),
    ]:
        with col:
            st.markdown(f"""
            <div class='stat-card' style='border-top-color: var(--green-light)'>
                <div style='font-size: 1.6rem; margin-bottom: 0.5rem'>{icon}</div>
                <div class='stat-num' style='font-size: 1rem; margin-bottom: 0.25rem'>{label}</div>
                <div class='stat-label'>{detail}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class='footer'>
        Built by <strong>Mokshi Jain</strong> &nbsp;·&nbsp;
        <a href='https://mokshi-repository.vercel.app' target='_blank'>Portfolio</a> &nbsp;·&nbsp;
        <a href='https://github.com/jainmokshii' target='_blank'>GitHub</a> &nbsp;·&nbsp;
        <a href='https://www.linkedin.com/in/mokshijain/' target='_blank'>LinkedIn</a>
    </div>
    """, unsafe_allow_html=True)