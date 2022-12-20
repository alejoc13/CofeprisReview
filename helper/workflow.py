import helper.Load as ld
import helper.Processing as pr
import pandas as pd

def review():
    mx,sp,cof = pr.PrepareData()
    pr.searchdiff(cof,sp)
    Coincidence,noCoincidence = pr.comparaDates(mx,cof)
    cfn_coincidence = pr.recoverCFNs(Coincidence,mx)
    pr.create_excelSearch(noCoincidence,Coincidence,cfn_coincidence,sp)
    




