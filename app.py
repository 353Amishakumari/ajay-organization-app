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
        # Yahan "EMAIL_PASSWORD" wahi key honi chahiye jo Render Dashboard par hai
        current_password = os.environ.get("nnndurundxsxzdke") 

        # Port 587 Render ke liye sabse best hai
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() # Secure connection start karein
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
# Form submit hone par "Processing" hamesha ke liye nahi rukega
with st.form("my_form", clear_on_submit=True):
    name = st.text_input("Full Name")
    phone = st.text_input("Mobile Number")
    choice = st.selectbox("I am interested in:", ["Land/Plot", "Construction Material", "Flat"])
    
    submit = st.form_submit_button("Book Now")

if submit:
    if name.strip() != "" and phone.strip() != "":
        # Spinner processing dikhayega, phir error ya success par ruk jayega
        with st.spinner("Processing..."):
            result = send_email(name, phone, choice)
            if result:
                st.success(f"Dhanyawad {name}! Ajay Organization aapko jald contact karegi.")
            else:
                st.error("Technical error: Connection failed. Check your App Password on Render.")
    else:
        st.warning("Please fill all details.")
