# SIQR Modelling Of Covid Data

To understand timely evolution of the Covid19 in India from the onset of it, SIQR modelling approach have been implemented which is discussed in the paper [Modelling and analysis of COVID-19 epidemic in India](https://www.sciencedirect.com/science/article/pii/S2666449620300311). Equations presented in the research paper have been used to fit the ***Total Confirmed Cases*** reported everyday to calculate the fitting parameters which in turn gives us  ***Rate of Transmission*** and ***Effective Reproduction number*** for a time period. Please see explained `SIQR_Modelling.ipynb` for clear understanding of the process. A `streamlit` app has also been created for the calculation of ***Rate of Transmission*** and ***Effective Reproduction Number*** based on the selected ***range of dates***.

* `covid.csv` contains the data used in the modelling project.
* `SIQR_Modelling.ipynb` has detailed comments added for clarity of the process.
* Please make sure you have all the librabries that are mentioned in the requirements.txt file.
* Steps for running the `SIQR_app.py` file has been written below 

## Running Streamlit App

   1. Move this repo to your local machine.
   2. Activate the environment after installing all the dependencies. 
   3. Move into the repo folder from your terminal/cmd.
   4. Type `streamlit run SIQR_app.py` in your terminal
   5. A Browser window will flash up representing the app.
   6. Now, tweak the dates range to see the variation in ***Rate of Transmisson*** and other parameters.

