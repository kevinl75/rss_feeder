import requests
import streamlit as st
import feedparser

# URL du flux RSS
url = "https://www.lemonde.fr/rss/une.xml"
url_libe = "https://www.liberation.fr/arc/outboundfeeds/rss-all/category/politique/?outputType=xml"

# Analyse du flux RSS
feed_monde = feedparser.parse(url)
feed_libe = feedparser.parse(url_libe)
# Extraction des données
st.title("RSS feeder.")

with st.expander("Open to see more news about le Monde:"):
    for entry in feed_monde.entries:
        c = st.container()
        c.subheader(entry.title)
        c.write(entry.description)
        c.write(entry.published)
        c.write(entry.link)
        c.divider()

st.divider()

with st.expander("Open to see more news about le libe:"):
    for entry in feed_libe.entries:
        c = st.container()
        c.subheader(entry.title)
        c.write(entry.description)
        c.write(entry.published)
        c.write(entry.link)
        c.divider()
