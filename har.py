import pandas as pd
import streamlit as st
import mysql.connector


st.set_page_config(page_title="Harvard Artifacts", layout="wide")

st.markdown(
    "<h1 style='text-align:center;'>🎨 🏛 Harvard's Artifacts Collection</h1>",
    unsafe_allow_html=True
)

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

classification = st.selectbox(
    "Select Classification",
    [
        "Coins", "Paintings", "Sculpture", "Drawings",
        "Textile Arts", "Manuscripts"
    ]
)

st.markdown("---")


if "show_queries" not in st.session_state:
    st.session_state.show_queries = False

if "show_tables" not in st.session_state:
    st.session_state.show_tables = False

col1, col2 = st.columns(2)

if col1.button("📊 SQL Queries", use_container_width=True):
    st.session_state.show_queries = True
    st.session_state.show_tables = False

if col2.button("📁 View Tables", use_container_width=True):
    st.session_state.show_tables = True
    st.session_state.show_queries = False

st.markdown("---")


SQL_QUERIES = {
    "Artifacts from 11th century (Byzantine culture)":
        "SELECT * FROM artifact_metadata WHERE century='11th century' AND culture='Byzantine'",

    "Unique cultures represented":
        "SELECT DISTINCT culture FROM artifact_metadata WHERE culture IS NOT NULL",

    "Artifacts from Archaic Period":
        "SELECT * FROM artifact_metadata WHERE period='Archaic Period'",

    "Artifacts ordered by accession year":
        "SELECT title, accessionyear FROM artifact_metadata ORDER BY accessionyear DESC",

    "Artifacts per department":
        "SELECT department, COUNT(*) AS total_artifacts FROM artifact_metadata GROUP BY department",

    "Artifacts with more than 1 image":
        "SELECT objectid, imagecount FROM artifact_media WHERE imagecount > 1",

    "Average rank of artifacts":
        "SELECT AVG(rank) AS avg_rank FROM artifact_media",

    "Artifacts created between 1500 and 1600":
        """SELECT m.title, a.datebegin, a.dateend
           FROM artifact_metadata m
           JOIN artifact_media a ON m.id = a.objectid
           WHERE a.datebegin >= 1500 AND a.dateend <= 1600""",

    "Top 5 most used colors":
        """SELECT color, COUNT(*) AS frequency
           FROM artifact_colors
           GROUP BY color
           ORDER BY frequency DESC
           LIMIT 5""",

    "Artifacts & hues (Byzantine culture)":
        """SELECT m.title, c.hue
           FROM artifact_metadata m
           JOIN artifact_colors c ON m.id = c.objectid
           WHERE m.culture = 'Byzantine'"""
}


if st.session_state.show_queries:
    st.subheader("🔍 SQL Queries")

    selected_query = st.selectbox(
        "Select Query",
        list(SQL_QUERIES.keys())
    )

    if st.button("Run Query"):
        try:
            if "%(class)s" in SQL_QUERIES[selected_query]:
                df = run_query(SQL_QUERIES[selected_query], params={"class": classification})
            else:
                df = run_query(SQL_QUERIES[selected_query])

            st.dataframe(df, use_container_width=True)

        except Exception as e:
            st.error(f"Error: {e}")

if st.session_state.show_tables:
    st.subheader("📁 Database Tables")

    table = st.selectbox(
        "Select Table",
        ["artifact_metadata", "artifact_media", "artifact_colors"]
    )

    try:
        df = run_query(f"SELECT * FROM {table} LIMIT 1000")
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"Error: {e}")

    