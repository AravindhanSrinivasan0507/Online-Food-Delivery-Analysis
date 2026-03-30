
import pandas as pd
import streamlit as st

df = pd.read_csv(r"C:\Users\ARAVINDHAN\Downloads\cleaned_orders.csv")


# Now you can safely use df
total_orders = len(df)
total_revenue = df['Order_Value'].sum()
aov = df['Order_Value'].mean()
avg_delivery_time = (df['Delivery_Time_Min']).mean()
cancellation_rate = (df['Order_Status'].eq("Cancelled").sum() / total_orders) * 100
avg_rating = df['Delivery_Rating'].mean()
profit_margin = ((total_revenue - df['cost'].sum()) / total_revenue) * 100

st.markdown("<h1 style='text-align: center;'>🍔 Online Food Delivery Analysis</h1>", unsafe_allow_html=True)
import streamlit as st

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://png.pngtree.com/png-clipart/20221217/original/pngtree-delivery-man-riding-motorbike-from-smart-phone-screen-deliver-png-image_8766820.png")
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)


# Display metrics
st.markdown(
    """
    <style>
    /* Style metric labels */
    [data-testid="stMetric"] [data-testid="stMetricLabel"] {
        color: darkblue !important;   /* Label text color */
        font-size: 18px !important;   /* Label font size */
        font-weight: 600 !important;  /* Label weight */
    }

    /* Style metric values */
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: darkred !important;    /* Value text color */
        font-size: 22px !important;   /* Value font size */
        font-weight: bold !important; /* Value weight */
    }
    </style>
    """,
    unsafe_allow_html=True
)





st.metric(label="Total Orders", value=total_orders )
st.metric(label="Total Revenue", value=f"₹{total_revenue:,.2f}" )
st.metric(label="Average Order Value", value=f"₹{aov:,.2f}" )
st.metric(label="Avg Delivery Time", value=f"{avg_delivery_time:.2f} mins")
st.metric(label="Cancellation Rate", value=f"{cancellation_rate:.2f}%" )
st.metric(label="Avg Delivery Rating", value=f"{avg_rating:.2f}" )
st.metric(label="Profit Margin %", value=f"{profit_margin:.2f}%")
