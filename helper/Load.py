import pandas as pd
import warnings
import datetime
import smartsheet
import os
warnings.filterwarnings('ignore')

def loadCOF(FileName):
    print('Cargando Documento COFEPRIS...')
    path = f'Documents\{FileName}'
    df = pd.read_excel(path,converters={'No. Registro':str},sheet_name = 'Procesos',date_parser=['Fecha expiración registro'])
    df = df.rename(columns={'No. Registro': 'REGISTRATION NUMBER'})
    print('Documento COFEPRIS cargado')
    return df

# def load_SPlan():
#     print('Cargando Submission Plan...')
#     df = pd.read_excel('Documents\Submission Plan - Full Report.xlsx',usecols=['Id','RAS Name','Project/Product Name','Status','Submission Type','Expected Submission Date','Approval Date','Therapy Group',
#                             'Expected Approval Date','Submission Date','Country','Cluster','License Number','RAC/RAN','License Expiration Date'])
#     df = df.rename(columns={'Project/Product Name':'PRODUCT NAME','License Number':'REGISTRATION NUMBER'})
#     df = df.dropna(subset = ['Submission Type'])
#     df = df[df['Submission Type'].str.contains('Renewal')]
#     print('Submission Plan cargado')
#     return df

def getSheets(sheet_id,SheetName,token):
    print(f'Downloading {SheetName}')
    current_dir = os.getcwd()
    path = f'{current_dir}\Documents/'
    smart = smartsheet.Smartsheet(token)
    smart.Sheets.get_sheet_as_excel(sheet_id,path,SheetName)
    print(f'{SheetName} was correctly Downloaded')

def getReport(report_id,reportName,token):
    print(f'Downloading {reportName}')
    current_dir = os.getcwd()
    path = f'{current_dir}\Documents/'
    smart = smartsheet.Smartsheet(token)
    smart.Reports.get_report_as_excel(report_id,path,reportName)
    print(f'{reportName} was correctly Downloaded')

def load_SPlan(token):
    report_id ='8721565023004548'
    reportName = 'Submission Plan - Full Report.xlsx'
    getReport(report_id,reportName,token)
    print('Cargando Submission Plan...')
    df_plan = pd.read_excel('Documents\Submission Plan - Full Report.xlsx',usecols=['Id','RAS Name','Project/Product Name','Status','Submission Type','Expected Submission Date','Approval Date','Therapy Group',
                            'Expected Approval Date','Submission Date','Country','Cluster','License Number','RAC/RAN','SubOU','License Expiration Date'])
    df_plan = df_plan.rename(columns={'Project/Product Name':'PRODUCT NAME','License Number':'REGISTRATION NUMBER','License Expiration Date':'EXPIRATION DATE'})
    print('Submission Plan cargado')
    return df_plan


