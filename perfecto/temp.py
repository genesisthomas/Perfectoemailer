from datetime import datetime, timedelta

import numpy as np
import pandas as pd

# https://stackoverflow.com/questions/60226735/how-to-count-overlapping-datetime-intervals-in-pandas


user = 'user'
deviceId = 'deviceId'
reservationid = 'reservationid'
startTime = 'startTime'
endTime = 'endTime'
status = 'status'

# ori_df = pd.DataFrame(columns=[user, deviceId, reservationid, status, startTime,endTime], index=range(4), \
#     data=[['gthomas',9182381092,'3','SCHEDULED','2005-10-01 00:00:00','2006-12-02 00:00:00'],
#             ['gthomas',9182381092,'2','SCHEDULED','2007-09-01 00:00:00','2008-12-01 00:00:00'],
#              ['gthomas',9182381092,'1', 'SCHEDULED','2006-01-01 00:00:00','2007-10-02 00:00:00'],
#             ['gthomas',9182381092,'4','SCHEDULED','2005-10-02 00:00:00','2006-01-02 00:00:00']
#             # ['sthomas',9182381092,'5','SCHEDULED','2007-10-01','2010-04-03'],
#             # ['sthomas',9929292,'6','STARTED','2010-04-04','2199-05-11'],
#             # ['sthomas',9929292,'7','EXPIRED','2016-05-12','2199-12-31']
#             ])

ori_df = pd.DataFrame(columns=[user, deviceId, reservationid, status, startTime,endTime], index=range(7), \
    data=[['gthomas',9182381092,'1','SCHEDULED','2020-12-03 07:00:00','2020-12-03 10:00:00'],
            ['gthomas',9182381092,'2','SCHEDULED','2020-12-03 09:00:00','2020-12-03 13:00:00'],
            ['gthomas',9182381092,'3', 'EXPIRED','2020-12-03 08:00:00','2020-12-03 11:00:00'],
            ['gthomas',9182381092,'4','SCHEDULED','2020-12-03 12:00:00','2020-12-03 16:00:00'],
            ['gthomas',9182381092,'5','SCHEDULED','2020-12-03 11:00:00','2020-12-03 14:00:00'],
            ['gthomas',9182381092,'6','STARTED','2020-12-03 12:00:00','2020-12-03 16:00:00'],
            ['gthomas',9182381092,'7','SCHEDULED','2020-12-03 15:00:00','2020-12-03 18:00:00']
            # ['sthomas',9182381092,'5','SCHEDULED','2007-10-01','2010-04-03'],
            # ['sthomas',9929292,'6','STARTED','2010-04-04','2199-05-11'],
            # ['sthomas',9929292,'7','EXPIRED','2016-05-12','2199-12-31']
            ])

# reservation id 1 should be marked as deleted
#2 & 4 not overlapped
for user_name in ori_df[user].unique():
    pd.options.mode.chained_assignment = None
    df = ori_df[ori_df['user'] == user_name] 
    df = ori_df[ori_df[status].isin(['SCHEDULED', 'STARTED'])] 
    
    df=df.sort_values([startTime,endTime])
    df[startTime] = pd.to_datetime(df[startTime])
    df[endTime] = pd.to_datetime(df[endTime])
    temp_df = df[[startTime,endTime]]
    print("\n full table of user: " + user_name)
    print(temp_df)
    temp_df = temp_df.melt(var_name = 'status',value_name = 'time').sort_values('time')
    temp_df['counter'] = np.where(temp_df['status'].eq(startTime),1,-1).cumsum()
    temp_df = temp_df[temp_df['counter'] > 2 ]  
    temp_df = temp_df[temp_df['status'] == "startTime"].sort_values(['counter'], ascending=[False]).sort_values(['counter'], ascending=[False])
    print((temp_df))
    # if there are more than 2 violations, delete the reservation.
    while(temp_df['time'].shape[0] > 0):
        new_df = df[df[startTime] == temp_df['time'].iloc[0]]
        print("\n violation for user: " + user_name)
        print(new_df)
        df.drop(df[df[reservationid] == new_df[reservationid].iloc[0]].index, inplace = True) 
        temp_df.drop(temp_df[temp_df['time'] == temp_df['time'].iloc[0]].index, inplace = True) 
    print("\n Remaining reservations of user: " + user_name)
    print(df)
    
    # starttime & endtime to be a part of parameterization of the api
    # return list of reservation ids and delete
