import streamlit as st
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np
from PIL import Image
from sklearn.metrics import r2_score

st.title("Understanding Covid19 data using SIQR Modelling")

st.caption(""" ## To better understand the covid19 pandemic, I have tried to calculate the associated parameters that explains the timely evolution of pandemic.""")

st.caption(""" ### Below, I have used equations derived from ***SIQR*** modelling in paper [Modelling and analysis of COVID-19 epidemic in India](https://www.sciencedirect.com/science/article/pii/S2666449620300311) to calculate Rate of Transmission (beta) and Effective Reproduction number (R) for a time period.  """)

st.caption(""" #### Rate of transmission (beta) and Reproduction number(R) is calculated for a time interval. For eg, it can be calculated for the month ***may*** or for a range of dates. """)



# Generating data for the calculation

df=pd.read_csv(r'C:\Users\Saurav Kumar\projects\covid\covid.csv')

remove_ind=df[df['state']=='TT']['state'].index

df.drop(remove_ind,inplace=True)

grouped_dates=df.groupby('dates').sum().reset_index()

grouped_dates.drop('population',axis=1,inplace=True )

grouped_dates.drop(559,axis=0,inplace=True )



# choosing date range   

range_start_date= datetime.strptime(grouped_dates.dates.values[0],"%Y-%m-%d")
range_end_date= datetime.strptime(grouped_dates.dates.values[-1],"%Y-%m-%d")

first,sec=st.slider("Select the time interval for which you want to calculate:", value=(range_start_date,range_end_date),format="DD/MM/YY")

st.write(" => Your chosen start date",first.date())
st.write(" => Your chosen end date",sec.date())


# Defining a equation in below function which is derived in the research paper that will fit in the scraped data to obtain pandemic parameters.

def optimize(t,a,b):
    return (a/b)*(np.exp(b*t)-1)


# Taking the total reported confirmed Cases from selected start date to selected end date.

y=grouped_dates[(grouped_dates.dates >first.strftime("%Y-%m-%d")) & (grouped_dates.dates <sec.strftime("%Y-%m-%d"))]['confirmed'].cumsum().values

# x (input) as number of days from which we are calculating.

x=np.array(range(1,len(y)+1))


# Fitting the above data points (x,y) on fucntion described in OPTIMIZE while also providing inital guess value for both the fitting parameters

popt,pcov=curve_fit(optimize,x,y,p0=(0.22,0.08))

#Extracting fitting parameters A & B below 

a,b=popt


# Inot will be the total reported confirmed cases on the first day of time interval for which we are calculating.

alpha=a/y[0]

# Beta which is rate of transmission is given by **b+alpha**

beta=alpha+b
    
st.write(f'Rate of Transmission for period between `{first.date()}` to `{sec.date()}` is : ',beta)

reff=beta/alpha
st.write('Effective Reproduction Number for this period is : ', reff)

# Calculating the y_values from our fitted equation.
y_opt=optimize(x,a,b)

fig,ax=plt.subplots(figsize=(12,8))

# fig.xlabel("Selected Date Range")


#plotting observed and obtained y_values(confirmed cases)
fitted = sns.lineplot(x=x,y=y_opt)
observed = sns.lineplot(x=x,y=y)

plt.xlabel("Selected Date Range")
plt.ylabel("Total Confirmed Cases")

ax.legend(['fitted','observed'])

st.caption("""`Note : Please go through the research paper once for better understanding of the calculations performed here.` """)


st.write("Figure 1 below shows the derived equation from SIQR modelling, which is represented in the form as shown in figure 2 ")

image=Image.open('eq9.png')
st.image(image,width=450)
st.caption("`Fig 1` : Derived Equation")

image=Image.open('eq9form.png')
st.image(image,width=250)
st.caption("`Fig 2` : Fitted Equation`")

""" ######  ***Equation in fig 2*** has been fitted on the total confirmed cases for the selected range of dates obtaining fitting parameters A & B which in turns give me (beta) and (R) for the time period.
"""



st.write("Below you can see the two plots, one from observed data and other is the fitted line. R2 score has been calculated to judge the fitting performance")

st.pyplot(fig)

st.write("`Fig. 3` : Observed and fitted graph")

st.write('R2 Score for the fitted equation: ',r2_score(optimize(x,a,b),y)*100)

""" `Note : You will observe different curve for different date range`"""








