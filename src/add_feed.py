import streamlit as st

from utils import add_rss_feed_to_config, load_feeds, load_feeds_config


st.title("Add a new RSS feed url")

with st.form("my_form"): # TODO change the name here

    feed_name = st.text_input("RSS feed name")

    feed_url = st.text_input("RSS feed url")

    submitted = st.form_submit_button("Submit")
    if submitted:
        add_rss_feed_to_config(feed_name, feed_url)
        load_feeds_config()
        load_feeds()
        st.success("Your RSS feed has been added properly.", icon=":material/check_circle:")
