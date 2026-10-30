"""Know Your Product — Streamlit entry point.

Flow: show the landing page -> user uploads a label photo -> OCR pulls raw
text off the image -> an LLM call filters that down to just the ingredient
names -> ingredients are shown as a bullet list.
"""
import streamlit as st

from config import APP_NAME
from src.ingredients.parser import extract_ingredients
from src.ocr.extractor import extract_text
from src.ui.landing import render_categories, render_hero, render_steps, render_upload_card
from src.ui.styles import CSS

st.set_page_config(page_title=APP_NAME, page_icon="🌿", layout="centered")
st.markdown(CSS, unsafe_allow_html=True)

render_hero()
uploaded_file = render_upload_card()

if uploaded_file is not None:
    # ~2"x3" preview (192x288px at 96dpi) instead of a full-width image.
    preview_col, _ = st.columns([1, 3])
    with preview_col:
        st.image(uploaded_file, caption="Uploaded label", width=192)

    with st.spinner("Reading the label..."):
        raw_text = extract_text(uploaded_file)

    with st.expander("Raw OCR text (debug)"):
        st.text(raw_text if raw_text else "No text detected — try a clearer photo.")

    if raw_text:
        with st.spinner("Identifying ingredients..."):
            ingredients = extract_ingredients(raw_text)

        st.markdown("### 🧾 Ingredients detected")
        if ingredients:
            bullet_html = "<ul class='kyp-ingredient-list'>" + "".join(
                f"<li>{name}</li>" for name in ingredients
            ) + "</ul>"
            st.markdown(bullet_html, unsafe_allow_html=True)
        else:
            st.warning(
                "Couldn't confidently identify an ingredient list in this "
                "image. Try a photo where the ingredients panel fills more "
                "of the frame."
            )
    else:
        st.warning("No readable text found in that image — try a clearer, well-lit photo.")

st.divider()
render_categories()
st.divider()
render_steps()
