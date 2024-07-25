import streamlit as st

# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
    "India": {
        # "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        # "Diet": 1.25,  # kgCO2/meal, 2.5kgco2/kg
        # "Waste": 0.1,  # kgCO2/kg
        "diesel":0.32,  #kgCO2/litre
        # "groundWater" : 265.39, #kgCO2/ha
        "Nitrogen(N)": 4.00, #kg CO2/kg product
        "Phosphate (P2O5)": 1.29 ,         #kg CO2/kg product
        # "Potash (K2O)": 1.47        #kg CO2/kg product


    }
}

# # Set wide layout and page name
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")

# # Streamlit app code
st.title("Personal Carbon Calculator App ⚠️")

# # User inputs
st.subheader("🌍 Your Country")
country = st.selectbox("Select", ["India"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚜 Monthly diesel used (in litre)")
    Diesel = st.slider("Diesel", 0.0, 100.0, key="diesel_input")

    st.subheader("💡 Monthly electricity consumption (in kWh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

with col2:
    st.subheader("🌱 Nitrogen(N) used per month (in kg)")
    Nitrogen = st.slider("Nitrogen(N)", 0.0, 100.0, key="Nitrogen(N)_input")

    st.subheader("🌱 Phosphate (P2O5) used per month (in kg)")
    Phosphate = st.slider("Phosphate (P2O5)", 0.0, 100.0,key="Phosphate(P2O5)_input")



# # Normalize inputs
if Diesel > 0:
    Diesel = Diesel * 12  # Convert monthly distance to yearly
if electricity > 0:
    electricity = electricity * 12  # Convert monthly electricity to yearly
if Nitrogen > 0:
    Nitrogen = Nitrogen * 12  # Convert monthly meals to yearly
if Phosphate > 0:
    Phosphate = Phosphate * 12  # Convert monthly waste to yearly

# # Calculate carbon emissions
diesel_emissions = EMISSION_FACTORS[country]["diesel"] * Diesel
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
Nitrogen_emissions = EMISSION_FACTORS[country]["Nitrogen(N)"] * Nitrogen
Phosphate_emissions = EMISSION_FACTORS[country]["Phosphate (P2O5)"] * Phosphate

# # Convert emissions to tonnes and round off to 2 decimal points
diesel_emissions = round(diesel_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
Nitrogen_emissions = round(Nitrogen_emissions / 1000, 2)
Phosphate_emissions = round(Phosphate_emissions / 1000, 2)

# # Calculate total emissions
total_emissions = round(
    diesel_emissions + electricity_emissions + Nitrogen_emissions + Phosphate_emissions, 2
)

if st.button("Calculate CO2 Emissions"):

#     # Display results
    st.header("Results")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"🚜 Diesel: {diesel_emissions} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
        st.info(f"🌱 Nitrogen(N): {Nitrogen_emissions} tonnes CO2 per year")
        st.info(f"🌱 Phosphate(P2O5): {Phosphate_emissions} tonnes CO2 per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
        st.warning("In 2023, CO2 emissions per capita for India was around 2 tons of CO2 per capita. Between 1972 and 2023, CO2 emissions per capita of India grew substantially from 0.39 to 1.9 tons of CO2 per capita rising at an increasing annual rate that reached a maximum of 9.41% in 2023")
