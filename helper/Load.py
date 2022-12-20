import pandas as pd
import warnings
import datetime
warnings.filterwarnings('ignore')

def loadMX():
    print('Cargando Base de datos de México...')
    activeCols = 'A:Z'
    coltypes = {'CFN':str,'REGISTRATION NUMBER': str}
    datesCols = ['APPROVAL DATE', 'EXPIRATION DATE']
    FileName = r'Documents/MDT Mexico DB.xlsm'
    df = pd.read_excel(FileName,sheet_name = 'ACTIVE CODES',usecols= ['REGISTRATION NUMBER','REGISTRATION NAME','STATUS','EXPIRATION DATE','CFN','CFN DESCRIPTION','OU','MANUFACTURING SITE','LICENSE HOLDER'],converters={'CFN':str,'REGISTRATION NUMBER':str},
                                date_parser = ['EXPIRATION DATE'])
    print('Base de datos Cargada')
    return df

def loadCOF(FileName):
    print('Cargando Documento COFEPRIS...')
    path = f'Documents\{FileName}'
    df = pd.read_excel(path,converters={'No. Registro':str},sheet_name = 'Procesos',date_parser=['Fecha expiración registro'])
    df = df.rename(columns={'No. Registro': 'REGISTRATION NUMBER'})
    print('Documento COFEPRIS cargado')
    return df

def load_SPlan():
    print('Cargando Submission Plan...')
    df = pd.read_excel('Documents\Submission Plan - Full Report.xlsx',usecols=['Id','RAS Name','Project/Product Name','Status','Submission Type','Expected Submission Date','Approval Date','Therapy Group',
                            'Expected Approval Date','Submission Date','Country','Cluster','License Number','RAC/RAN'])
    df = df.rename(columns={'Project/Product Name':'PRODUCT NAME','License Number':'REGISTRATION NUMBER'})
    print('Submission Plan cargado')
    return df


