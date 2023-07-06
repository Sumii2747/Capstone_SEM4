# NGSIM Cleaned Dataset

This repository contains the NGSIM Cleaned Dataset, a cleaned and preprocessed version of the Next Generation Simulation (NGSIM) dataset for traffic flow analysis. The NGSIM dataset provides detailed vehicle trajectory data collected on highways in the United States. (https://github.com/Shuoxuan/NGSIM_Cleaned_Dataset)

**Updated i80 and us101 ipynb file** in which we combined all datasets of us101 and i80 . Moreover, we added two columns Period and Location in every datasets 

In the ipynb file designated as **01_read_and_clean**, we eliminated the **Lane Changing Vehicle** and simply selected the "Non Lane Changing Vehicle." Additionally, we kept the vehicles from lanes 1, 2, and 3 and deleted certain information where there was no preceding vehicle. 

**02_Exploratory_of_Dataset** The Correlation between the columns is being studied. Additionally, it was evident from the distribution of vehicle speed bar chart that the majority of cars go between 50 and 60 km/h, albeit some displayed a zero speed. 
- Speaking of instant accerlation of autos, only a select few vehicles displayed this phenomenon. Additionally, we examined the association between the columns using a Heat map. 
