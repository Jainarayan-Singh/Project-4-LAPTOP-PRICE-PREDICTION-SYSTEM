import streamlit as st
import pickle
import numpy as np

# page icon
st.set_page_config(page_title='Laptop Price Prediction App', page_icon=':computer:', layout='wide')

tab1, tab2 = st.tabs(['Price Prediction', 'About App'])

with tab1:
    # import the model
    pipe = pickle.load(open('pipe.pkl', 'rb'))
    df = pickle.load(open('df.pkl', 'rb'))

    st.title("Laptop Price Prediction App")

    # brand
    company = st.selectbox('Brand', df['Company'].unique())

    # type of laptop
    type = st.selectbox('Type', df['TypeName'].unique())

    # Ram
    ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

    # weight
    weight = st.number_input('Weight of the Laptop (in kg)')

    # Touchscreen
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

    # IPS
    ips = st.selectbox('IPS', ['No', 'Yes'])

    # screen size
    screen_size = st.number_input('Screen Size (in Inches)')

    # resolution
    resolution = st.selectbox('Screen Resolution',
                              ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600',
                               '2560x1440', '2304x1440'])

    # cpu
    cpu = st.selectbox('CPU', df['Cpu brand'].unique())

    hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])

    ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])

    gpu = st.selectbox('GPU', df['Gpu brand'].unique())

    os = st.selectbox('OS', df['os'].unique())

    if st.button('Predict Price'):
        # query
        ppi = None
        if touchscreen == 'Yes':
            touchscreen = 1
        else:
            touchscreen = 0

        if ips == 'Yes':
            ips = 1
        else:
            ips = 0

        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size
        query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

        query = query.reshape(1, 12)
        st.text("The predicted price of this configuration is ₹ " + str(int(np.exp(pipe.predict(query)[0]))))

with tab2:
    st.info(
        'This is a Laptop Price Prediction web app, which predicts the approximate price of the laptop for required configuration.\n'
        'If User wants to know the price of certain configuration of laptop can give the features information about the laptop\n'
        'and hit Predict button to know the price.')
    st.warning(
        'User should be noticed that this webapp may not give the actual price. To know actual price please kindly \n'
        'visit the actual laptop brand website. Thankyou!')
    st.text('Created by JAINARAYAN SINGH')