import streamlit as st
import smtplib
import os  # <-- Ye line add karein
from email.mime.text import MIMEText

# --- CONFIGURATION ---
MY_EMAIL = "25167005@kiit.ac.in"
# Niche wali line ko dhyan se copy karein:
APP_PASSWORD = os.getenv("hieklioljhfizjmc") # Spaces ke bina likhein

def send_email(name, phone, interest):
    msg = MIMEText(f"Naya Customer Inquiry!\n\nNaam: {name}\nPhone: {phone}\nInterest: {interest}")
    msg['Subject'] = f"New Lead: {name} (Ajay Organization)"
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(MY_EMAIL, APP_PASSWORD)
            server.send_message(msg)
        return True
    except:
        return False

# --- UI ---
st.set_page_config(page_title="Ajay Organization", page_icon="🏢")
st.title("🏢 Ajay Organization")
st.markdown("### Real Estate & Construction Materials")

st.info("Quality materials aur best properties ke liye humse judein.")

# Inventory Display
col1, col2 = st.columns(2)
with col1:
    st.subheader("📍 Properties")
    st.write("✅ Plots in Bhubaneswar\n✅ 2/3 BHK Flats\n✅ Commercial Shops")
with col2:
    st.subheader("🏗️ Materials")
    st.write("✅ Premium Cement\n✅ TMT Steel Rods\n✅ High-quality Bricks")

st.divider()

# Inquiry Form
st.subheader("📩 Send Inquiry")
with st.form("my_form"):
    name = st.text_input("Full Name")
    phone = st.text_input("Mobile Number")
    choice = st.selectbox("I am interested in:", ["Land/Plot", "Construction Material", "Flat"])
    submit = st.form_submit_button("Book Now")
    
    if submit:
        if name and phone:
            if send_email(name, phone, choice):
                st.success(f"Dhanyawad {name}! Ajay Organization aapko jald contact karegi.")
            else:
                st.error("Kuch technical error hai. Please check credentials.")
        else:
            st.warning("Please fill all details.")
