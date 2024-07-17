import logging

import streamlit as st

from utils import load_feeds, load_feeds_config

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)


# Analyse du flux RSS
if "feeds_to_update" not in st.session_state:
    st.session_state["feeds_to_update"] = True

if "flux_rss_url" not in st.session_state:
    load_feeds_config()

if "flux_rss" not in st.session_state or st.session_state["feeds_to_update"] == True:
    load_feeds()

if "actual_rss_feed" not in st.session_state:
    if len(st.session_state["flux_rss_url"]) > 0:
        st.session_state["actual_rss_feed"] = st.session_state["flux_rss_url"][0]["name"]

display_feed = st.Page("display_feed.py", title="Display my Feeds", icon=":material/newspaper:")
add_feed = st.Page("add_feed.py", title="Add a new RSS feeds", icon=":material/add_circle:")
update_feed = st.Page("update_feed.py", title="Update RSS feeds", icon=":material/edit:")

pg = st.navigation([display_feed, add_feed, update_feed])

st.set_page_config(page_title="RSS Feeder", page_icon=":material/edit:")

pg.run()
