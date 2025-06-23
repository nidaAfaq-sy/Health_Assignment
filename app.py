import streamlit as st

# Page configuration
st.set_page_config(page_title="Health Assignment", layout="centered")

st.title("🏥 Health Assignment App")
st.write("Apni sehat ki maloomat daalein aur apna BMI jaanen!")

# User Inputs
name = st.text_input("Apna naam likhein:")
age = st.number_input("Umar (saalon mein):", min_value=1, max_value=120, value=20)
height = st.number_input("Qad (meters mein):", min_value=0.5, max_value=2.5, value=1.7, step=0.01)
weight = st.number_input("Wazan (kg mein):", min_value=10.0, max_value=300.0, value=70.0, step=0.1)

if st.button("BMI Calculate karein"):
    if height > 0:
        bmi = weight / (height ** 2)
        st.success(f"{name}, aap ka BMI hai: {bmi:.2f}")

        # Health advice
        if bmi < 18.5:
            st.info("Aap ka wazan kam hai. Zyada protein aur healthy cheezein khayen.")
        elif 18.5 <= bmi < 25:
            st.info("Aap ka wazan bilkul theek hai. Isi tarah sehatmand lifestyle jari rakhein!")
        elif 25 <= bmi < 30:
            st.info("Aap ka wazan kuch zyada hai. Exercise aur healthy diet par tawajjo dein.")
        else:
            st.info("Aap ka wazan kafi zyada hai. Doctor se mashwara karein aur diet/exercise par amal karein.")
    else:
        st.error("Qad sahi tareeqay se daalein.")

st.write("---")
st.write("**Sehatmand Zindagi ke Tips:**")
st.markdown("""
- Rozana kuch der walk ya exercise karein.
- Zyada pani piyen.
- Sabziyan aur phal apni diet mein shamil karein.
- Junk food aur cold drinks se parhez karein.
- Apni neend puri karein.
""")
