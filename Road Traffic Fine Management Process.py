#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pm4py
log = pm4py.read_xes(os.path.join("tests","input_data","C:/Users/Asus/Desktop/Road_Traffic_Fine_Management_Process.xes"))
dfg, start_activities, end_activities = pm4py.discover_dfg(log)
pm4py.view_dfg(dfg, start_activities, end_activities)


# In[ ]:





# In[ ]:





# In[ ]:




