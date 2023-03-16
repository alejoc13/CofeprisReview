import pandas as pd 
import helper.Load as ld

def create_excelSPCOF(doc1,doc2):
    print('Este documento almacenará la comparación con Submission Plan')
    name = input('Ingrese el nombre del archivo a guardar:')
    path = f'Resultados\{name}.xlsx'
    
    with pd.ExcelWriter(path) as writer1:
        doc1.to_excel(writer1, sheet_name = 'Solo en SubPlan', index = False)
        doc2.to_excel(writer1, sheet_name = 'Solo en COFEPRIS', index = False)

def create_excelSearch(doc1,doc2,doc3,sp):
    print('Este documento almacenará la comparación con bases de datos')
    name = input('Ingrese el nombre del archivo a guardar: ')
    path = f'Resultados\{name}.xlsx'
    repo = pd.merge(sp,doc2, how='inner',on='REGISTRATION NUMBER')
    with pd.ExcelWriter(path) as writer1:
        doc3.to_excel(writer1, sheet_name = 'Con CFNs', index = False)
        doc2.to_excel(writer1, sheet_name = 'Solo registros', index = False)
        doc1.to_excel(writer1, sheet_name = 'Sin coincidencias', index = False)
        repo.to_excel(writer1, sheet_name = 'busqueda en Submission Plan', index = False)

    pass

def TrimCols(row,col = 'REGISTRATION NUMBER'):
    val = str(row[col])
    val = val.strip()
    return val

def addParticle(row,col = 'REGISTRATION NUMBER'):
    val = str(row[col])
    if 'SSA' in val:
        return val
    else:
        val += ' SSA'
        return val
def mxTrimer(mx):
    print('Pre procesando base de datos de México')
    for colu in mx.columns:
        if colu not in ['APPROVAL DATE','EXPIRATION DATE']:
            mx[colu] = mx.apply(TrimCols,axis = 1,col = colu)
    return mx

def spTrimer(sp):
    print('Pre procesando Submission Plan')
    for colu in sp.columns:
        if colu not in ['Expected Submission Date','Approval Date','Expected Approval Date','Submission Date']:
            sp[colu] = sp.apply(TrimCols,axis = 1, col = colu)
    return sp

def cofTrimer(cof):
    print('Pre-procesando documento COFEPRIS')
    for colu in cof.columns:
        if colu not in ['Fecha Sometimiento','Fecha disponible Web','Fecha de entrega del CIS','Fecha expiración registro']:
            cof[colu] = cof.apply(TrimCols,axis = 1, col = colu)
    return cof
def separeData(cof,sp):
    print('Separando las renovaciones en el documento COFEPRIS')
    cof1 = cof[cof['TRAMITE'] == 'PRÓRROGA']
    print('Separando los datos de México del Submission Plan')
    sp1 = sp[sp['Country'] == 'MX - Mexico']
    return cof1,sp1

def PrepareData(token):
    sp = spTrimer(ld.load_SPlan(token))
    File = input('Ingrese el nombre del documento COFEPRIS: ')
    cof = cofTrimer(ld.loadCOF(File))
    cof,sp = separeData(cof,sp)
    cof['REGISTRATION NUMBER'] = cof.apply(addParticle,axis = 1)
    sp['REGISTRATION NUMBER'] = sp.apply(addParticle,axis = 1)
    return sp,cof

def searchdiff(cof,sp):
    '''
    input:
        cof: Documento del cofepris ya procesado para tener solo las Prórrogas.
        sp: Submission Plan(version guardada en la carpeta documents).
    output:
        findSP: lo que no está en cofepris pero si en submission Plan.
        findCOF lo que no está en Submission Plan pero si en Cofepris Doc.
    '''
    # Lo que no se encuentra en el submission plan pero si está en cofepris doc
    cof_reg = [reg for reg in cof['REGISTRATION NUMBER']]
    findSP = sp[~sp['REGISTRATION NUMBER'].isin(cof_reg)]
    # Lo que no se encuentra en el doc cofepris pero si está en cofepris SP
    sp_reg = [reg for reg in sp['REGISTRATION NUMBER']]
    findCOF = cof[~cof['REGISTRATION NUMBER'].isin(sp_reg)]
    create_excelSPCOF(findSP,findCOF)

def comparaDates(mx,cof):
    print('Comparando información...')
    mx1 = mx.drop(['CFN','CFN DESCRIPTION'], axis = 1)
    mx1 = mx1.drop_duplicates(subset = ['REGISTRATION NUMBER'])
    Conicidence = pd.DataFrame(columns=mx1.columns)
    noConicidence = pd.DataFrame(columns=mx1.columns)
    referencias = set([ref for ref in mx1['REGISTRATION NUMBER']])
    cof1 = cof[cof['REGISTRATION NUMBER'].isin(referencias)]
    for rn in referencias:
        a = mx1[mx1['REGISTRATION NUMBER'] == rn]
        a = a.reset_index(drop=True)
        refDate = a['EXPIRATION DATE'][0]
        medio = cof1[cof1['REGISTRATION NUMBER']==rn]
        b = [date for date in medio['Fecha expiración registro']]
        if len(b) != 0:
            if (refDate in b):
                Conicidence = pd.concat([Conicidence,a])
            else:
                noConicidence = pd.concat([noConicidence,a])
    return Conicidence,noConicidence

def recoverCFNs(df_ref,mx):
    ref = set(df_ref['REGISTRATION NUMBER'])
    mx1 = mx[mx['REGISTRATION NUMBER'].isin(ref)]
    return mx1







