import streamlit as st


def set_default_rss_feed(feed_name: str):
    st.session_state["actual_rss_feed"] = feed_name


def generate_sidebar():
    sidebar = st.sidebar

    sidebar.text("Available RSS feeds:")

    for item in st.session_state["flux_rss_url"]:
        sidebar.button(
            label=item["name"],
            key=item["name"],
            on_click=set_default_rss_feed,
            args=[item["name"]],
            use_container_width=True
        )
    return sidebar

generate_sidebar()

display_title = f"Feed RSS for: {st.session_state['actual_rss_feed']}" if st.session_state["actual_rss_feed"] else "No feed to display."
st.title(display_title)

for entry in st.session_state["flux_rss"][st.session_state["actual_rss_feed"]].entries:
    c = st.container()
    try:
        c.subheader(entry.title)
        c.write(entry.description)
        c.write(entry.published)
        c.write(entry.link)
        c.divider()
    except AttributeError:
        c.error("Your RSS feed cannot be load correctly.")
