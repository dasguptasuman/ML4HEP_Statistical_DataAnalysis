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


mu_true = np.linspace(0, 20, 20001) # Genarate mu_true 
len(mu_true)


# In[29]:


bkg = 3 # we fixed the bkg


# In[30]:


def Possion(n,mu):
    # Likelihood: the poisson probablity for getting measured n for  mean (mu + bkg) : implement this function by hand 
    return p


# In[31]:


Lower_limit = []
Upper_limit = []


# In[33]:


np.arange(0,10)


# In[34]:


# We want to caculate acceptance region for each value of mu_true


for mu in mu_true:
        n = np.arange(0,40)
        mu_best = # TODO: mu_cap value
        R = Possion(n,mu)/Possion(n,mu_best) # Likelihood ratio
        Prob = Possion(n,mu)
        #Sort the probablity "Prob" by increasing order of R : ToDO
        # Find Endpoins of acceptance region for CL 90% : Cumulative Sum: ADD "Prob" on the basis of R untill sum is just satisfy > 0.90
        #EndPoints = Define funtion that do that
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
