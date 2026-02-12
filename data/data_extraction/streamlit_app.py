import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import json
import os

# ---------------- PAGE CONFIG (MUST BE FIRST) ----------------
st.set_page_config(layout="wide")
st.title("📊 PHONEPE DATA VISUALIZATION AND EXPLORATION")

# ---------------- BASE DIR ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    parent_dir = os.path.dirname(BASE_DIR)  # goes to DATA/

    transaction_df = pd.read_csv(os.path.join(parent_dir, "transaction_data.csv"))
    user_df = pd.read_csv(os.path.join(parent_dir, "user_data.csv"))
    insurance_df = pd.read_csv(os.path.join(parent_dir, "insurance_data.csv"))

    return transaction_df, user_df, insurance_df


transaction_df, user_df, insurance_df = load_data()

# ---------------- LOAD GEOJSON ----------------
with open(os.path.join(BASE_DIR, "geo", "india_states.geojson"), "r", encoding="utf-8") as f:
    india_geojson = json.load(f)

for feature in india_geojson["features"]:
    feature["properties"]["state"] = feature["properties"]["NAME_1"].title()

# ---------------- SIDEBAR ----------------
with st.sidebar:
    select = option_menu(
        "Main Menu",
        ["HOME", "DATA EXPLORATION", "TOP CHARTS"],
        icons=["house", "bar-chart", "trophy"]
    )

# ---------------- HOME ----------------
if select == "HOME":
    st.subheader("Welcome 👋")
    st.write("Explore PhonePe Transactions, Users and Insurance data.")

# ---------------- DATA EXPLORATION ----------------
elif select == "DATA EXPLORATION":

    tab1, tab2, tab3 = st.tabs(
        ["📈 Aggregated Analysis", "🗺️ Map Analysis", "🏆 Top Analysis"]
    )

    # ---------- TAB 1 ----------
    with tab1:
        method = st.radio(
            "Select the Method",
            ["Insurance Analysis", "Transaction Analysis", "User Analysis"],
            key="agg_method"
        )

        if method == "Insurance Analysis":
            year = st.selectbox(
                "Select Year",
                sorted(insurance_df["year"].unique()),
                key="ins_year"
            )

            grouped = (
                insurance_df[insurance_df["year"] == year]
                .groupby("state")[["insurance_amount"]]
                .sum()
                .reset_index()
            )

            fig = px.bar(
                grouped.sort_values("insurance_amount", ascending=False).head(10),
                x="state",
                y="insurance_amount",
                title="Top 10 States by Insurance Amount"
            )
            st.plotly_chart(fig, use_container_width=True)

        elif method == "Transaction Analysis":
            year = st.selectbox(
                "Select Year",
                sorted(transaction_df["year"].unique()),
                key="txn_year"
            )

            grouped = (
                transaction_df[transaction_df["year"] == year]
                .groupby("transaction_type")[["transaction_amount"]]
                .sum()
                .reset_index()
            )

            fig = px.pie(
                grouped,
                names="transaction_type",
                values="transaction_amount",
                title="Transaction Amount Distribution"
            )
            st.plotly_chart(fig, use_container_width=True)

        elif method == "User Analysis":
            year = st.selectbox(
                "Select Year",
                sorted(user_df["year"].unique()),
                key="user_year"
            )

            grouped = (
                user_df[user_df["year"] == year]
                .groupby("state")[["registered_users"]]
                .sum()
                .reset_index()
            )

            fig = px.bar(
                grouped.sort_values("registered_users", ascending=False).head(10),
                x="state",
                y="registered_users",
                title="Top 10 States by Registered Users"
            )
            st.plotly_chart(fig, use_container_width=True)

    # ---------- TAB 2 ----------
    # ---------- TAB 2 ----------
    with tab2:
        method_2 = st.radio(
        "Select the Method",
        ["Map Insurance", "Map Transaction", "Map User"],
        key="map_method"
        )

    # -------- Map Insurance --------
        if method_2 == "Map Insurance":

            year = st.selectbox(
                "Select Year",
                sorted(insurance_df["year"].unique()),
                key="map_ins_year"
            )

            grouped = (
                insurance_df[insurance_df["year"] == year]
                .groupby("state")[["insurance_amount"]]
                .sum()
                .reset_index()
            )

            fig = px.choropleth(
                grouped,
                geojson=india_geojson,
                featureidkey="properties.state",
                locations="state",
                color="insurance_amount",
                color_continuous_scale="Blues",
                title="State-wise Insurance Amount"
            )

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig, use_container_width=True)


    # -------- Map Transaction --------
        elif method_2 == "Map Transaction":

                year = st.selectbox(
                    "Select Year",
                    sorted(transaction_df["year"].unique()),
                    key="map_trans_year"
                )

                grouped = (
                    transaction_df[transaction_df["year"] == year]
                    .groupby("state")[["transaction_amount"]]
                    .sum()
                    .reset_index()
                )

                fig = px.choropleth(
                    grouped,
                    geojson=india_geojson,
                    featureidkey="properties.state",
                    locations="state",
                    color="transaction_amount",
                    color_continuous_scale="Blues",
                    title="State-wise Transaction Amount"
                )

                fig.update_geos(fitbounds="locations", visible=False)
                st.plotly_chart(fig, use_container_width=True)


    # -------- Map User --------
        elif method_2 == "Map User":

            year = st.selectbox(
                "Select Year",
                sorted(user_df["year"].unique()),
                key="map_user_year"
            )

            grouped = (
                user_df[user_df["year"] == year]
                .groupby("state")[["registered_users"]]
                .sum()
                .reset_index()
            )

            fig = px.choropleth(
                grouped,
                geojson=india_geojson,
                featureidkey="properties.state",
                locations="state",
                color="registered_users",
                color_continuous_scale="Blues",
                title="State-wise Registered Users"
            )

            fig.update_geos(fitbounds="locations", visible=False)
            st.plotly_chart(fig, use_container_width=True)



    # ---------- TAB 3 ----------
        # ---------- TAB 3 ----------
    with tab3:

        method_3 = st.radio(
            "Select the Method",
            ["Top Insurance", "Top Transaction", "Top User"],
            key="top_method"
        )

        # -------- Top Insurance --------
        if method_3 == "Top Insurance":

            year = st.selectbox(
                "Select Year",
                sorted(insurance_df["year"].unique()),
                key="top_ins_year_tab3"
            )

            grouped = (
                insurance_df[insurance_df["year"] == year]
                .groupby("state")[["insurance_amount"]]
                .sum()
                .sort_values("insurance_amount", ascending=False)
                .head(10)
                .reset_index()
            )

            fig = px.bar(
                grouped,
                x="insurance_amount",
                y="state",
                orientation="h",
                title=f"Top 10 States by Insurance Amount ({year})"
            )

            fig.update_layout(yaxis={'categoryorder': 'total ascending'})
            st.plotly_chart(fig, use_container_width=True)

        # -------- Top Transaction --------
        elif method_3 == "Top Transaction":

            year = st.selectbox(
                "Select Year",
                sorted(transaction_df["year"].unique()),
                key="top_txn_year_tab3"
            )

            grouped = (
                transaction_df[transaction_df["year"] == year]
                .groupby("state")[["transaction_amount"]]
                .sum()
                .sort_values("transaction_amount", ascending=False)
                .head(10)
                .reset_index()
            )

            fig = px.treemap(
                grouped,
                path=["state"],
                values="transaction_amount",
                title=f"Top 10 States by Transaction Amount ({year})"
            )

            st.plotly_chart(fig, use_container_width=True)

        # -------- Top User --------
        elif method_3 == "Top User":

            year = st.selectbox(
                "Select Year",
                sorted(user_df["year"].unique()),
                key="top_user_year_tab3"
            )

            grouped = (
                user_df[user_df["year"] == year]
                .groupby("state")[["registered_users"]]
                .sum()
                .sort_values("registered_users", ascending=False)
                .head(10)
                .reset_index()
            )

            fig = px.pie(
                grouped,
                names="state",
                values="registered_users",
                hole=0.5,
                title=f"Top 10 States by Registered Users ({year})"
            )

            st.plotly_chart(fig, use_container_width=True)

    # ---------------- TOP CHARTS ----------------
