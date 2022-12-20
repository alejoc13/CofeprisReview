import helper.Load as ld
import helper.Processing as pr
import pandas as pd

def review():
    mx,sp,cof = pr.PrepareData()
    findSP,findCOF = pr.searchdiff(cof,sp)
    Coincidence,noCoincidence = pr.comparaDates(mx,cof)




