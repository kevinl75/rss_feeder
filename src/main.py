import streamlit as st
import feedparser

# Analyse du flux RSS
if "flux_rss_url" not in st.session_state:
    st.session_state["flux_rss_url"] = {
        "le_monde": "https://www.lemonde.fr/rss/une.xml",
        "libe" : "https://www.liberation.fr/arc/outboundfeeds/rss-all/category/politique/?outputType=xml"
    }

if "flux_rss" not in st.session_state:
    st.session_state["flux_rss"] = {}
    for k, v in st.session_state["flux_rss_url"].items():
        st.session_state["flux_rss"][k] = feedparser.parse(v)

if "actual_rss_feed" not in st.session_state:
    st.session_state["actual_rss_feed"] = "le_monde"
# Extraction des données
st.title("RSS feeder.")


def set_default_rss_feed(rss_feed_name: str):
    st.session_state["actual_rss_feed"] = rss_feed_name


def generate_sidebar():
    sidebar = st.sidebar
    
    sidebar.text("Available RSS feeds:")

    for rss_feed_name, _ in st.session_state["flux_rss_url"].items():
        sidebar.button(
            label=rss_feed_name,
            key=rss_feed_name,
            on_click=set_default_rss_feed,
            args=[rss_feed_name],
            use_container_width=True
        )
    return sidebar


generate_sidebar()

for entry in st.session_state["flux_rss"][st.session_state["actual_rss_feed"]].entries:
    c = st.container()
    c.subheader(entry.title)
    c.write(entry.description)
    c.write(entry.published)
    c.write(entry.link)
    c.divider()
