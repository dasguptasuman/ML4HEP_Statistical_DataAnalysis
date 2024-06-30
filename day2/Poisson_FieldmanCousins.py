#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.stats import norm
import ROOT
from scipy.stats import poisson


# In[2]:


from array import array


# In[28]:


mu_true = np.linspace(0, 20, 20001)
len(mu_true)


# In[29]:


bkg = 3


# In[30]:


def Possion(n,mu):
    mu = mu + bkg
    p = poisson.pmf(n, mu)
    return p


# In[31]:


def Limit(arr):
    cumulative_sum = 0
    cumulative_sum_array = [0]
    result_array = []
    for i in range(len(arr)):
        cumulative_sum += arr[i]
        cumulative_sum_array.append(cumulative_sum)
        if ((cumulative_sum <= 0.9) or ((cumulative_sum > 0.9) and (cumulative_sum_array[i]<=0.9))):
            result_array.append(arr[i])
    return len(result_array)-1


# In[32]:


Lower_limit = []
Upper_limit = []


# In[33]:


np.arange(0,10)


# In[34]:


for mu in mu_true:
        #mu = 0.1
        n = np.arange(0,40)
        mu_best = np.maximum(0, n-bkg)
        R = Possion(n,mu)/Possion(n,mu_best)
        Prob = Possion(n,mu)
        #print("Probablity:", Prob)
        #print("R:",R)
        index = np.argsort(R)[::-1]
        #print("index:", index)
        Sort_Prob = Prob[index]
        #print("Sort_Prob:",Sort_Prob)
        End_point = Limit(Sort_Prob)
        #print(End_point)
        n_bound = n[index][:End_point+1]
        #print("n_bount", n_bound)
        upper_limit = np.max(n_bound)
        lower_limit = np.min(n_bound)
        Lower_limit.append(lower_limit)
        Upper_limit.append(upper_limit)


# In[35]:


step_upper = np.where(np.diff((np.array(Upper_limit))) != 0)
step_lower = np.where(np.diff((np.array(Lower_limit))) != 0)


# In[38]:


mu_lo = mu_true[step_lower]
mu_lo = array("d", mu_lo)


# In[39]:


mu_up = mu_true[step_upper]
mu_up = array("d", mu_up)


# In[40]:


bin_center1 = np.arange(0.5, 16.5, 1.0)
bin_center1 = array("d", bin_center1)


# In[41]:


bin_center2 = np.arange(5.5, 31.5, 1.0)
bin_center2 = array("d", bin_center2)


# In[42]:


hlower_limit = ROOT.TGraph(len(mu_lo), bin_center1, mu_lo)
hupper_limit = ROOT.TGraph(len(mu_up), bin_center2, mu_up)

# In[1]:


# Create TMultiGraph
TG = ROOT.TMultiGraph()
hupper_limit.SetMarkerStyle(3)  # 20 corresponds to a filled circle
hlower_limit.SetMarkerStyle(3)
hupper_limit.SetMarkerColor(2)
hlower_limit.SetMarkerColor(4)

TG.Add(hlower_limit, "AP")
TG.Add(hupper_limit, "AP")


# In[44]:


# Create canvas
canvas = ROOT.TCanvas("canvas", "Confidence belt for Poisson distribution", 800, 600)

# Draw TMultiGraph
TG.Draw("A")

TG.GetXaxis().SetTitle("Measured n")
TG.GetYaxis().SetTitle("Signal mean Mu")

TG.GetXaxis().SetRangeUser(0, 15)
TG.GetYaxis().SetRangeUser(0, 15)
# Show the canvas
canvas.SaveAs("output.jpg")
