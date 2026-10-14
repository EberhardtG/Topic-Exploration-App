
# 📘 **README — Resort Travel Experience (Streamlit App)**

## 🌴 Overview
**Resort Travel Experience** is an interactive Streamlit application that helps users plan a vacation by selecting a destination, resort, travel dates, number of travelers, budget ranges, and passport status. The app uses multiple Streamlit widgets, dynamic conditional logic, and real-time calculations to provide an estimated trip cost and helpful travel guidance.

This project demonstrates core Streamlit concepts:
- Widgets that collect user input  
- Conditional logic that changes content dynamically  
- Calculations based on widget values  
- Display elements such as metrics, warnings, and success messages  

---

## 🚀 Features

### **1. Destination & Resort Selection**
Users enter:
- Travel destination  
- Resort name  

The app immediately displays their selections.

---

### **2. Travel Date Range**
A date range selector allows users to choose:
- Start date  
- End date  

The app calculates and displays:
- **Trip Length (in days)** using `st.metric()`

---

### **3. Traveler Count**
A selectbox lets users choose how many people are traveling.  
Dynamic messages appear based on the selection:
- Solo travel → info message  
- Small group → success message  
- Large group → warning message  

---

### **4. Budget Estimator**
Users select budget ranges for:
- Flight  
- Resort stay  

The app:
- Converts ranges into estimated numeric values  
- Calculates total estimated trip cost  
- Calculates cost per traveler  
- Displays results using `st.metric()` and formatted text  
- Shows a warning if either budget category is missing  

---

### **5. Passport Status**
A radio button asks whether the user has a valid passport.  
The app displays:
- A success message if “Yes”  
- A warning message if “No”  

---

## 🧮 Calculations Included
- Trip length:  
  ```python
  trip_length = (end_date - start_date).days
  ```
- Estimated flight cost  
- Estimated resort cost  
- Total estimated cost  
- Cost per traveler  

---

## 🛠️ Technologies Used
- **Python 3**
- **Streamlit**
- **Datetime module**

---

## 📦 How to Run the App

1. Install Streamlit (if not installed):
   ```
   pip install streamlit
   ```

2. Save the project file as:
   ```
   explore.py
   ```

3. Run the app:
   ```
   streamlit run explore.py
   ```

4. The app will open automatically in your browser.

---

## 📑 Project Requirements Checklist

| Requirement | Completed |
|------------|-----------|
| 5+ widget types | ✔ |
| Conditional logic | ✔ |
| At least one calculation | ✔ (multiple) |
| Display elements | ✔ (`st.write`, `st.info`, `st.success`, `st.warning`, `st.metric`, `st.divider`) |
| Title + headers | ✔ |
| Interactive content | ✔ |

---

## 🎯 Learning Objectives Demonstrated
- Building interactive UI with Streamlit  
- Using widget return values to drive logic  
- Creating dynamic, user‑responsive content  
- Performing calculations based on user input  
- Structuring a clean, readable Streamlit application  

---
