import helper.Load as ld
import helper.Processing as pr
import pandas as pd

def review(token):
    sp,cof = pr.PrepareData(token)
    pr.searchdiff(cof,sp)
  
    




