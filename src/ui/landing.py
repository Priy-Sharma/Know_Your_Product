"""Landing page sections, split out from app.py so app.py stays readable."""
import streamlit as st

from config import APP_NAME, APP_TAGLINE, CATEGORIES, STEPS


def render_hero():
    st.markdown(f'<span class="kyp-badge">{APP_TAGLINE}</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="kyp-title">{APP_NAME}</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="kyp-subtitle">Scan product labels, discover ingredients, '
        "and understand what you&rsquo;re putting on (or in) your body.</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="kyp-description">Our AI reads the label, identifies '
        "ingredients, and explains their purpose, potential benefits, "
        "possible risks, and safety considerations &mdash; in simple "
        "terms.</div>",
        unsafe_allow_html=True,
    )


def render_upload_card():
    """Renders the dashed upload card and returns the uploaded file, if any."""
    st.markdown('<div class="kyp-upload-card">', unsafe_allow_html=True)
    st.markdown("### 📤 Upload a photo of your product label")
    st.markdown("Clear and well-lit images work best.")
    uploaded_file = st.file_uploader(
        label="Choose Image",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed",
    )
    st.caption("JPG · PNG · JPEG")
    st.markdown("</div>", unsafe_allow_html=True)
    return uploaded_file


def render_categories():
    st.markdown("#### Examples of products you can analyze")
    cols = st.columns(len(CATEGORIES))
    backgrounds = ["#eaf3ec", "#f3ede4", "#e6eef6", "#f6ebe8"]
    for col, cat, bg in zip(cols, CATEGORIES, backgrounds):
        with col:
            st.markdown(
                f'<div class="kyp-category-card" style="background:{bg};">'
                f'<div style="font-size:1.4rem;">{cat["emoji"]}</div>'
                f'<h4>{cat["name"]}</h4>'
                f'<p>{cat["desc"]}</p>'
                "</div>",
                unsafe_allow_html=True,
            )


def render_steps():
    cols = st.columns(len(STEPS))
    for col, step in zip(cols, STEPS):
        with col:
            st.markdown(
                '<div class="kyp-step">'
                f'<div class="kyp-step-emoji">{step["emoji"]}</div>'
                f'<h5>{step["title"]}</h5>'
                f'<p>{step["desc"]}</p>'
                "</div>",
                unsafe_allow_html=True,
            )
