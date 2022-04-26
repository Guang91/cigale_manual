import numpy as np

def get_cigale_prob(fname):
    '''
    Input:
        fname, the file name of cigale output chi
    Ouput:
        unq_vls, unique values of the parameters
        ps, probability of each unique value
    '''
    # Read the cigale output chi file
    chi_data = np.memmap(fname, dtype=np.float64)
    # Separate chi values from parameter values
    chi_data = chi_data.reshape( (2, int(len(chi_data)/2)) )
    # Filter out nan models
    chi_data = chi_data[:, np.isfinite(chi_data[1])]
    # Reset chi=nan to chi=1e99
    chi_data[0, np.isnan(chi_data[0])] = 1e99

    # Get all the unique values
    unq_vls = np.unique( chi_data[1] )
    # Count the probability of each unique value
    ps = []
    for unq_vl in unq_vls:
        # Get the idxs of the unq value
        vl_idxs = np.where( chi_data[1]==unq_vl )
        # Sum up the probability
        ps.append( np.sum( np.exp(-chi_data[0][vl_idxs]/2) ) )
    # Normalize the probability
    ps = np.array(ps) / np.trapz(ps, x=unq_vls)

    return unq_vls, ps

def get_cigale_prob_2d(x_fname, y_fname):
    '''
    Input:
        x_fname, the file name (x-axis) of cigale output chi
        y_fname, the file name (y-axis) of cigale output chi
    Ouput:
        x_unq_vls, x-axis unique values of the parameters
        y_unq_vls, y-axis unique values of the parameters
        pss, probability of each unique-value pair
    '''
    # 2D prob. density map
    x_chi_data = np.memmap(x_fname, dtype=np.float64)
    y_chi_data = np.memmap(y_fname, dtype=np.float64)

    # Separate chi values from parameter values
    x_chi_data = x_chi_data.reshape( (2, int(len(x_chi_data)/2)) )
    y_chi_data = y_chi_data.reshape( (2, int(len(y_chi_data)/2)) )
    # Filter out nan models
    x_chi_data = x_chi_data[:, np.isfinite(x_chi_data[1])]
    y_chi_data = y_chi_data[:, np.isfinite(y_chi_data[1])]
    # Reset chi=nan to chi=1e99
    x_chi_data[0, np.isnan(x_chi_data[0])] = 1e99
    y_chi_data[0, np.isnan(y_chi_data[0])] = 1e99

    # Get all the unique values
    x_unq_vls = np.unique( x_chi_data[1] )
    y_unq_vls = np.unique( y_chi_data[1] )
    # Count the probability of each (x,y) unique value
    pss = []
    for x_unq_vl in x_unq_vls:
        # Create the list for temperary result storage
        ps = []
        for y_unq_vl in y_unq_vls:
            # Get the idxs of the unq value
            vl_idxs = np.where( (x_chi_data[1]==x_unq_vl) &                                 (y_chi_data[1]==y_unq_vl) )
            # Sum up the probability
            # Note that x_chi_data[0] and y_chi_data[0]
            # are the same, so either one is OK
            ps.append( np.sum( np.exp(-x_chi_data[0][vl_idxs]/2) ) )
        # Save the results
        pss.append(ps)
    # Normalize the probability
    pss = np.array(pss) / np.trapz(np.trapz(pss,x=y_unq_vls),x=x_unq_vls)
    return x_unq_vls, y_unq_vls, pss
