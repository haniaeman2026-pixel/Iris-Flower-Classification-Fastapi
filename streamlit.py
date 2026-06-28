# ==========================================================
# Iris Flower Prediction System
# Frontend: Streamlit
# Backend : FastAPI
# Developed By: Hania Eman
# ==========================================================

import streamlit as st
import requests

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Iris Flower Prediction",
    page_icon="🌸",
    layout="centered"
)

# ==========================================================
# Custom CSS
# ==========================================================

st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

.title{
    text-align:center;
    color:#1565C0;
    font-size:42px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#555555;
    font-size:18px;
    margin-bottom:30px;
}

.result{
    background:#E3F2FD;
    padding:20px;
    border-radius:10px;
    text-align:center;
    font-size:22px;
    color:#0D47A1;
    font-weight:bold;
}

.stButton>button{
    width:100%;
    height:50px;
    border-radius:10px;
    background-color:#1565C0;
    color:white;
    font-size:18px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# Header
# ==========================================================

st.markdown(
    "<div class='title'>🌸 Iris Flower Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Machine Learning | FastAPI | Streamlit</div>",
    unsafe_allow_html=True
)

# ==========================================================
# User Inputs
# ==========================================================

sepal_length = st.number_input(
    "Sepal Length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=5.1
)

sepal_width = st.number_input(
    "Sepal Width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=3.5
)

petal_length = st.number_input(
    "Petal Length (cm)",
    min_value=0.0,
    max_value=10.0,
    value=1.4
)

petal_width = st.number_input(
    "Petal Width (cm)",
    min_value=0.0,
    max_value=10.0,
    value=0.2
)

# ==========================================================
# Prediction Button
# ==========================================================

if st.button("🔍 Predict Flower"):

    api_url = "http://127.0.0.1:8000/predict"

    input_data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    try:

        response = requests.post(
            api_url,
            json=input_data,
            timeout=10
        )

        if response.status_code == 200:

            result = response.json()

            prediction = result.get("prediction", "Unknown")
            confidence = result.get("confidence", 0)

            st.success("Prediction Successful ✅")

            st.markdown(
                f"""
                <div class="result">
                    🌸 Prediction : {prediction}<br><br>
                    🎯 Confidence : {confidence}%
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.error("API returned an error.")
            st.write(response.text)

    except requests.exceptions.ConnectionError:

        st.error(
            "❌ FastAPI server is not running.\n\n"
            "Please run:\n\n"
            "uvicorn app:app --reload"
        )

    except requests.exceptions.Timeout:

        st.error("⌛ Request timed out.")

    except Exception as e:

        st.exception(e)

# ==========================================================
# Footer
# ==========================================================

st.markdown("---")

st.info("""
### Technologies Used

✅ Python

✅ Scikit-Learn

✅ FastAPI

✅ Streamlit
""")