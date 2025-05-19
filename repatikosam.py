import streamlit as st
import google.generativeai as genai

# Gemini API setup
genai.configure(api_key="AIzaSyDckLeyS8164U5X1Z_75e7-Ie__pTPjTcI")
model = genai.GenerativeModel('models/gemini-2.0-flash')

# Set up chatbot
def initialize_chat():
    if 'chat' not in st.session_state:
        st.session_state.chat = model.start_chat(history=[])
        st.session_state.chat.send_message(medical_context)
    if 'messages' not in st.session_state:
        st.session_state.messages = []

# Medical Context
medical_context = """
You are a medical chatbot for a hospital. Respond in simple, empathetic language.
Avoid diagnoses, suggest specialist consultations, and stay friendly.
"""

# Chatbot interface
def medical_chatbot():
    st.header("🤖 Medical Assistant Chatbot")
    initialize_chat()

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask your health-related question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Replying..."):
                response = st.session_state.chat.send_message(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})

# Mock appointment form
def book_appointment():
    st.header("📅 Book an Appointment")
    name = st.text_input("Patient Name")
    dept = st.selectbox("Department", ["Cardiology", "Neurology", "Orthopedics", "General"])
    date = st.date_input("Preferred Date")
    time = st.time_input("Preferred Time")
    if st.button("Book Now"):
        st.success(f"Appointment booked with {dept} on {date} at {time} for {name}")

# Doctor recommendation
def recommend_doctor():
    st.header("🧑‍⚕️ Doctor Recommendation")
    symptoms = st.text_area("Describe your symptoms")
    if st.button("Find Specialist"):
        prompt = f"I have these symptoms: {symptoms}. Which specialist should I consult?"
        response = model.generate_content(prompt)
        st.success(response.text)

# Mock report download
def report_portal():
    st.header("📄 Medical Report Portal")
    st.text_input("Enter Patient ID")
    if st.button("Download Latest Report"):
        st.info("Downloading mock report...")

# Medicine info/reminder
def medicine_helper():
    st.header("💊 Medicine Info & Reminder")
    med_name = st.text_input("Enter Medicine Name")
    if st.button("Get Info"):
        prompt = f"Tell me how to use {med_name}, its side effects and when to take it."
        response = model.generate_content(prompt)
        st.write(response.text)
    st.checkbox("Remind me daily", value=False)

# Simple hospital map
def hospital_map():
    st.header("🗺️ Hospital Navigation")
    st.info("Example: 'Cardiology is on Floor 2, Room 204' (mock directions)")

# Staff dashboard
def staff_dashboard():
    st.header("🏥 Staff Dashboard")
    st.subheader("Bed Availability")
    st.write("ICU: 2 beds available\nGeneral Ward: 10 beds available")
    st.subheader("Quick Patient Lookup")
    pid = st.text_input("Enter Patient ID to fetch info")
    if pid:
        st.info(f"Showing mock details for patient ID: {pid}")

# Inventory alerts
def inventory_alerts():
    st.header("📦 Inventory Alerts")
    st.warning("Paracetamol stock low!")
    st.success("Gloves restocked today.")

# Daily summary
def daily_summary():
    st.header("📊 Daily Hospital Summary")
    st.info("Today: 73 Appointments, 18 Discharges, 2 Emergency Cases")

# Symptom checker
def symptom_checker():
    st.header("🩺 Symptom Checker")
    symptoms = st.text_area("List your symptoms")
    if st.button("Check"):
        prompt = f"What might be the issue with symptoms: {symptoms}? Give a general idea."
        response = model.generate_content(prompt)
        st.write(response.text)

# Multilingual support
def multilingual_bot():
    st.header("🌐 Multilingual Support")
    lang = st.selectbox("Select Language", ["English", "Telugu", "Hindi", "Tamil"])
    query = st.text_input("Ask a question")
    if st.button("Translate and Answer"):
        prompt = f"Translate this to {lang} and answer: {query}"
        response = model.generate_content(prompt)
        st.write(response.text)

# AI health tips
def ai_health_tips():
    st.header("🧠 AI-Powered Health Tips")
    age = st.slider("Your Age", 0, 100, 25)
    health_focus = st.selectbox("Health Goal", ["General Wellness", "Heart Health", "Diabetes Prevention"])
    if st.button("Give Me Tips"):
        prompt = f"Give health tips for a {age}-year-old focused on {health_focus}"
        response = model.generate_content(prompt)
        st.write(response.text)

# Emergency help
def emergency_help():
    st.header("🚨 Emergency Help")
    if st.button("Call for Assistance"):
        st.error("Alert sent to hospital staff (mock)")

# Notifications
def notifications_center():
    st.header("📢 Notifications")
    st.info("🩹 Free Vaccination Camp on April 20\n🧪 Health Checkup Camp – Book Now!")

# Main tabs
def main():
    st.set_page_config(page_title="🏥 Hospital Management Chatbot", layout="wide")
    tab_names = [
        "Medical Chat", "Appointment", "Doctor Suggestion", "Reports",
        "Medicine", "Map", "Staff", "Inventory", "Summary",
        "Symptom Check", "Multilingual", "Health Tips", "Emergency", "Notifications"
    ]
    tabs = st.tabs(tab_names)

    with tabs[0]: medical_chatbot()
    with tabs[1]: book_appointment()
    with tabs[2]: recommend_doctor()
    with tabs[3]: report_portal()
    with tabs[4]: medicine_helper()
    with tabs[5]: hospital_map()
    with tabs[6]: staff_dashboard()
    with tabs[7]: inventory_alerts()
    with tabs[8]: daily_summary()
    with tabs[9]: symptom_checker()
    with tabs[10]: multilingual_bot()
    with tabs[11]: ai_health_tips()
    with tabs[12]: emergency_help()
    with tabs[13]: notifications_center()

if __name__ == "__main__":
    main()
