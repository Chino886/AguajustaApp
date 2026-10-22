from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Prototipo AguaJusta", page_icon="💧", layout="centered")

# Quita márgenes de Streamlit para que la app se vea como en el celular
st.markdown(
    """
    <style>
      .block-container {padding-top: 1rem; padding-bottom: 0; max-width: 520px;}
      header[data-testid="stHeader"] {display: none;}
      footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = (Path(__file__).parent / "prototipo.html").read_text(encoding="utf-8")

# La página del prototipo no trae <html>/<body>; se los agregamos aquí
page = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  html, body {{margin: 0; height: 100%;}}
  body {{font: 14px system-ui, sans-serif;}}
  [hidden] {{display: none !important;}}
</style>
</head>
<body>
{html}
</body>
</html>"""

components.html(page, height=900, scrolling=True)
