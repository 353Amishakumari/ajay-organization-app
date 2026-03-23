import streamlit as st
import smtplib
import os
from email.mime.text import MIMEText

# --- CONFIGURATION ---
MY_EMAIL = "ar3097058@gmail.com"

def send_email(name, phone, interest):
    msg = MIMEText(f"Naya Customer Inquiry!\n\nNaam: {name}\nPhone: {phone}\nInterest: {interest}")
    msg['Subject'] = f"New Lead: {name} (Ajay Organization)"
    msg['From'] = MY_EMAIL
    msg['To'] = MY_EMAIL

    try:
        # Render ke Environment Variable se password load karna
        current_password = os.environ.get("nnndurundxsxzdke") 

        # Port 465 aur SMTP_SSL connection ke liye sabse stable hai
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(MY_EMAIL, current_password) 
        server.sendmail(MY_EMAIL, MY_EMAIL, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"SMTP Error: {e}")
        return False

# --- UI (Website Design) ---
st.set_page_config(page_title="Ajay Organization", page_icon="🏢")
st.title("🏢 Ajay Organization")
st.markdown("### Real Estate & Construction Materials")

st.info("Quality materials aur best properties ke liye humse judein.")

# Inventory Details
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
with st.form("my_form", clear_on_submit=True):
    name = st.text_input("Full Name")
    phone = st.text_input("Mobile Number")
    choice = st.selectbox("I am interested in:", ["Land/Plot", "Construction Material", "Flat"])
    
    # Button sirf EK baar
    submit = st.form_submit_button("Book Now")

    if submit:
        # Check karein ki fields khaali toh nahi hain
        if name.strip() != "" and phone.strip() != "":
            with st.spinner("Processing..."):
                if send_email(name, phone, choice):
                    st.success(f"Dhanyawad {name}! Ajay Organization aapko jald contact karegi.")
                else:
                    st.error("Technical error: Connection failed. Check App Password.")
        else:
            st.warning("Please fill all details.")
