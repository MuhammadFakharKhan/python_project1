import streamlit as st

# Custom CSS
st.markdown("""
    <style>
    .stButton>button { 
        color: black; 
        border: none; 
        padding: 10px 20px; 
        font-size: 16px;
        background-color: white; 
    }
    .stButton>button:hover { 
        background-color: black; 
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Unit Converter")
st.write("Convert between different units easily!")

# Conversion factors (to base unit for each category)
conversion_factors = {
    "Length": {
        "meter": 1,
        "kilometer": 1000,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "centimeter": 0.01,
        "inch": 0.0254,
        "millimeter": 0.001
    },
    "Weight": {
        "kilogram": 1,
        "pound": 0.453592,
        "ounce": 0.0283495,
        "gram": 0.001,
        "milligram": 0.000001
    },
    "Volume": {
        "liter": 1,
        "cubic_meter": 1000,
        "gallon": 3.78541,
        "quart": 0.946353,
        "pint": 0.473176,
        "milliliter": 0.001
    }
}

# Unit categories and their units
unit_categories = {
    "Length": ["kilometer", "mile", "meter", "yard", "foot", "centimeter", "inch", "millimeter"],
    "Weight": ["kilogram", "pound", "ounce", "gram", "milligram"],
    "Temperature": ["kelvin", "celsius", "fahrenheit"],
    "Volume": ["cubic_meter", "gallon", "quart", "liter", "pint", "milliliter"],
}

# Select category
category = st.selectbox("Select Category", list(unit_categories.keys()))

# Select units
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", unit_categories[category])
with col2:
    to_unit = st.selectbox("To", unit_categories[category])

# Input value
value = st.number_input("Enter value", min_value=0.0, value=1.0, step=0.1)

def convert_units(value, from_unit, to_unit, category):
    try:
        # Special handling for temperature
        if category == "Temperature":
            if from_unit == "celsius":
                if to_unit == "fahrenheit":
                    return value * 9/5 + 32
                elif to_unit == "kelvin":
                    return value + 273.15
                else:
                    return value
            elif from_unit == "fahrenheit":
                if to_unit == "celsius":
                    return (value - 32) * 5/9
                elif to_unit == "kelvin":
                    return (value - 32) * 5/9 + 273.15
                else:
                    return value
            else:  # kelvin
                if to_unit == "celsius":
                    return value - 273.15
                elif to_unit == "fahrenheit":
                    return (value - 273.15) * 9/5 + 32
                else:
                    return value
        
        # For other categories
        if from_unit == to_unit:
            return value
        
        # Convert to base unit first
        base_value = value * conversion_factors[category][from_unit]
        # Convert from base unit to target unit
        result = base_value / conversion_factors[category][to_unit]
        return result
        
    except Exception as e:
        return f"Error: {str(e)}"

# Perform conversion
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    if isinstance(result, str):
        st.error(result)
    else:
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")