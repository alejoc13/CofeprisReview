import pandas as pd 
import helper.Load as ld

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


def PrepareData():
    mx = mxTrimer(ld.loadMX())
    sp = spTrimer(ld.load_SPlan())
    File = input('Ingrese el nombre del documento COFEPRIS: ')
    cof = cofTrimer(ld.loadCOF(File))
    return mx,sp,cof

