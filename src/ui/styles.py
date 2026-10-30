"""Custom CSS injected into the Streamlit app to approximate the mock."""
from config import ACCENT_COLOR, ACCENT_LIGHT

CSS = f"""
<style>
    #MainMenu, footer {{visibility: hidden;}}
    .block-container {{
        padding-top: 2rem;
        max-width: 980px;
    }}

    .kyp-badge {{
        display: inline-block;
        background: {ACCENT_LIGHT};
        color: {ACCENT_COLOR};
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.06em;
        padding: 0.3rem 0.9rem;
        border-radius: 999px;
        margin-bottom: 1rem;
    }}

    .kyp-title {{
        font-size: 3rem;
        font-weight: 800;
        color: #14281f;
        margin: 0 0 0.75rem 0;
        line-height: 1.1;
    }}

    .kyp-subtitle {{
        font-size: 1.25rem;
        color: #2c3b33;
        margin-bottom: 0.75rem;
        line-height: 1.4;
    }}

    .kyp-description {{
        color: #6b7a71;
        font-size: 1rem;
        margin-bottom: 1.5rem;
        max-width: 640px;
    }}

    .kyp-upload-card {{
        border: 2px dashed #c9d6cd;
        border-radius: 16px;
        padding: 2rem 1.5rem;
        text-align: center;
        background: #fbfdfc;
    }}

    .kyp-upload-card h3 {{
        margin-bottom: 0.25rem;
        color: #14281f;
    }}

    .kyp-upload-card p {{
        color: #8a9790;
        margin-bottom: 1rem;
    }}

    .kyp-category-card {{
        border-radius: 14px;
        padding: 1.1rem 1.2rem;
        height: 100%;
    }}

    .kyp-category-card h4 {{
        margin: 0.4rem 0 0.1rem 0;
        color: #14281f;
    }}

    .kyp-category-card p {{
        margin: 0;
        font-size: 0.85rem;
        color: #6b7a71;
    }}

    .kyp-step {{
        text-align: center;
        padding: 0.5rem;
    }}

    .kyp-step .kyp-step-emoji {{
        font-size: 1.5rem;
    }}

    .kyp-step h5 {{
        margin: 0.4rem 0 0.1rem 0;
        color: #14281f;
    }}

    .kyp-step p {{
        margin: 0;
        font-size: 0.85rem;
        color: #6b7a71;
    }}

    .kyp-ingredient-list li {{
        margin-bottom: 0.4rem;
    }}

    div[data-testid="stFileUploaderDropzone"] {{
        border-radius: 12px !important;
    }}
</style>
"""
