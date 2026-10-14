import streamlit as st
from datetime import datetime

st.title("Resort Travel Experience")

# This runs on EVERY re-run — so the timestamp changes each time
st.write(f"Script ran at: **{datetime.now().strftime('%H:%M:%S')}**")

st.divider()  # Visual separator line

st.header("Vacation Planner")

# Each widget returns its current value
country_name=st.text_input("Enter your travel destination:", placeholder="Enter Country name here")
if country_name:
    st.write(f"Destination selected: {country_name}")
    
resort_name=st.text_input("Enter name of Resort:", placeholder="Enter Resort Name here")
if resort_name:
    st.write(f"Resort selected: {resort_name}")

start_date, end_date = st.date_input(
    "Select your travel dates",
    value=[datetime(2026, 10, 1), datetime(2026, 10, 7)]
)

trip_length = (end_date - start_date).days
st.metric("Trip Length", f"{trip_length} days")

number_of_travelers = st.selectbox(
    "How many travelers will be on this trip?",
    options=["1", "2", "3", "4", "5", "6"],
    index=0 # selects "1" by default
)
if number_of_travelers == "1":
    st.info("Solo travel — consider booking a smaller room.")
elif number_of_travelers in ["2", "3"]:
    st.success("Great for couples or small families!")
else:
    st.warning("Large group — check group discounts!")

    st.divider()
st.header("Budget Estimator")

flight_price = st.multiselect(
    "What is your budget for the price of your flight?",
    options=["$150-$350", "$350-$550", "$550-$750", "$750-$999", "$10,000"],
    default=["$150-$350"]
)

resort_price = st.multiselect(
    "What is your budget for the resort stay?",
    options=["$150-$350", "$350-$550", "$550-$750", "$750-$999", "$10,000"],
    default=["$150-$350"]
)

price_map = {
    "$150-$350": 250,
    "$350-$550": 450,
    "$550-$750": 650,
    "$750-$999": 875,
    "$10,000": 10000
}

if flight_price and resort_price:
    est_flight_cost = sum(price_map[p] for p in flight_price)
    est_resort_cost = sum(price_map[p] for p in resort_price)
    total_estimated_cost = est_flight_cost + est_resort_cost

    st.subheader("Estimated Trip Cost")
    st.metric("Total Estimated Cost", f"${total_estimated_cost:,}")

    cost_per_person = total_estimated_cost / int(number_of_travelers)
    st.write(f"Estimated cost per traveler: **${cost_per_person:,.2f}**")
else:
    st.warning("Select at least one option for both flight and resort budgets.")



st.divider()
st.header("Passport Information")

passport = st.radio(
    "Do you have a valid passport?",
    options=["Yes", "No"]
)
if passport == "Yes":
    st.success("Great! You will need to enter your passport details at checkout.")
else:
    st.warning("You will need a valid passport before booking this trip.")





