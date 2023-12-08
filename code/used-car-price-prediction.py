from pathlib import Path
import pandas as pd
import streamlit as st
import predict
import sklearn

def get_user_input(df):
    car_maker = st.selectbox("Manufacturer:", used_car.Make.unique())
    car_type = st.selectbox("Model/Type:", used_car[used_car.Make == car_maker].Type.unique())
    car_origin = st.selectbox("Origin/From:", used_car.Origin.unique())
    car_region = st.selectbox("Selling/Buying Region:", used_car.Region.unique())
    car_option = st.selectbox("Car's Option:", used_car.Options.unique())
    car_gear_type = st.selectbox("Gear Type:", used_car.Gear_Type.unique())
    car_year = st.number_input("Year of Production:", value=2000, step=1)
    car_engine_size = st.number_input("Engine Size:", value=0.0, step=0.1)
    car_mileage = st.number_input("Mileage:", value=0, step=1)

    user_data = pd.DataFrame({
        'Type':[car_type],
        'Region':[car_region],
        'Make':[car_maker],
        'Gear_Type':[car_gear_type],
        'Origin':[car_origin],
        'Options':[car_option],
        'Year':[car_year],
        'Engine_Size':[car_engine_size],
        'Mileage':[car_mileage]
    })

    return user_data

if __name__=="__main__":
    
    used_car = pd.read_csv(str(Path(__file__).parents[1] /'data/used_car_cleaned.csv'))

    st.set_page_config(page_title="Used Car Price Prediction", page_icon=None, layout="centered")
    
    # Displaying text
    st.markdown("<h1 style='text-align: center; color: black;'>USED-CAR PRICE PREDICTION</h1>", unsafe_allow_html=True)

    # Displaying an image
    st.image(str(Path(__file__).parents[1] /'pic/images.png'), width=700)

    st.write("""  
            This application predicts a used-car price based on some features. Please input your car features below here:
             """)
    
    user_data = get_user_input(used_car)

    # display predictions
    if st.button("Predict Price"):
        used_car_price = round(predict.predict(user_data)[0], 2)  # get predicitions
        formatted_X = "{:.2f}".format(used_car_price)
        st.write(f"**Estimated car price :** {formatted_X} RSA")
        st.write("This price calculated using machine learning model, can be used to estimate used-car price for selling or buying.")
