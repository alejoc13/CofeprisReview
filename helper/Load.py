import pandas as pd
import datetime
def loadMX():
    pass

def loadCOF():
    cof = pd.read_excel('Documents\cofepris.xlsm',converters={'No. Registro':str},sheet_name = 'Procesos')
    cof = cof.rename(columns={'No. Registro': 'REGISTRATION NUMBER'})
    return cof

def load_SPlan():
    print('Cargando Submission Plan...')
    df_plan = pd.read_excel('Documents\Submission Plan - Full Report.xlsx',usecols=['Id','RAS Name','Project/Product Name','Status','Submission Type','Expected Submission Date','Approval Date','Therapy Group',
                            'Expected Approval Date','Submission Date','Country','Cluster','License Number','RAC/RAN'])
    df_plan = df_plan.rename(columns={'Project/Product Name':'PRODUCT NAME','License Number':'REGISTRATION NUMBER'})
    print('Submission Plan cargado')
    return df_plan


