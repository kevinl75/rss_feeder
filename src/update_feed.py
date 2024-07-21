import streamlit as st

from utils import update_rss_feeds, remove_rss_feeds, load_feeds, load_feeds_config


st.header("Remove a RSS feed.")

with st.form(key="remove_rss_feed"):
    feed_name = st.text_input("Enter the RSS feed name to remove.")
    submitted = st.form_submit_button("Submit")

    if submitted:

        is_removed = remove_rss_feeds(feed_name)

        if is_removed:
            load_feeds_config()
            load_feeds()
            if st.session_state["actual_rss_feed"] == feed_name:
                if len(st.session_state["flux_rss_url"]) > 0:
                    st.session_state["actual_rss_feed"] = st.session_state["flux_rss_url"][0]["name"]
            st.success("Your RSS feed has been removed properly.", icon=":material/check_circle:")
        else:
            st.error("An error occured while removing your feed. Are you sure this feed name exists?", icon="🚨")


st.header("Update a RSS feed.")

for index, feed in enumerate(st.session_state["flux_rss_url"]):

    with st.form(key=f"update_rss_feed_{index}"):
    
        feed_name = st.text_input("RSS feed name.", feed["name"])
        feed_url = st.text_input("RSS feed url.", feed["url"])
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
