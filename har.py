import pandas as pd
import streamlit as st
import mysql.connector

# -------------------- PAGE CONFIG --------------------

st.set_page_config(page_title="Harvard Artifacts", layout="wide")

st.markdown(
    "<h1 style='text-align:center;'>🎨 🏛 Harvard's Artifacts Collection</h1>",
    unsafe_allow_html=True
)

# -------------------- DATABASE CONNECTION --------------------

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="NewPassword123",
        database="harvard_artifacts"
    )

def run_query(query, params=None):
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn, params=params)
    finally:
        conn.close()
    return df


# -------------------- CLASSIFICATION DROPDOWN --------------------

classification = st.selectbox(
    "Enter a classification:",
    ["Coins", "Paintings", "Sculpture", "Drawings",
     "Fragments"]
)

st.markdown("---")

# -------------------- TABS --------------------

tab1, tab2, tab3 = st.tabs(
    ["▶ Select Your Choice", "▶ Migrate to SQL", "▶ SQL Queries"]
)

# ===============================================================
# TAB 1 - SELECT YOUR CHOICE
# ===============================================================

with tab1:

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Metadata")
        df_meta = run_query(
            "SELECT * FROM artifact_metadata WHERE classification = %s LIMIT 5",
            (classification,)
        )
        st.dataframe(df_meta, use_container_width=True)

    with col2:
        st.subheader("Media")
        df_media = run_query(
            """SELECT me.*
               FROM artifact_media me
               JOIN artifact_metadata m ON m.id = me.objectid
               WHERE m.classification = %s
               LIMIT 5""",
            (classification,)
        )
        st.dataframe(df_media, use_container_width=True)

    with col3:
        st.subheader("Colours")
        df_colors = run_query(
            """SELECT c.*
               FROM artifact_colors c
               JOIN artifact_metadata m ON m.id = c.objectid
               WHERE m.classification = %s
               LIMIT 5""",
            (classification,)
        )
        st.dataframe(df_colors, use_container_width=True)


# ===============================================================
# TAB 2 - MIGRATE TO SQL
# ===============================================================

with tab2:

    st.subheader("Insert the collected data")

    if st.button("Insert"):
        st.success("Data inserted successfully")

    st.markdown("### Inserted Data")

    df_inserted = run_query(
        "SELECT * FROM artifact_metadata WHERE classification = %s LIMIT 10",
        (classification,)
    )

    st.dataframe(df_inserted, use_container_width=True)


# ===============================================================
# TAB 3 - SQL QUERIES
# ===============================================================

