import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime
st.image('./R.png')
st.markdown(''' # SR7 Stock Predictor
Shown are the stock price data for Giant Companies!
- App built by `Shreyas Dumbre`
- At `SR7` Stock Predictor we try to predict the most accurate value of the stock.
- Note:- Here at SR7 Stock Predictor we do not give `financial` advice , we predict. 
''')


st.write('---')


st.sidebar.subheader('Select the Date and Preferred Stock')
start_date = st.sidebar.date_input("Start date", datetime.date(2020, 3, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 3, 31))


ticker_list = pd.read_csv(r'C:\Users\LENOVO\Documents\myapp\ABT.txt')
tickerSymbol = st.sidebar.selectbox('Select the Stock', ticker_list) 
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date) 


string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)


st.header('**Stock Data**')
st.write(tickerDf)


st.header('**Prediction Range**')
qf=cf.QuantFig(tickerDf,title='Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)

####
#st.write('---')
#st.write(tickerData.info)ckerDf.Volume)