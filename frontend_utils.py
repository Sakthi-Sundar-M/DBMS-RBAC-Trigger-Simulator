import os
import streamlit as st

@st.cache_data
def get_css_content() -> str:
    """Reads the static CSS stylesheet from disk."""
    css_path = os.path.join(os.path.dirname(__file__), "static", "css", "styles.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def load_css():
    """
    Injects the separated static stylesheet into the Streamlit app.
    Streamlit also serves this file at /app/static/css/styles.css via enableStaticServing.
    """
    css = get_css_content()
    if css:
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

@st.cache_data
def get_template(template_name: str) -> str:
    """Reads an HTML template from the templates/ directory."""
    template_path = os.path.join(os.path.dirname(__file__), "templates", template_name)
    if os.path.exists(template_path):
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def render_template(template_name: str, context: dict = None) -> str:
    """Renders an HTML template with variable replacement."""
    content = get_template(template_name)
    if not content:
        return ""
    if context:
        for k, v in context.items():
            content = content.replace(f"{{{{ {k} }}}}", str(v))
    return content

def render_brand_header(is_connected: bool = True):
    """Renders the top branding header banner from templates/brand_header.html."""
    status_class = "online" if is_connected else "offline"
    status_text = "PostgreSQL connected" if is_connected else "PostgreSQL offline: simulator mode"
    html_content = render_template("brand_header.html", {
        "status_class": status_class,
        "status_text": status_text
    })
    st.markdown(html_content, unsafe_allow_html=True)

def render_sidebar_role_card(formatted_role_name: str, role_desc: str):
    """Renders the active role information card from templates/sidebar_role_card.html."""
    html_content = render_template("sidebar_role_card.html", {
        "role_name": formatted_role_name,
        "role_desc": role_desc
    })
    st.sidebar.markdown(html_content, unsafe_allow_html=True)

def render_sidebar_bio():
    """Renders the developer and team profile from templates/sidebar_bio.html."""
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Developer & Team Profile")
    html_content = render_template("sidebar_bio.html")
    st.sidebar.markdown(html_content, unsafe_allow_html=True)

def render_defense_depth_grid():
    """Renders the 3-tier defense-in-depth grid from templates/defense_depth.html."""
    html_content = render_template("defense_depth.html")
    st.markdown(html_content, unsafe_allow_html=True)
