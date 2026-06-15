import streamlit as st
import pandas as pd
from datetime import datetime

# import your scraper functions
from youtube_scraper import (
    open_browser,
    visit_channel,
    scrape_videoes
)

st.set_page_config(
    page_title="YouTube Scraper",
    layout="wide"
)
st.title("📺 YouTube Channel Scraper")

channel = st.text_input(
    "Enter Channel URL or Name"
)

channel = channel.strip()
if st.button("Start Scraping"):

    if not channel:
        st.warning("Enter channel name first")
        st.stop()
    # If user entered only channel name
    if "youtube.com" not in channel:
        channel = f"https://www.youtube.com/@{channel}"

    # Make sure we're on Videos tab
    if not channel.endswith("/videos"):
        channel = channel.rstrip("/") + "/videos"
    

    status = st.empty()
    progress = st.progress(0)

    try:

        status.info("🚀 Opening Browser...")
        progress.progress(10)

        driver = open_browser()

        status.info("🌐 Opening Channel...")
        progress.progress(20)

        visit_channel(driver,channel)

        status.info("📜 Scrolling Videos...")
        progress.progress(40)

        df = scrape_videoes(driver)

        progress.progress(100)

        status.success(
            f"✅ Finished! {len(df)} videos scraped"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        excel_file = "youtube_data.xlsx"

        df.to_excel(
            excel_file,
            index=False
        )

        with open(excel_file, "rb") as f:

            st.download_button(
                "📥 Download Excel",
                f,
                file_name=excel_file,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    except Exception as e:

        st.error(str(e))