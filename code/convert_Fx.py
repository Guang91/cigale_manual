import numpy as np
import scipy.constants as cst
nu_1keV = 1e3*cst.eV / cst.h

def convt_Fx_to_Fnu(flux, flux_err, Elo, Eup):
    '''
    Convert X-ray flux to flux density
    Input:
        flux, flux of an X-ray band (untis: erg/s/cm2)
              array-like objects
        flux_err, the uncertainty of flux
        Elo, Eup: observed-frame energy range of flux_xray (units: keV)
    Output:
        Fnu, X-ray flux density (units: mJy)
        Fnu_err, the error of Fnu
    '''
    Fnu = np.array(flux) / (nu_1keV * (Eup-Elo) * 1e-26)
    Fnu_err = np.array(flux_err) / (nu_1keV * (Eup-Elo) * 1e-26)

    return Fnu, Fnu_err
