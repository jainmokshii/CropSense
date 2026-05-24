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
.stApp { background: var(--off-white); }
.block-container {
    padding: 0 2.5rem 4rem !important;
    max-width: 1240px !important;
    margin: 0 auto !important;
}
#MainMenu, footer, header { visibility: hidden; }

/* ── HIDE STREAMLIT SIDEBAR ARROW/TOGGLE (all known selectors) ── */
button[data-testid="collapsedControl"],
button[kind="header"],
[data-testid="collapsedControl"],
.css-1rs6os,
.css-17ziqus,
[aria-label="Close sidebar"],
[aria-label="Open sidebar"],
section[data-testid="stSidebar"] > div > div:first-child > div > button,
section[data-testid="stSidebar"] button[title="Close sidebar"],
.st-emotion-cache-1rs6os,
.st-emotion-cache-17ziqus {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
}

/* ── SIDEBAR ── */
section[data-testid="stSidebar"] {
    background: var(--green) !important;
    border-right: none !important;
    min-width: 240px !important;
    max-width: 240px !important;
}
section[data-testid="stSidebar"] > div:first-child { padding-top: 0 !important; }
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
.sb-footer-text a { color: var(--yellow) !important; text-decoration: none !important; }

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
.page-header p { color: var(--muted); font-size: 1rem; max-width: 560px; line-height: 1.7; }
.page-header .hi { color: rgba(0,0,0,0.38); font-size: 0.87rem; margin-top: 0.3rem; }

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
.hero-desc { color: rgba(255,255,255,0.75); font-size: 0.97rem; line-height: 1.8; max-width: 500px; margin-bottom: 0.5rem; }
.hero-hi { color: rgba(255,255,255,0.4); font-size: 0.85rem; margin-top: 0.4rem; }

/* ── STAT CARDS ── */
.stat-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.2rem; margin-bottom: 2.5rem; }
.stat-card { background: var(--white); border-radius: 12px; padding: 1.6rem; border: 1px solid var(--line); border-top: 3px solid var(--yellow); }
.stat-num { font-family: 'Playfair Display', serif; font-size: 2.2rem; font-weight: 700; color: var(--black); line-height: 1; margin-bottom: 0.4rem; }
.stat-label { font-size: 0.84rem; color: var(--muted); line-height: 1.55; }
.stat-src { font-size: 0.66rem; color: var(--green-light); margin-top: 0.5rem; }

/* ── SECTION HEADING ── */
.sec-label { display: block; font-size: 0.66rem; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: var(--green-light); margin-bottom: 0.35rem; }
.sec-title { font-family: 'Playfair Display', serif !important; font-size: clamp(1.4rem, 2.4vw, 1.9rem) !important; color: var(--black) !important; margin-bottom: 1.5rem !important; line-height: 1.2 !important; }
.sec-title em { color: var(--green-mid); font-style: italic; }