elif select == "TOP CHARTS":

    st.subheader("🏆 Top Charts Analysis")

    chart_type = st.radio(
        "Select Chart Type",
        ["Top Transaction States", "Top User States", "Top Insurance States"]
    )

    # ---------------- TRANSACTION ----------------
    if chart_type == "Top Transaction States":

        year = st.selectbox(
            "Select Year",
            sorted(transaction_df["year"].unique())
        )

        grouped = (
            transaction_df[transaction_df["year"] == year]
            .groupby("state")[["transaction_amount"]]
            .sum()
            .sort_values("transaction_amount", ascending=False)
            .head(10)
            .reset_index()
        )

        fig = px.treemap(
            grouped,
            path=["state"],
            values="transaction_amount",
            title=f"Top 10 States by Transaction Amount ({year})"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ---------------- USERS ----------------
    elif chart_type == "Top User States":

        year = st.selectbox(
            "Select Year",
            sorted(user_df["year"].unique())
        )

        grouped = (
            user_df[user_df["year"] == year]
            .groupby("state")[["registered_users"]]
            .sum()
            .sort_values("registered_users", ascending=False)
            .head(10)
            .reset_index()
        )

        fig = px.pie(
            grouped,
            names="state",
            values="registered_users",
            hole=0.5,
            title=f"Top 10 States by Registered Users ({year})"
        )

        st.plotly_chart(fig, use_container_width=True)

    # ---------------- INSURANCE ----------------
    elif chart_type == "Top Insurance States":

        year = st.selectbox(
            "Select Year",
            sorted(insurance_df["year"].unique())
        )

        grouped = (
            insurance_df[insurance_df["year"] == year]
            .groupby("state")[["insurance_amount"]]
            .sum()
            .sort_values("insurance_amount", ascending=False)
            .head(10)
            .reset_index()
        )

        fig = px.bar(
            grouped,
            x="insurance_amount",
            y="state",
            orientation="h",
            title=f"Top 10 States by Insurance Amount ({year})"
        )

        fig.update_layout(yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig, use_container_width=True)
