import streamlit as st

from utils import update_rss_feeds, remove_rss_feeds, load_feeds, load_feeds_config

for index, feed in enumerate(st.session_state["flux_rss_url"]):

    with st.form(key=f"update_rss_feed_{index}"):
    
        feed_name = st.text_input("RSS feed name.", feed["name"]) #, key=feed["name"])
        feed_url = st.text_input("RSS feed url.", feed["url"]) #, key=feed["url"])

        submitted = st.form_submit_button("Submit")

        if submitted:

            is_update_ok = update_rss_feeds(
                old_feed_name=feed["name"],
                old_feed_url=feed["url"],
                new_feed_name=feed_name,
                new_url_name=feed_url
            )

            if is_update_ok:
                load_feeds_config()
                load_feeds()
                st.success("Your RSS feed has been updated properly.", icon=":material/check_circle:")

    if st.button(
        "Remove this feed",
        key=f"remove_rss_feed_{index}",
        on_click=remove_rss_feeds,
        args=[feed["name"], feed["url"]]
    ):
        st.success("Your RSS feed has been removed properly.", icon=":material/check_circle:")