/* ── CROP GRID ── */
.crop-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-bottom: 2rem; }
.crop-card { background: var(--white); border-radius: 12px; padding: 1.4rem; border: 1px solid var(--line); transition: all 0.2s; }
.crop-card:hover { border-color: var(--yellow); box-shadow: 0 6px 24px rgba(245,197,24,0.12); transform: translateY(-2px); }
.crop-emoji { font-size: 1.8rem; margin-bottom: 0.5rem; }
.crop-name { font-family: 'Playfair Display', serif; font-size: 0.95rem; color: var(--black); margin-bottom: 0.15rem; }
.crop-name-hi { font-size: 0.76rem; color: var(--muted); margin-bottom: 0.55rem; }
.dtag { display: inline-block; background: var(--green-pale); color: var(--green); font-size: 0.67rem; font-weight: 600; padding: 0.16rem 0.5rem; border-radius: 2rem; margin: 0.1rem 0.06rem 0 0; }
.dtag.warn { background: #FEF3C7; color: #92400E; }
.dtag.danger { background: #FEE2E2; color: #991B1B; }

/* ── HOW IT WORKS ── */
.how-card { background: var(--white); border-radius: 12px; padding: 1.8rem 1.4rem; border: 1px solid var(--line); text-align: center; transition: border-color 0.2s; }
.how-card:hover { border-color: var(--yellow); }
.how-icon { font-size: 2.2rem; margin-bottom: 0.8rem; }
.how-title { font-family: 'Playfair Display', serif; font-size: 1rem; color: var(--black); margin-bottom: 0.5rem; }
.how-desc { font-size: 0.84rem; color: var(--muted); line-height: 1.65; }
.how-hi { font-size: 0.76rem; color: rgba(0,0,0,0.3); margin-top: 0.4rem; line-height: 1.5; }

/* ── CTA BANNER ── */
.cta-banner { background: var(--yellow-pale); border: 1.5px solid #E6D200; border-radius: 12px; padding: 1.8rem 2rem; text-align: center; margin: 1.5rem 0 0.5rem; }
.cta-banner h3 { font-size: 1.2rem; color: var(--black); margin-bottom: 0.5rem; }
.cta-banner p { color: var(--muted); font-size: 0.9rem; line-height: 1.6; }

/* ── STEP CARD ── */
.step-card { background: var(--white); border-radius: 12px; padding: 1.2rem 1.4rem; border: 1px solid var(--line); margin-bottom: 0.75rem; display: flex; gap: 1rem; align-items: flex-start; transition: border-color 0.2s; }
.step-card:hover { border-color: var(--green-light); }
.step-num { background: var(--yellow); color: var(--black); font-family: 'Playfair Display', serif; font-size: 1rem; font-weight: 700; width: 38px; height: 38px; border-radius: 50%; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
.step-content h4 { color: var(--black); font-size: 0.92rem; font-weight: 600; margin-bottom: 0.2rem; font-family: 'Outfit', sans-serif; }
.step-content p { color: var(--muted); font-size: 0.83rem; line-height: 1.6; }
.step-content .hi { color: rgba(0,0,0,0.32); font-size: 0.76rem; margin-top: 0.15rem; }

/* ── TIP CARD ── */
.tip-card { background: var(--white); border-radius: 10px; padding: 1.1rem 1.3rem; border: 1px solid var(--line); border-left: 3px solid var(--yellow); margin-bottom: 0.7rem; }
.tip-card h4 { color: var(--black); font-size: 0.9rem; margin-bottom: 0.2rem; font-family: 'Outfit', sans-serif; font-weight: 600; }
.tip-card p { color: var(--muted); font-size: 0.83rem; line-height: 1.6; }
.tip-card .hi { color: rgba(0,0,0,0.32); font-size: 0.76rem; margin-top: 0.15rem; }

/* ── FAIL CARD ── */
.fail-card { background: #FFF5F5; border-radius: 10px; padding: 1.1rem; border: 1px solid #FECACA; border-top: 3px solid #F87171; margin-bottom: 0.75rem; }
.fail-card h4 { color: #7F1D1D; font-size: 0.88rem; margin-bottom: 0.3rem; font-family: 'Outfit', sans-serif; font-weight: 600; }
.fail-card p { color: var(--muted); font-size: 0.83rem; line-height: 1.6; }

/* ── DISEASE GUIDE ── */
.dg-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-bottom: 2rem; }
.dg-card { background: var(--white); border-radius: 12px; padding: 1.3rem; border: 1px solid var(--line); border-top: 3px solid var(--green-light); }
.dg-card h4 { font-family: 'Playfair Display', serif; font-size: 1rem; color: var(--black); margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem; }
.dg-item { display: flex; gap: 0.5rem; margin-bottom: 0.45rem; }
.dg-dot { width: 6px; height: 6px; border-radius: 50%; background: var(--yellow); margin-top: 0.4rem; flex-shrink: 0; }
.dg-text strong { font-size: 0.82rem; color: var(--black); font-weight: 600; }
.dg-text span { font-size: 0.78rem; color: var(--muted); display: block; line-height: 1.45; margin-top: 0.05rem; }

/* ── UPLOAD ── */
.upload-wrap { background: var(--yellow-pale); border: 2px dashed var(--yellow-mid); border-radius: 14px; padding: 2rem 1.6rem 1rem; text-align: center; margin-bottom: 1rem; }
.upload-wrap h3 { font-family: 'Playfair Display', serif; color: var(--black); margin-bottom: 0.4rem; font-size: 1.1rem; }
.upload-wrap p { color: var(--muted); font-size: 0.84rem; margin-bottom: 0.25rem; }

/* ── RESULT ── */
.result-banner { background: var(--green); border-radius: 12px; padding: 1.5rem 1.8rem; margin-bottom: 0.9rem; color: white; }
.result-banner h2 { color: white !important; font-size: 1.6rem !important; margin-bottom: 0.2rem !important; }
.result-banner p { opacity: 0.7; font-size: 0.87rem; }
.conf-row { background: var(--yellow-pale); border: 1px solid #E6D200; border-radius: 8px; padding: 0.8rem 1.1rem; margin-bottom: 0.9rem; display: flex; align-items: center; gap: 0.7rem; flex-wrap: wrap; }
.badge { display: inline-block; padding: 0.2rem 0.7rem; border-radius: 2rem; font-size: 0.72rem; font-weight: 600; }
.b-healthy { background: var(--green-pale); color: var(--green); }
.b-low     { background: var(--green-pale); color: var(--green); }
.b-medium  { background: #FEF3C7; color: #92400E; }
.b-high    { background: #FEE2E2; color: #991B1B; }
.b-gold    { background: var(--yellow); color: var(--black); }
.top3 { background: #F4FAF5; border: 1px solid var(--line); border-radius: 10px; padding: 1rem 1.2rem; margin-bottom: 0.9rem; }
.top3 h5 { font-family: 'Outfit', sans-serif; font-size: 0.67rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; color: var(--green-light); margin-bottom: 0.7rem; }
.pred-row { display: flex; align-items: center; gap: 0.7rem; margin-bottom: 0.5rem; }
.pred-lbl { font-size: 0.81rem; color: var(--ink); flex: 1.2; }
.pred-track { flex: 1.5; height: 5px; background: var(--line); border-radius: 3px; overflow: hidden; }
.pred-fill { height: 100%; border-radius: 3px; }
.pred-pct { font-size: 0.79rem; font-weight: 600; color: var(--black); min-width: 38px; text-align: right; }
.unknown-box { background: var(--yellow-pale); border: 2px solid var(--yellow-mid); border-radius: 12px; padding: 2rem; text-align: center; margin-bottom: 1rem; }
.unknown-box h3 { color: var(--black); font-size: 1.1rem; margin-bottom: 0.5rem; }
.unknown-box p { color: var(--muted); font-size: 0.86rem; line-height: 1.7; }
.tcard { background: var(--white); border-radius: 10px; padding: 1.1rem 1.3rem; border: 1px solid var(--line); margin-bottom: 0.7rem; }
.tcard.cause    { border-left: 3px solid var(--green); }
.tcard.organic  { border-left: 3px solid var(--green-light); }
.tcard.chemical { border-left: 3px solid var(--yellow-mid); }
.tcard.prevent  { border-left: 3px solid #60A5FA; }
.tcard h4 { font-family: 'Outfit', sans-serif; font-size: 0.67rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: var(--green-mid); margin-bottom: 0.45rem; }
.tcard p  { font-size: 0.86rem; color: var(--ink); line-height: 1.7; margin-bottom: 0.25rem; }
.tcard .hi { color: var(--muted); font-size: 0.8rem; }

/* ── TAP-TO-CALL HELPLINE ── */
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
.helpline a {
    color: var(--yellow) !important;
    text-decoration: none !important;
    font-weight: 700 !important;
}
.helpline a:hover { text-decoration: underline !important; }

/* ── ABOUT ── */
.about-card { background: var(--green); border-radius: 16px; padding: 2.8rem; color: white; margin-bottom: 2rem; border-left: 5px solid var(--yellow); }
.about-card h2 { color: var(--yellow) !important; margin-bottom: 1rem !important; font-size: 1.7rem !important; }
.about-card p  { opacity: 0.8; line-height: 1.9; font-size: 0.94rem; margin-bottom: 0.9rem; }
.about-card .hi { color: rgba(255,255,255,0.45) !important; font-size: 0.84rem !important; margin-bottom: 0.9rem !important; display: block !important; }
.about-sig { color: var(--yellow) !important; font-weight: 600 !important; font-size: 0.9rem !important; opacity: 1 !important; }

/* ── FOOTER ── */
.footer { text-align: center; color: var(--muted); font-size: 0.78rem; padding: 2rem 0 0.5rem; border-top: 1px solid var(--line); margin-top: 3rem; }
.footer a { color: var(--green-mid); text-decoration: none; font-weight: 500; }
.footer a:hover { color: var(--green); }

/* ════════════════════════════════════════
   MOBILE RESPONSIVE
   ════════════════════════════════════════ */

/* ── DESKTOP (>768px): sidebar always fully expanded ── */
@media (min-width: 769px) {
    .ham-btn { display: none !important; }
    .block-container { padding: 0 2.5rem 4rem !important; }
}

/* ── TABLET (600–768px): sidebar shrinks to a narrow strip ── */
@media (max-width: 768px) {
    /* Narrow strip — shows the green brand bar so user knows sidebar exists */
    section[data-testid="stSidebar"] {
        min-width: 52px !important;
        max-width: 52px !important;
        overflow: hidden !important;
        transition: min-width 0.25s ease, max-width 0.25s ease !important;
    }
    /* Hide all text/labels in collapsed strip — only the green bar shows */
    section[data-testid="stSidebar"] .sb-brand-name,
    section[data-testid="stSidebar"] .sb-brand-sub,
    section[data-testid="stSidebar"] .sb-nav-label,
    section[data-testid="stSidebar"] .stRadio,
    section[data-testid="stSidebar"] hr,
    section[data-testid="stSidebar"] .sb-helpline,
    section[data-testid="stSidebar"] .sb-footer {
        opacity: 0 !important;
        pointer-events: none !important;
        transition: opacity 0.15s !important;
    }
    /* Hamburger sits inside the strip, top-left */
    .ham-btn {
        position: fixed;
        top: 12px;
        left: 6px;
        z-index: 9999;
        background: transparent;
        color: rgba(255,255,255,0.85);
        border: none;
        border-radius: 6px;
        width: 40px;
        height: 40px;
        font-size: 1.2rem;
        cursor: pointer;
        display: flex !important;
        align-items: center;
        justify-content: center;
        transition: background 0.15s;
        font-family: 'Outfit', sans-serif;
        line-height: 1;
    }
    .ham-btn:hover { background: rgba(255,255,255,0.12); }
    /* Push main content right of the strip */
    .block-container { padding: 0 1.2rem 3rem !important; }
    .hero { padding: 2rem 1.4rem; }
    .hero::after { display: none; }
    .stat-row { grid-template-columns: 1fr 1fr; gap: 0.8rem; }
    .crop-grid { grid-template-columns: 1fr 1fr; gap: 0.8rem; }
    .dg-grid  { grid-template-columns: 1fr; }
}

/* ── MOBILE (<600px): strip still visible, content stacks ── */
@media (max-width: 600px) {
    .block-container { padding: 0 0.8rem 2.5rem !important; }
    .hero { padding: 1.6rem 1.2rem; border-radius: 12px; }
    .hero h1 { font-size: 1.7rem !important; }
    .stat-row { grid-template-columns: 1fr; }
    .crop-grid { grid-template-columns: 1fr; }
    .stat-card, .crop-card { padding: 1.1rem; }
    [data-testid="column"] { min-width: 100% !important; flex: 1 1 100% !important; }
    .how-card { padding: 1.3rem 1rem; }
    .step-card { gap: 0.75rem; }
    .tcard { padding: 0.9rem 1rem; }
    .result-banner { padding: 1.1rem 1.2rem; }
    .result-banner h2 { font-size: 1.25rem !important; }
    .upload-wrap { padding: 1.4rem 1rem 0.8rem; }
    .about-card { padding: 1.8rem 1.4rem; }
    .page-header { padding: 1.8rem 0 1.4rem; }
    .page-header h1 { font-size: 1.7rem !important; }
    .dg-grid { grid-template-columns: 1fr; gap: 0.8rem; }
    .conf-row { flex-direction: column; align-items: flex-start; gap: 0.4rem; }
    .pred-lbl { font-size: 0.75rem; }
    .pred-pct { font-size: 0.73rem; min-width: 32px; }
}

/* ── EXPANDED STATE: when sidebar is open on mobile ── */
/* Streamlit adds aria-expanded="true" to the sidebar when open */
@media (max-width: 768px) {
    section[data-testid="stSidebar"][aria-expanded="true"] {
        min-width: 240px !important;
        max-width: 240px !important;
    }
    section[data-testid="stSidebar"][aria-expanded="true"] .sb-brand-name,
    section[data-testid="stSidebar"][aria-expanded="true"] .sb-brand-sub,
    section[data-testid="stSidebar"][aria-expanded="true"] .sb-nav-label,
    section[data-testid="stSidebar"][aria-expanded="true"] .stRadio,
    section[data-testid="stSidebar"][aria-expanded="true"] hr,
    section[data-testid="stSidebar"][aria-expanded="true"] .sb-helpline,
    section[data-testid="stSidebar"][aria-expanded="true"] .sb-footer {
        opacity: 1 !important;
        pointer-events: auto !important;
    }
    /* Larger tap targets when fully open */
    section[data-testid="stSidebar"][aria-expanded="true"] .stRadio [role="radiogroup"] label {
        padding: 0.9rem 1.1rem !important;
        font-size: 0.95rem !important;
    }
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# HAMBURGER BUTTON — visible on mobile inside the narrow green strip
# Toggles aria-expanded on the sidebar so CSS expands/collapses it
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<button class="ham-btn" onclick="toggleSidebar()" title="Open menu / मेनू खोलें">☰</button>
<script>
function toggleSidebar() {
    const doc = window.parent.document;
    const sidebar = doc.querySelector('[data-testid="stSidebar"]');
    if (!sidebar) return;
    const isOpen = sidebar.getAttribute('aria-expanded') === 'true';
    sidebar.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
    // Also try clicking Streamlit's own toggle so its internal state matches
    const btn = doc.querySelector('[data-testid="collapsedControl"]');
    if (btn) btn.click();
}
</script>
""", unsafe_allow_html=True)

# FIX 1 — CLASS NAMES: hardcoded sorted list so it works on Streamlit Cloud
#          (no dataset folder present there). Matches PlantVillage alphabetical order.
# ─────────────────────────────────────────────────────────────────────────────
PLANTVILLAGE_CLASSES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy",
]


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────

@st.cache_resource(show_spinner=False)
def load_model():
    import tensorflow as tf
    from huggingface_hub import hf_hub_download
    model_path = hf_hub_download(repo_id="jainmokshi/CropSense", filename="cropsense_model.h5")
    return tf.keras.models.load_model(model_path)


@st.cache_resource(show_spinner=False)
def load_class_names():
    # FIX 1: Use hardcoded list — not dict keys, not os.listdir.
    # This matches the model's training class index order reliably
    # on both local machines and Streamlit Cloud.
    return PLANTVILLAGE_CLASSES


def preprocess(image):
    # FIX 2: Handle RGBA and other non-RGB modes before processing
    if image.mode != "RGB":
        image = image.convert("RGB")
    img = image.resize((224, 224))
    arr = np.array(img, dtype=np.float32) / 255.0
    if arr.ndim == 2:                      # greyscale edge case
        arr = np.stack([arr, arr, arr], axis=-1)
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
        <div class='sb-brand-sub'>AI Crop Doctor · AI फसल डॉक्टर</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<span class='sb-nav-label'>Menu / मेनू</span>", unsafe_allow_html=True)

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

    st.markdown("<span class='sb-nav-label'>📞 Helpline / सहायता</span>", unsafe_allow_html=True)
    # FIX 3: tap-to-call link on mobile
    st.markdown("""
    <div class='sb-helpline'>
        <div class='sb-helpline-label'>Kisan Call Centre</div>
        <a href='tel:18001801551' style='text-decoration:none'>
            <div class='sb-helpline-num'>1800-180-1551</div>
        </a>
        <div class='sb-helpline-sub'>निःशुल्क · 24/7 · हिंदी उपलब्ध</div>
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
            with treatment advice in Hindi &amp; English. Built for real-world conditions —
            basic phones, imperfect lighting, no expertise needed.
        </p>
        <p class='hero-hi'>किसी भी फसल की पत्ती की फोटो अपलोड करें — तुरंत निदान और उपचार की जानकारी पाएं।<br>
        हिंदी और अंग्रेजी दोनों में। बिलकुल मुफ़्त।</p>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown("""
    <div class='stat-row'>
        <div class='stat-card'>
            <div class='stat-num'>35%</div>
            <div class='stat-label'>of India's annual crop production lost to pests and disease</div>
            <div class='stat-src'>भारत की वार्षिक फसल का 35% कीट और रोगों से नष्ट</div>
            <div class='stat-src'>ICAR · PlantDoc, IIT Gandhinagar (2019)</div>
        </div>
        <div class='stat-card'>
            <div class='stat-num'>54,000+</div>
            <div class='stat-label'>leaf images across 14 plant species used to train the AI model</div>
            <div class='stat-src'>14 फसलों की 54,000+ पत्ती छवियों पर AI प्रशिक्षित</div>
            <div class='stat-src'>PlantVillage Dataset · Hughes &amp; Salathé, Penn State (2015)</div>
        </div>
        <div class='stat-card'>
            <div class='stat-num'>38</div>
            <div class='stat-label'>disease classes detected — both healthy and diseased conditions</div>
            <div class='stat-src'>38 रोग वर्ग पहचाने जाते हैं — स्वस्थ और रोगग्रस्त दोनों</div>
            <div class='stat-src'>PlantVillage Dataset · Kaggle (CC BY-NC-SA 4.0)</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # How it works
    st.markdown("<span class='sec-label'>The process / प्रक्रिया</span>", unsafe_allow_html=True)
    st.markdown("<h2 class='sec-title'>How it <em>Works</em></h2>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="medium")
    for col, icon, title, desc, hi in [
        (c1, "📸", "Upload a Leaf Photo",
         "Take a close-up of the affected leaf in natural daylight. Any smartphone camera works.",
         "प्रभावित पत्ती की क्लोज़-अप फोटो दिन की रोशनी में लें।"),
        (c2, "🧠", "AI Analyses It",
         "ResNet50 scans the leaf against 38 disease patterns in seconds and returns a confidence-scored result.",
         "AI 38 रोग पैटर्न से मिलान करके सेकंड में परिणाम देता है।"),
        (c3, "💊", "Get Actionable Advice",
         "Diagnosis, cause, organic & chemical treatments, and prevention — in Hindi and English.",
         "निदान, कारण, जैविक/रासायनिक उपचार और बचाव — हिंदी और अंग्रेजी में।"),
    ]:
        with col:
            st.markdown(f"""
            <div class='how-card'>
                <div class='how-icon'>{icon}</div>
                <div class='how-title'>{title}</div>
                <div class='how-desc'>{desc}</div>
                <div class='how-hi'>{hi}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Crops — FIX 4: Tomato now shows 10 conditions + all tags; Corn shows Healthy tag
    st.markdown("<span class='sec-label'>Supported crops / समर्थित फसलें</span>", unsafe_allow_html=True)
    st.markdown("<h2 class='sec-title'>What CropSense <em>Knows</em></h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class='crop-grid'>
        <div class='crop-card'>
            <div class='crop-emoji'>🍅</div>
            <div class='crop-name'>Tomato — टमाटर</div>
            <div class='crop-name-hi'>10 conditions detected</div>
            <span class='dtag danger'>Early Blight</span>
            <span class='dtag danger'>Late Blight</span>
            <span class='dtag warn'>Leaf Mold</span>
            <span class='dtag warn'>Mosaic Virus</span>
            <span class='dtag'>Septoria Spot</span>
            <span class='dtag danger'>Spider Mites</span>
            <span class='dtag warn'>Target Spot</span>
            <span class='dtag'>Bacterial Spot</span>
            <span class='dtag danger'>Yellow Leaf Curl</span>
            <span class='dtag'>Healthy</span>
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
            <span class='dtag'>Healthy</span>
        </div>
        <div class='crop-card'>
            <div class='crop-emoji'>🍎</div>
            <div class='crop-name'>Apple — सेब</div>
            <div class='crop-name-hi'>4 conditions detected</div>
            <span class='dtag danger'>Apple Scab</span>
            <span class='dtag danger'>Black Rot</span>
            <span class='dtag warn'>Cedar Rust</span>
            <span class='dtag'>Healthy</span>
        </div>
        <div class='crop-card'>
            <div class='crop-emoji'>🍇</div>
            <div class='crop-name'>Grape — अंगूर</div>
            <div class='crop-name-hi'>4 conditions detected</div>
            <span class='dtag danger'>Black Rot</span>
            <span class='dtag warn'>Esca</span>
            <span class='dtag'>Leaf Blight</span>
            <span class='dtag'>Healthy</span>
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
        <h3>Ready to diagnose your crop? / अपनी फसल जांचें</h3>
        <p>Navigate to <strong>🔬 Detect Disease</strong> in the sidebar and upload your first leaf photo.</p>
        <p style='color: var(--green-mid); margin-top: 0.4rem; font-size: 0.84rem'>
            साइडबार में <strong>🔬 Detect Disease</strong> पर जाएं → पत्ती की फोटो अपलोड करें → तुरंत निदान पाएं
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
        <span class='page-header-chip'>User Guide / उपयोगकर्ता गाइड</span>
        <h1>How to Use <em>CropSense</em></h1>
        <p>Step-by-step instructions and best practices for accurate results.</p>
        <p class='hi'>सटीक परिणाम के लिए चरण-दर-चरण निर्देश और सर्वोत्तम तरीके।</p>
    </div>
    """, unsafe_allow_html=True)

    col_steps, col_tips = st.columns([1.15, 1], gap="large")

    with col_steps:
        st.markdown("<span class='sec-label'>Step by step / चरण दर चरण</span>", unsafe_allow_html=True)
        st.markdown("<h2 class='sec-title'>Getting <em>Started</em></h2>", unsafe_allow_html=True)

        for num, title, desc, hi in [
            ("1", "Open the Detect page",
             "Click '🔬 Detect Disease' in the left sidebar to go to the upload page.",
             "बाईं साइडबार में '🔬 Detect Disease' पर क्लिक करें।"),
            ("2", "Take a clear leaf photo",
             "Use your phone in natural daylight. Let the diseased leaf fill most of the frame. Avoid flash.",
             "दिन की रोशनी में फोटो लें। रोगग्रस्त पत्ती फ्रेम में भरी होनी चाहिए। फ्लैश बंद रखें।"),
            ("3", "Upload the image",
             "Click 'Browse files' or drag and drop your photo. JPG, JPEG, and PNG all work.",
             "'Browse files' पर क्लिक करें या फोटो खींचकर छोड़ें। JPG, JPEG और PNG सभी चलते हैं।"),
            ("4", "Wait a few seconds",
             "The AI analyses your leaf and returns its top prediction with a confidence score.",
             "AI पत्ती का विश्लेषण करके शीर्ष अनुमान और विश्वास स्कोर देता है।"),
            ("5", "Read the diagnosis",
             "You get the disease name, cause, organic and chemical treatments, and prevention tips — in Hindi & English.",
             "रोग का नाम, कारण, जैविक/रासायनिक उपचार और बचाव — हिंदी और अंग्रेजी में।"),
            ("6", "Low confidence shown?",
             "If confidence is below 45%, the photo isn't clear enough. Retake in better lighting, closer to the leaf.",
             "यदि विश्वास 45% से कम है — बेहतर रोशनी में, पत्ती के करीब से फोटो दोबारा लें।"),
            ("7", "Still unsure? Call the helpline",
             "Dial 1800-180-1551 (free, 24/7) and speak with a Kisan expert in Hindi.",
             "1800-180-1551 पर कॉल करें (निःशुल्क, 24/7) — हिंदी में किसान विशेषज्ञ से बात करें।"),
        ]:
            st.markdown(f"""
            <div class='step-card'>
                <div class='step-num'>{num}</div>
                <div class='step-content'>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                    <p class='hi'>{hi}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

        if st.button("🔬 Go to Detect Disease →", type="primary"):
            st.session_state.page = "Detect"
            st.rerun()

    with col_tips:
        st.markdown("<span class='sec-label'>Best practices / सर्वोत्तम तरीके</span>", unsafe_allow_html=True)
        st.markdown("<h2 class='sec-title'>Photo <em>Tips</em></h2>", unsafe_allow_html=True)

        for icon, title, desc, hi in [
            ("☀️", "Natural daylight only",
             "Sunlight gives the most accurate colours. Indoor lighting distorts the green tones the model relies on.",
             "धूप में सबसे सटीक रंग मिलते हैं। इनडोर लाइट से हरे रंग विकृत हो जाते हैं।"),
            ("📏", "15–20 cm distance",
             "Hold your phone about 15–20 cm from the leaf so it fills most of the frame.",
             "फोन को पत्ती से लगभग 15-20 सेमी दूर रखें ताकि पत्ती फ्रेम में भरी रहे।"),
            ("🍃", "One leaf per photo",
             "Multiple leaves in one shot significantly reduce accuracy. Focus on one clearly affected leaf.",
             "एक फोटो में एक ही पत्ती। कई पत्तियाँ सटीकता कम करती हैं।"),
            ("🔄", "Check both sides",
             "Many diseases appear differently on the top and bottom. Photograph both if symptoms differ.",
             "कई रोग ऊपर और नीचे अलग दिखते हैं। दोनों तरफ से फोटो लें।"),
            ("🎯", "Tap to focus first",
             "Wait for your camera to lock focus before shooting. Blur is the top cause of wrong predictions.",
             "शूट करने से पहले कैमरे को फोकस करने दें। धुंधलापन गलत अनुमान का सबसे बड़ा कारण है।"),
            ("⏱️", "Detect early",
             "Upload photos as soon as you notice unusual colour, spots, or texture — early detection saves crops.",
             "असामान्य रंग, धब्बे या बनावट दिखते ही फोटो अपलोड करें — जल्दी पहचान फसल बचाती है।"),
        ]:
            st.markdown(f"""
            <div class='tip-card'>
                <h4>{icon} {title}</h4>
                <p>{desc}</p>
                <p class='hi'>{hi}</p>
            </div>
            """, unsafe_allow_html=True)

    # Limitations
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<span class='sec-label'>Honest limitations / ईमानदार सीमाएं</span>", unsafe_allow_html=True)
    st.markdown("<h2 class='sec-title'>Known <em>Failure Cases</em></h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: var(--muted); font-size: 0.9rem; margin-bottom: 1.3rem; max-width: 660px'>CropSense is built for real-world use. Here are the cases where accuracy drops — and why.<br><span style='color:rgba(0,0,0,0.35);font-size:0.82rem'>CropSense वास्तविक उपयोग के लिए बना है। यहाँ वे मामले हैं जहाँ सटीकता कम हो सकती है।</span></p>", unsafe_allow_html=True)

    fc1, fc2, fc3 = st.columns(3)
    for col, title, desc in [
        (fc1, "🌑 Poor lighting / कम रोशनी", "Images taken indoors or at night lack the colour and texture signals the model trained on. Always photograph in daylight."),
        (fc2, "📷 Blurry or overexposed / धुंधला फोटो", "Blur destroys edge features; overexposure washes out colour. Both cause low confidence or wrong predictions."),
        (fc3, "🌾 Unsupported crops / असमर्थित फसलें", "CropSense knows 14 crops. Uploading wheat, rice, or sugarcane will return a misleading result."),
        (fc1, "🖼️ Non-leaf images / पत्ती के बिना फोटो", "Uploading soil, fruit, or a whole plant bypasses leaf detection and returns a meaningless result."),
        (fc2, "🦠 Very early symptoms / बहुत शुरुआती लक्षण", "Diseases with extremely mild symptoms may be classified as 'Healthy'. Visible symptoms are needed."),
        (fc3, "🔬 Lab vs. field gap / प्रयोगशाला बनाम खेत", "PlantVillage images were taken in controlled conditions. Real farm photos with dirt or water drops score lower confidence."),
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
        <strong>Krishi Vigyan Kendra (KVK)</strong> or call <strong><a href='tel:18001801551' style='color:var(--green)'>1800-180-1551</a></strong> (free, 24/7).<br>
        <span style='color:rgba(0,0,0,0.4);font-size:0.82rem'>CropSense एक सहायक उपकरण है, कृषि विशेषज्ञ का विकल्प नहीं।
        परिणाम संदिग्ध हो तो अपने नजदीकी KVK से संपर्क करें।</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Quick disease guide
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<span class='sec-label'>Reference / संदर्भ</span>", unsafe_allow_html=True)
    st.markdown("<h2 class='sec-title'>Quick Disease <em>Guide</em></h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: var(--muted); font-size: 0.9rem; margin-bottom: 1.3rem'>Common symptoms for key crops — useful when identifying issues in the field before uploading.<br><span style='color:rgba(0,0,0,0.35);font-size:0.82rem'>मुख्य फसलों के सामान्य लक्षण — फोटो अपलोड करने से पहले खेत में पहचान के लिए उपयोगी।</span></p>", unsafe_allow_html=True)

    st.markdown("""
    <div class='dg-grid'>
        <div class='dg-card'>
            <h4>🍅 Tomato / टमाटर</h4>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Early Blight / अगेती झुलसा</strong><span>Concentric brown rings on lower leaves first</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Late Blight / पछेती झुलसा</strong><span>Dark water-soaked lesions, spreads rapidly</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Leaf Mold / पत्ती फफूंद</strong><span>Yellow patches above, mold growth on underside</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Mosaic Virus / मोजेक विषाणु</strong><span>Mottled yellow-green patterns, stunted growth</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Spider Mites / मकड़ी घुन</strong><span>Fine webbing on leaf, bronze discolouration</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Septoria Spot / सेप्टोरिया</strong><span>Small circular spots with dark border</span></div></div>
        </div>
        <div class='dg-card'>
            <h4>🥔 Potato / आलू &amp; 🌽 Corn / मक्का</h4>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Potato Early Blight / अगेती झुलसा</strong><span>Circular brown spots on older leaves</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Potato Late Blight / पछेती झुलसा</strong><span>Most destructive — dark lesions + tuber rot</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Corn Common Rust / सामान्य रतुआ</strong><span>Oval rust-coloured pustules on both leaf surfaces</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Gray Leaf Spot / ग्रे धब्बा</strong><span>Long rectangular grey-brown lesions</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Northern Leaf Blight / उत्तरी झुलसा</strong><span>Long cigar-shaped grey-green lesions</span></div></div>
        </div>
        <div class='dg-card'>
            <h4>🍎 Apple / सेब</h4>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Apple Scab / खुरदरापन</strong><span>Olive-green to black spots on leaves and fruit</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Black Rot / काला सड़न</strong><span>Brown concentric rings on fruit; frog-eye spots on leaves</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Cedar Apple Rust / सीडर रतुआ</strong><span>Bright orange spots on upper leaf surface</span></div></div>
        </div>
        <div class='dg-card'>
            <h4>🍇 Grape / अंगूर &amp; 🫑 Pepper / शिमला मिर्च</h4>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Grape Black Rot / काला सड़न</strong><span>Reddish-brown spots, shrivelled black berries</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Esca / एस्का</strong><span>Tiger-stripe leaf pattern, wood decay</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Grape Leaf Blight / पत्ती झुलसा</strong><span>Irregular brown spots with yellow halos</span></div></div>
            <div class='dg-item'><div class='dg-dot'></div><div class='dg-text'><strong>Pepper Bacterial Spot / जीवाणु धब्बा</strong><span>Water-soaked spots turning yellow-brown</span></div></div>
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
        <span class='page-header-chip'>AI Diagnosis / AI निदान</span>
        <h1>Detect <em>Disease</em></h1>
        <p>Upload a clear leaf photo for an instant AI-powered diagnosis.</p>
        <p class='hi'>तुरंत AI निदान के लिए एक साफ पत्ती की फोटो अपलोड करें।</p>
    </div>
    """, unsafe_allow_html=True)

    col_up, col_res = st.columns([1, 1.6], gap="large")

    with col_up:
        st.markdown("""
        <div class='upload-wrap'>
            <div style='font-size: 2.4rem; margin-bottom: 0.6rem'>🌿</div>
            <h3>Upload Leaf Photo</h3>
            <p>पत्ती की फोटो अपलोड करें</p>
            <p>Drag &amp; drop or browse</p>
            <p style='color: var(--green-light); font-size: 0.78rem'>JPG · JPEG · PNG supported</p>
        </div>
        """, unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "Choose leaf image",
            type=["jpg", "jpeg", "png"],
            label_visibility="collapsed"
        )

        if uploaded_file:
            image = Image.open(uploaded_file)
            # FIX 2: convert to RGB early for correct display too
            if image.mode != "RGB":
                image = image.convert("RGB")
            st.image(image, use_container_width=True, caption="Uploaded leaf / अपलोड की गई पत्ती")
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
                                This usually means the image is blurry, too dark, shows multiple leaves,
                                or the crop is not in the current dataset.<br><br>
                                <strong>बेहतर रोशनी में एक पत्ती की साफ फोटो लें और दोबारा अपलोड करें।</strong><br>
                                <span style='font-size:0.82rem;color:var(--muted)'>
                                आत्मविश्वास {conf*100:.1f}% है — {int(THRESHOLD*100)}% सीमा से कम।
                                </span>
                            </p>
                        </div>
                        """, unsafe_allow_html=True)

                        st.markdown("<div class='top3'><h5>Top guesses (low confidence) / शीर्ष अनुमान</h5>", unsafe_allow_html=True)
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

                        # FIX 5: clean bar_colors — no pointless list comprehension
                        bar_colors = ["#2D6A4F", "#52B788", "#95D5B2"]
                        st.markdown("<div class='top3'><h5>📊 Top 3 predictions / शीर्ष 3 अनुमान</h5>", unsafe_allow_html=True)
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
                        """, unsafe_allow_html=True)

                        # FIX 3: tap-to-call helpline
                        st.markdown("""
                        <div class='helpline'>
                            📞 Kisan Call Centre &nbsp;·&nbsp;
                            <a href='tel:18001801551'>1800-180-1551</a>
                            &nbsp;·&nbsp; Free / निःशुल्क &nbsp;·&nbsp; 24/7 &nbsp;·&nbsp; Hindi &amp; Regional Languages
                        </div>
                        """, unsafe_allow_html=True)

                # FIX 4: catch HuggingFace download failures, not just FileNotFoundError
                except Exception as e:
                    err_str = str(e).lower()
                    if "404" in err_str or "not found" in err_str or "repository" in err_str or "hf_hub" in err_str:
                        st.warning("""
                        **Model could not be downloaded from Hugging Face.**

                        Check that `jainmokshi/CropSense` repo is public and `cropsense_model.h5` exists there.
                        If you just uploaded a new model, wait 2–3 minutes and refresh.

                        *मॉडल Hugging Face से डाउनलोड नहीं हो सका। कृपया 2-3 मिनट बाद दोबारा कोशिश करें।*
                        """)
                    else:
                        st.error(f"Unexpected error: {e}")
                        st.info("Check that `treatment_data.py` is in the same directory as `app.py`.")

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
        <span class='page-header-chip'>Builder's Note / निर्माता का नोट</span>
        <h1>The <em>Why</em> Behind CropSense</h1>
        <p>A personal note from the person who built this.</p>
        <p class='hi'>इसे बनाने वाले की ओर से एक व्यक्तिगत संदेश।</p>
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
        <span class='hi'>भारत एक कृषि प्रधान देश है। हमारी 60% से अधिक जनसंख्या खेती पर निर्भर है।
        फिर भी हर साल किसान उन फसल रोगों से अपनी पूरी फसल खो देते हैं जिन्हें वे समय पर पहचान नहीं पाते।</span>
        <p>
        I built CropSense because most existing agricultural AI tools are English-only, require expensive
        equipment, and are built for perfect studio-quality images. A farmer with a basic Android phone
        and an imperfect photo shouldn't be left without help.
        </p>
        <span class='hi'>मैंने CropSense इसलिए बनाया क्योंकि अधिकांश कृषि AI उपकरण केवल अंग्रेजी में हैं।
        एक साधारण Android फोन वाले किसान को सहायता से वंचित नहीं रहना चाहिए।</span>
        <p>
        CropSense gives that farmer an instant diagnosis in Hindi, with practical treatment advice they
        can actually act on — no cost, no English required, no technical knowledge needed.
        </p>
        <span class='hi'>CropSense उस किसान को हिंदी में तुरंत निदान देता है — बिना किसी लागत, बिना अंग्रेजी,
        बिना किसी तकनीकी ज्ञान के।</span>
        <p>
        This is not just an AI model project. It is an AI product system designed under real-world
        constraints: low-quality images, regional language needs, and users with zero technical background.
        The gap between "lab accuracy" and "field reality" is the problem I spent the most time thinking about.
        </p>
        <span class='hi'>यह केवल एक AI मॉडल प्रोजेक्ट नहीं है। यह वास्तविक परिस्थितियों के लिए बनाया गया
        AI उत्पाद है — कम गुणवत्ता की छवियां, क्षेत्रीय भाषाएं, शून्य तकनीकी पृष्ठभूमि।</span>
        <p class='about-sig'>— Mokshi Jain</p>
    </div>
    """, unsafe_allow_html=True)

    col_prob, col_sol = st.columns(2, gap="large")

    with col_prob:
        st.markdown("<span class='sec-label'>The challenge / चुनौती</span>", unsafe_allow_html=True)
        st.markdown("<h2 class='sec-title'>Real <em>Problems</em></h2>", unsafe_allow_html=True)

        for icon, title, desc, hi in [
            ("📉", "Massive crop losses",
             "Over 35% of India's annual crop production is lost to pests and disease — most of it preventable with early detection.",
             "भारत की 35% से अधिक वार्षिक फसल कीट और रोगों से नष्ट होती है — अधिकांश समय पर पहचान से रोका जा सकता है।"),
            ("🌐", "Language barrier",
             "Most agricultural AI tools are English-only. The majority of Indian farmers are far more comfortable in Hindi or regional languages.",
             "अधिकांश कृषि AI उपकरण केवल अंग्रेजी में हैं। भारतीय किसान हिंदी या क्षेत्रीय भाषाओं में अधिक सहज हैं।"),
            ("📱", "Technology gap",
             "Existing tools assume high-quality cameras and stable internet. Most smallholder farmers use basic Android phones with 2G/3G data.",
             "मौजूदा उपकरण उच्च गुणवत्ता कैमरे और स्थिर इंटरनेट मानते हैं। अधिकांश किसानों के पास 2G/3G का Android फोन है।"),
            ("⏱️", "Delayed action",
             "By the time a farmer reaches an agricultural expert, the disease has already spread — and the window for effective action has closed.",
             "जब तक किसान कृषि विशेषज्ञ तक पहुंचता है, रोग फैल चुका होता है — प्रभावी कार्रवाई की खिड़की बंद हो जाती है।"),
        ]:
            st.markdown(f"""
            <div class='step-card'>
                <div class='step-num' style='background:var(--green-pale);color:var(--green);font-size:1.2rem'>{icon}</div>
                <div class='step-content'>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                    <p class='hi'>{hi}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_sol:
        st.markdown("<span class='sec-label'>Our approach / हमारा तरीका</span>", unsafe_allow_html=True)
        st.markdown("<h2 class='sec-title'>The <em>Solutions</em></h2>", unsafe_allow_html=True)

        for icon, title, desc, hi in [
            ("🗣️", "Bilingual by design",
             "Every diagnosis, treatment, and tip is available in Hindi and English — no translation step needed.",
             "हर निदान, उपचार और सुझाव हिंदी और अंग्रेजी में — कोई अनुवाद चरण नहीं।"),
            ("📷", "Real-world images",
             "Trained with heavy augmentation (rotation, blur, brightness variation) to handle real phone camera photos.",
             "वास्तविक फोन कैमरा फोटो को संभालने के लिए भारी augmentation के साथ प्रशिक्षित।"),
            ("💊", "Actionable advice",
             "We don't just name the disease — we give organic remedies, chemical options, yield loss estimates, and prevention tips.",
             "हम केवल रोग का नाम नहीं देते — जैविक उपाय, रासायनिक विकल्प, उपज हानि अनुमान और बचाव के सुझाव देते हैं।"),
            ("🧠", "Transparent uncertainty",
             "When the model isn't confident, it says so clearly. No false positives that could mislead a farmer into wrong treatment.",
             "जब मॉडल आश्वस्त नहीं होता, वह स्पष्ट रूप से कहता है। गलत उपचार की ओर किसान को भ्रमित करने वाले झूठे परिणाम नहीं।"),
            ("⚡", "Instant and free",
             "No sign-up, no cost, no app download. Upload from any browser and get a structured diagnosis in seconds.",
             "कोई साइन-अप नहीं, कोई लागत नहीं, कोई ऐप डाउनलोड नहीं। किसी भी ब्राउज़र से अपलोड करें और सेकंड में निदान पाएं।"),
        ]:
            st.markdown(f"""
            <div class='step-card'>
                <div class='step-num' style='background:var(--yellow);color:var(--black);font-size:1.1rem'>{icon}</div>
                <div class='step-content'>
                    <h4>{title}</h4>
                    <p>{desc}</p>
                    <p class='hi'>{hi}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<span class='sec-label'>Under the hood / तकनीक</span>", unsafe_allow_html=True)
    st.markdown("<h2 class='sec-title'>Tech <em>Stack</em></h2>", unsafe_allow_html=True)

    ts1, ts2, ts3, ts4 = st.columns(4)
    for col, icon, label, detail in [
        (ts1, "🧠", "Model", "ResNet50 · Transfer Learning · TensorFlow 2.13 · Keras"),
        (ts2, "🖼️", "Data", "PlantVillage Dataset · 54,000+ images · 38 classes"),
        (ts3, "🌐", "App", "Streamlit · PIL · NumPy · Python 3.11"),
        (ts4, "🚀", "Deploy", "Hugging Face (model) · Streamlit Cloud (app)"),
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