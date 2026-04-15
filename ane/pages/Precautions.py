import streamlit as st

st.set_page_config(page_title="Precautions", layout="centered")

st.markdown("<h2 style='text-align:center; color:#b71c1c;'>🩺 Precautions for Anemia</h2>", unsafe_allow_html=True)

st.markdown("## ✅ What You Should Do:")
st.markdown("""
<div style='background-color:#e8f5e9; padding:15px; border-radius:10px;'>
<ul>
<li>Eat <b>iron-rich foods</b> like spinach, eggs, lentils</li>
<li>Include <b>Vitamin C</b> in your meals</li>
<li>Use <b>cast iron cookware</b></li>
<li>Stay <b>hydrated</b> throughout the day</li>
<li>Get <b>adequate sleep</b> and manage stress</li>
<li>Take <b>iron supplements</b> if prescribed</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("## 🚫 What You Should Avoid:")
st.markdown("""
<div style='background-color:#ffebee; padding:15px; border-radius:10px;'>
<ul>
<li>Avoid <b>skipping meals</b></li>
<li>Don't drink <b>tea/coffee</b> right after meals</li>
<li>No <b>self-medication</b> with iron</li>
<li>Avoid <b>alcohol & smoking</b></li>
<li>Don’t <b>ignore symptoms</b> like fatigue/dizziness</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center;'>
    <a href='../app.py'>
        <button style='margin-top:30px; padding:10px 25px; background-color:#1976d2; color:white; font-size:16px; border:none; border-radius:8px;'>
            ⬅️ Back to Home
        </button>
    </a>
</div>
""", unsafe_allow_html=True)
