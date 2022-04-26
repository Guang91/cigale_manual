import numpy as np
import scipy.constants as cst

# Define wavelenght (units: nm) corresponding to 1 keV
lam_1keV = 1e9*cst.c*cst.h / (1e3*cst.eV)

# Write a box-car filter
def write_boxcar_filter(file_name, filter_name, E_lo, E_up, phot_ct=False, desc='no description'):
    '''
    Input:
        file_name, the file name to output
        filter_name, the name of the filter
                     should be different from any existing name
        E_lo, E_up: energy range of the filter, units: keV
    Keywords:
        phot_ct, True=photon counter
                 Falsse=energy counter
        desc, some descriptions in string
    Output:
        lams, wavelength in nm
        trans, fractional transmission
    '''
    # Get the corresponding wavelength
    lam_lo, lam_up = lam_1keV/E_up, lam_1keV/E_lo
    # Generate the grids
    lams = np.logspace(np.log10(lam_lo), np.log10(lam_up), 100)
    # Set the transmission profile
    trans = np.zeros(len(lams))+1.
    trans[0], trans[-1] = 0, 0

    with open(file_name, mode='w') as file:
        # Write the filter name
        file.write('# ' + filter_name + '\n')
        # Write filter type
        if phot_ct: file.write('# photon\n')
        else: file.write('# energy\n')
        # Write the description
        file.write('# ' + desc + '\n')
        # Wrtie the transmission curve
        # Note that cigale filter is in format of A
        # so need to multiply lam by a factor of 10
        # to convert nm to A
        for lam, tran in zip(lams, trans):
            file.write("%.4e %.3f \n" %(lam*10, tran))

    return None
