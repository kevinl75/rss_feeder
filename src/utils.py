import json

import feedparser
import streamlit as st

def add_rss_feed_to_config(rss_feed_name:str, rss_feed_url:str) -> dict:

    with open("config/rss_feeds_config.json", "r") as fd:
        feeds = json.load(fd)
    
    feeds["rss_feeds"].append({
        "name": rss_feed_name,
        "url": rss_feed_url
    })

    with open("config/rss_feeds_config.json", "w") as fd:
        json.dump(feeds, fd)

    return feeds["rss_feeds"]


def load_rss_feeds_from_config() -> dict:

    with open("config/rss_feeds_config.json", "r") as fd:
        return json.load(fd)["rss_feeds"]


def update_rss_feeds(
        old_feed_name: str,
        old_feed_url: str,
        new_feed_name: str,
        new_url_name: str
    ) -> bool:

    feeds = {}

    with open("config/rss_feeds_config.json", "r") as fd:
        feeds = json.load(fd)
    
    for feed in feeds["rss_feeds"]:
        if feed["name"] == old_feed_name and feed["url"] == old_feed_url:
            feed["name"] = new_feed_name
            feed["url"] = new_url_name
            break
    
    with open("config/rss_feeds_config.json", "w") as fd:
        json.dump(feeds, fd)
    
    return True


def remove_rss_feeds(feed_name: str, feed_url: str ) -> None:

    feeds = {}

    with open("config/rss_feeds_config.json", "r") as fd:
        feeds = json.load(fd)
    
    feeds["rss_feeds"].remove({
        "name": feed_name,
        "url": feed_url
    })
    
    with open("config/rss_feeds_config.json", "w") as fd:
        json.dump(feeds, fd)

    load_feeds_config()
    load_feeds()
    if st.session_state["actual_rss_feed"] == feed_name:
        if len(st.session_state["flux_rss_url"]) > 0:
            st.session_state["actual_rss_feed"] = st.session_state["flux_rss_url"][0]["name"]


def load_feeds_config():
    st.session_state["flux_rss_url"] = load_rss_feeds_from_config()

def load_feeds():
    st.session_state["flux_rss"] = {}
    for item in st.session_state["flux_rss_url"]:
        st.session_state["flux_rss"][item["name"]] = feedparser.parse(item["url"])
    st.session_state["feeds_to_update"] = False