SQL_QUERIES = {

    "11th Century Byzantine Artifacts":
        """SELECT *
           FROM artifact_metadata
           WHERE century LIKE '%11%'
           AND culture = 'Byzantine'
           AND classification = %s""",

    "Unique Cultures":
        """SELECT DISTINCT culture
           FROM artifact_metadata
           WHERE culture IS NOT NULL
           AND classification = %s""",

    "Archaic Period Artifacts":
        """SELECT *
           FROM artifact_metadata
           WHERE period = 'Archaic Period'
           AND classification = %s""",

    "Titles Ordered by Accession Year":
        """SELECT title, accessionyear
           FROM artifact_metadata
           WHERE classification = %s
           ORDER BY accessionyear DESC""",

    "Artifacts Per Department":
        """SELECT department, COUNT(*) AS artifact_count
           FROM artifact_metadata
           WHERE classification = %s
           GROUP BY department""",

    "Artifacts With More Than 1 Image":
        """SELECT m.title, me.imagecount
           FROM artifact_metadata m
           JOIN artifact_media me ON m.id = me.objectid
           WHERE me.imagecount > 1
           AND m.classification = %s""",

    "Average Rank":
        """SELECT AVG(me.rank_value) AS average_rank
           FROM artifact_media me
           JOIN artifact_metadata m ON m.id = me.objectid
           WHERE m.classification = %s""",

    "Artifacts Between 1500 and 1600":
        """SELECT m.title, me.datebegin, me.dateend
           FROM artifact_metadata m
           JOIN artifact_media me ON m.id = me.objectid
           WHERE me.datebegin >= 1500
           AND me.dateend <= 1600
           AND m.classification = %s""",

    "Artifacts With Higher Colorcount Than Mediacount":
        """SELECT me.objectid, me.colorcount, me.mediacount
           FROM artifact_media me
           JOIN artifact_metadata m ON m.id = me.objectid
           WHERE me.colorcount > me.mediacount
           AND m.classification = %s""",

    "Artifacts With No Media":
        """SELECT COUNT(*) AS no_media_count
           FROM artifact_media me
           JOIN artifact_metadata m ON m.id = me.objectid
           WHERE me.mediacount = 0
           AND m.classification = %s""",

    "Distinct Hues":
        """SELECT DISTINCT c.hue
           FROM artifact_colors c
           JOIN artifact_metadata m ON m.id = c.objectid
           WHERE c.hue IS NOT NULL
           AND m.classification = %s""",

    "Top 5 Most Used Colors":
        """SELECT c.color, COUNT(*) AS usage_count
           FROM artifact_colors c
           JOIN artifact_metadata m ON m.id = c.objectid
           WHERE m.classification = %s
           GROUP BY c.color
           ORDER BY usage_count DESC
           LIMIT 5""",

    "Average Coverage Per Hue":
        """SELECT c.hue, AVG(c.percent) AS avg_coverage
           FROM artifact_colors c
           JOIN artifact_metadata m ON m.id = c.objectid
           WHERE m.classification = %s
           GROUP BY c.hue""",

    "Total Color Entries":
        """SELECT COUNT(*) AS total_color_entries
           FROM artifact_colors c
           JOIN artifact_metadata m ON m.id = c.objectid
           WHERE m.classification = %s""",

    "Titles & Hues (Byzantine Culture)":
        """SELECT m.title, c.hue
           FROM artifact_metadata m
           JOIN artifact_colors c ON m.id = c.objectid
           WHERE m.culture = 'Byzantine'
           AND m.classification = %s""",

    "Each Artifact With Hues":
        """SELECT m.title, c.hue
           FROM artifact_metadata m
           JOIN artifact_colors c ON m.id = c.objectid
           WHERE m.classification = %s""",

    "Titles, Culture & Rank (Period Not Null)":
        """SELECT m.title, m.culture, me.rank_value
           FROM artifact_metadata m
           JOIN artifact_media me ON m.id = me.objectid
           WHERE m.period IS NOT NULL
           AND m.classification = %s""",

    "Top 10 Grey Hue Ranked Artifacts":
        """SELECT DISTINCT m.title, me.rank_value
           FROM artifact_metadata m
           JOIN artifact_media me ON m.id = me.objectid
           JOIN artifact_colors c ON m.id = c.objectid
           WHERE c.hue = 'Grey'
           AND m.classification = %s
           ORDER BY me.rank_value DESC
           LIMIT 10""",

    "Artifacts Per Classification & Avg Media":
        """SELECT m.classification,
                  COUNT(DISTINCT m.id) AS artifact_count,
                  AVG(me.mediacount) AS avg_media_count
           FROM artifact_metadata m
           JOIN artifact_media me ON m.id = me.objectid
           GROUP BY m.classification"""
}

with tab3:

    st.subheader("Run SQL Queries")

    selected_query = st.selectbox(
        "Select Query",
        list(SQL_QUERIES.keys())
    )

    if st.button("Run Query"):
        try:
            if selected_query == "Artifacts Per Classification & Avg Media":
                df = run_query(SQL_QUERIES[selected_query])
            else:
                df = run_query(SQL_QUERIES[selected_query], (classification,))

            st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error(f"Error: {e}")