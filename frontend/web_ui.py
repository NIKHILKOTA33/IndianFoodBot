import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="IndianFoodBot", layout="centered")

st.title("IndianFoodBot")
st.caption("Local Recipe Chatbot")

st.markdown("---")

ingredients_text = st.text_input(
    "Enter ingredients (comma separated)",
    placeholder="Example: egg, onion, tomato"
)

search_btn = st.button("🔍 Find Best Recipe")

st.markdown("---")

if search_btn:
    if not ingredients_text.strip():
        st.error("Please enter at least one ingredient.")
    else:
        ingredients = [x.strip() for x in ingredients_text.split(",") if x.strip()]

        with st.spinner("IndianFoodBot is thinking..."):
            response = requests.post(API_URL, json={"ingredients": ingredients})

        if response.status_code != 200:
            st.error("Backend Error: " + response.text)
        else:
            data = response.json()

            if data["status"] == "no_match":
                st.warning("No recipe found for given ingredients.")
            else:
                best = data["best_match"]

                st.subheader("IndianFoodBot Response")
                st.success(data["chatbot_response"])

                st.markdown("---")

                st.subheader("Best Recipe Match")

                st.markdown(
                    f"""
                    <div style="padding:15px; border-radius:12px; background-color:#f0f2f6;">
                        <h3 style="margin-bottom:5px;">{best['recipe_name']}</h3>
                        <p style="margin:0;"><b>Cuisine:</b> {best['cuisine']}</p>
                        <p style="margin:0;"><b>Course:</b> {best['course']}</p>
                        <p style="margin:0;"><b>Diet:</b> {best['diet']}</p>
                        <p style="margin:0;"><b>Total Time:</b> {best['total_time_mins']} mins</p>
                        <p style="margin:0;"><b>Similarity Score:</b> {best['similarity_score']}%</p>
                        <p style="margin:0;"><b>URL:</b> <a href="{best['url']}" target="_blank">{best['url']}</a></p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown("---")

                st.subheader("Ingredients (From Dataset)")
                st.info(best["ingredients_text"])

                st.subheader("Instructions (From Dataset)")
                st.write(best["instructions"])
