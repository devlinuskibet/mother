import streamlit as st
import pandas as pd
import joblib

# --- 1. Load the Model ---
# This looks for the files in the CURRENT folder (mamacare-backend)
@st.cache_resource
def load_model():
    pipeline = joblib.load('maternal_risk_pipeline.joblib')
    encoder = joblib.load('label_encoder.joblib')
    return pipeline, encoder

try:
    pipeline, label_encoder = load_model()
except FileNotFoundError:
    st.error("Error: Model files not found. Run 'python fix_model.py' first.")
    st.stop()

# --- 2. App Title ---
st.set_page_config(page_title="Maternal Health Risk Predictor", page_icon="🏥")
st.title("🏥 Maternal Health Risk Predictor")
st.markdown("### AI-Powered Prenatal Assessment")
st.info("ℹ️ Model Version: Lite (6 Clinical Features)")

# --- 3. Input Form ---
with st.form("risk_assessment_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        # Note: Variable names match the 'Lite' dataset exactly
        age = st.number_input("Age (Years)", min_value=10, max_value=70, value=25)
        systolic_bp = st.number_input("Systolic BP (mm Hg)", min_value=50, max_value=200, value=110)
        diastolic_bp = st.number_input("Diastolic BP (mm Hg)", min_value=30, max_value=150, value=70)
        
    with col2:
        bs = st.number_input("Blood Sugar (BS)", min_value=3.0, max_value=20.0, value=7.0, step=0.1)
        body_temp = st.number_input("Body Temperature (F)", min_value=95.0, max_value=105.0, value=98.0, step=0.1)
        heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=150, value=72)

    # Submit Button
    submit_btn = st.form_submit_button("Analyze Risk Profile", type="primary")

# --- 4. Prediction Logic ---
if submit_btn:
    # Prepare input data matching EXACTLY what fix_model.py trained on
    # Columns must be: ['Age', 'SystolicBP', 'DiastolicBP', 'BS', 'BodyTemp', 'HeartRate']
    input_data = {
        'Age': age,
        'SystolicBP': systolic_bp,   # NO SPACE in name
        'DiastolicBP': diastolic_bp, # NO SPACE in name
        'BS': bs,
        'BodyTemp': body_temp,       # NO SPACE in name
        'HeartRate': heart_rate
    }
    
    input_df = pd.DataFrame([input_data])
    
    try:
        # Predict
        prediction_idx = pipeline.predict(input_df)[0]
        risk_label = label_encoder.inverse_transform([prediction_idx])[0]
        
        # Display Results
        st.divider()
        st.subheader("Assessment Result")
        
        # Handle capitalization differences in dataset (High Risk vs high risk)
        result_text = risk_label.lower()
        
        if "high" in result_text:
            st.error(f"⚠️ **HIGH RISK DETECTED**")
            st.write("Recommendation: Immediate specialist consultation.")
        elif "mid" in result_text or "moderate" in result_text:
             st.warning(f"⚠️ **MODERATE RISK DETECTED**")
             st.write("Recommendation: Schedule follow-up checkup.")
        else:
            st.success(f"✅ **LOW RISK**")
            st.write("Recommendation: Standard care.")
            
    except Exception as e:
        st.error(f"An error occurred: {e}")