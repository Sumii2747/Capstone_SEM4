#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import random


# In[5]:


class clean():
    # Removing the Lane changing vehicle and keeping only non-lane change Vehicle
    
    def remove_lane_change(self,df):
        self.previous_lane_id = None
        self.filtered_data = []

        for index, row in df.iterrows():
            self.current_vehicle_id = row['Vehicle_ID']
            self.current_lane_id = row['Lane_ID']

            if self.previous_lane_id is None or self.current_lane_id == self.previous_lane_id:
                self.filtered_data.append(row)

            self.previous_lane_id = self.current_lane_id

        self.filtered_df = pd.DataFrame(self.filtered_data)
        return self.filtered_df

    
    
    def filter_non_zero_values(self,df):
        
        # we are removing the zero when there is no preceding vehicles
        
        df = df[df['Preceding'] != 0]
        df = df[df['Following'] != 0]
        df = df[df['Space_Headway'] != 0]
        df = df[df['Time_Headway'] != 0]
        return df
    
    def filter_by_desired_lanes(self,df):
        
          # we are taking three lanes 1 , 2 and 3 and 4 , 5 , 6 and 7 are ramps or exit
        desired_lanes = [1, 2, 3]
        df = df[df['Lane_ID'].isin(desired_lanes)]
        return df
        
    def remap_pair_time(self, df):
        '''
        Map the Pairs for the Preceding and lead vehicle. 
        Input: 
            df
        Ouptut: 
            df
        '''
        df = df.sort_values(by=['Global_Time'],
                            ascending=True, ignore_index=True)
        df['pair_Time_Duration'] = (df.groupby(
            ['L-F_Pair'], as_index=False).cumcount()*0.1)
        x = (df[['L-F_Pair', 'pair_Time_Duration']].groupby(['L-F_Pair'],
             as_index=False).max(['pair_Time_Duration']))
        dict_lenght = dict(zip(x['L-F_Pair'], x['pair_Time_Duration']))
        df["total_pair_dur"] = df["L-F_Pair"].map(dict_lenght)
        return df
    
    def time_pairs(self, df):
        '''
        Map the Pairs for the Preceding and lead vehicle. 
        Input: 
            df
        Ouptut: 
            df
        '''
        df = df.sort_values(by=['Global_Time'],
                            ascending=True, ignore_index=True)
        df['pair_Time_Duration'] = (df.groupby(
            ['L-F_Pair'], as_index=False).cumcount()*0.1)
        x = (df[['L-F_Pair', 'pair_Time_Duration']].groupby(['L-F_Pair'],
             as_index=False).max(['pair_Time_Duration']))
        dict_lenght = dict(zip(x['L-F_Pair'], x['pair_Time_Duration']))
        df["total_pair_duration"] = df["L-F_Pair"].map(dict_lenght)

        return df
    
    def train_test_pair(self, df, split, neural=False, seed=0):
        
        total_pairs = df["L-F_Pair"].unique()
        total_pairs = total_pairs.tolist()
        test_split_cnt = round(len(total_pairs) * split)
        test_split_pairs = random.sample(total_pairs, test_split_cnt)
        train_df = df[df['L-F_Pair'].isin(test_split_pairs)]
        test_df = df[~df['L-F_Pair'].isin(test_split_pairs)]
        return train_df, test_df





