import streamlit as st

st.set_page_config(page_title="Anemia Detection", layout="centered")

st.markdown("<h1 style='text-align:center; color:#c62828;'>🩸 Anemia Detection Tool</h1>", unsafe_allow_html=True)

with st.form("anemia_form"):
    st.subheader("📝 Enter Your Health Data")

    gender = st.selectbox("Gender", ["M", "F"])
    age = st.number_input("Age", 1, 120, 30)
    blood_group = st.selectbox("Blood Group", ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"])
    red_pixel = st.number_input("Red Pixel (%)", 0.0, 100.0, 30.0)
    green_pixel = st.number_input("Green Pixel (%)", 0.0, 100.0, 30.0)
    blue_pixel = st.number_input("Blue Pixel (%)", 0.0, 100.0, 30.0)
    hb = st.number_input("Hemoglobin (Hb) Level (g/dL)", 0.0, 20.0, 11.5)

    # Centered and styled submit button
    submitted = st.form_submit_button(
        "🔍 Predict Anemia",
        use_container_width=True
    )

if submitted:
    pixel_avg = (red_pixel + green_pixel + blue_pixel) / 3
    hb_score = 70 if hb < 12 else 30
    pixel_score = 60 if pixel_avg < 50 else 40
    final_score = (hb_score * 0.6) + (pixel_score * 0.4)

    st.markdown("---")
    st.markdown("### 📋 Input Summary")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Age:** {age}")
    st.write(f"**Blood Group:** {blood_group}")
    st.write(f"**Red Pixel:** {red_pixel}%")
    st.write(f"**Green Pixel:** {green_pixel}%")
    st.write(f"**Blue Pixel:** {blue_pixel}%")
    st.write(f"**Hemoglobin:** {hb} g/dL")

    st.markdown("---")
    st.markdown(f"""
        <h3 style='text-align:center; font-size:28px;'>
            🧠 Predicted Likelihood of Anemia:
            <span style='color:#b71c1c;'>{final_score:.2f}%</span>
        </h3>
    """, unsafe_allow_html=True)

    if final_score > 50:
        st.markdown("""
            <h2 style='text-align:center; color:red; font-weight: bold;'>
                ⚠️ You may be suffering from Anemia!
            </h2>
        """, unsafe_allow_html=True)

        # Streamlit native button styled as page link
        st.page_link("pages/Precautions.py", label="🩺 View Precautions", icon="⚕️", use_container_width=True)

    else:
        st.markdown("""
            <h2 style='text-align:center; color:green; font-weight: bold;'>
                ✅ You're not showing signs of anemia.
            </h2>
        """, unsafe_allow_html=True)
