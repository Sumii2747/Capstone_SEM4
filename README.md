# NGSIM Cleaned Dataset

This repository contains the NGSIM Cleaned Dataset, a cleaned and preprocessed version of the Next Generation Simulation (NGSIM) dataset for traffic flow analysis. The NGSIM dataset provides detailed vehicle trajectory data collected on highways in the United States. (https://github.com/Shuoxuan/NGSIM_Cleaned_Dataset)

**Inter-Vehicle Distance Terminology**
![image](https://github.com/Sumii2747/Capstone_SEM4/assets/128542601/ddbf16ba-17b1-4475-963b-0154bb1bc642)


**Updated i80 and us101 ipynb file** in which we combined all datasets of us101 and i80 . Moreover, we added two columns Period and Location in every datasets 

In the ipynb file designated as **01_read_and_clean**, we eliminated the **Lane Changing Vehicle** and simply selected the "Non Lane Changing Vehicle.
- we kept the vehicles from lanes 1, 2, and 3 and deleted certain information where there was no preceding vehicle. 

**02_Exploratory_of_Dataset** The Correlation between the columns is being studied. Additionally, it was evident from the distribution of vehicle speed bar chart that the majority of cars go between 50 and 60 km/h, albeit some displayed a zero speed. 
- Speaking of instant accerlation of autos, only a select few vehicles displayed this phenomenon. Additionally, we examined the association between the columns using a Heat map. 

**03_Transformation_01**  In the transformation stage, all of the vehicle's units are first converted into input variables that are available in feet to metres, feet to seconds, and so on. 
- In order to calculate the acceleration, speed, length, and vehicle class, we then used the Vehicle ID and Frame ID. Three vehicles (Following, Subject, and Preceding) are running in the same lane in a single Frame 
  ID, and we based all calculations on them. 
