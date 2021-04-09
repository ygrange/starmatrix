
"""
Datasets of Supernova ejections for different metallicities

"""

sn_elements_list = ["He4", "C12", "C13", "N14", "O16", "Ne", "Mg", "Si", "S", "Ca", "Fe"]


def empty_yields_set():
    return dict(zip(sn_elements_list, [0.0 for i in range(11)]))


def yields(dataset_key, feh):
    datasets = {
        "iwa1998": yields_from_iwamoto,
        "sei2013": yields_from_seitenzahl,
        "lm2020": yields_from_leung_nomoto_2020
    }
    sn_yields = datasets[dataset_key](feh)
    return dict(zip(sn_elements_list, sn_yields))


def yields_from_iwamoto(feh):
    """
    Supernova data source: Iwamoto, K. et al., 1999, ApJ 125, 439
    """
    if feh < -0.3:
        return [0.0, 0.0508, 1.56e-9, 3.31e-8, 0.133, 0.00229, 0.0158, 0.142, 0.0914, 0.0181, 0.68]
    else:
        return [0.0, 0.0483, 1.40e-6, 1.16e-6, 0.143, 0.00202, 0.0085, 0.154, 0.0846, 0.0119, 0.626]


def yields_from_seitenzahl(feh):
    """
    Supernova data source: Seitenzahl et al. 2013, MNRAS, Vol 429, Issue 2, 1156–1172
    The four datasets are provided for FeH values of -2, -1, -0.301 and 0. We assign them to 4 intervals.
    """
    if feh <= -1.5:
        return [0.0, 3.16e-03, 2.72e-10, 7.22e-08, 9.47e-02, 3.74e-03, 2.90e-02, 2.89e-01, 1.15e-01, 1.77e-02, 6.72e-01]
    elif -1.5 < feh <= -0.65:
        return [0.0, 3.15e-03, 1.91e-09, 4.71e-07, 9.64e-02, 3.69e-03, 2.69e-02, 2.94e-01, 1.12e-01, 1.66e-02, 6.66e-01]
    elif -0.65 < feh <= -0.15:
        return [0.0, 3.10e-03, 8.47e-09, 1.80e-06, 9.87e-02, 3.06e-03, 2.02e-02, 2.90e-01, 1.12e-01, 1.57e-02, 6.46e-01]
    elif -0.15 < feh:
        return [0.0, 3.04e-03, 1.74e-08, 3.21e-06, 1.01e-01, 3.53e-03, 1.52e-02, 2.84e-01, 1.11e-01, 1.47e-02, 6.22e-01]


def yields_from_leung_nomoto_2020(feh):
    """
    Supernova data source: Seitenzahl et al. 2013, MNRAS, Vol 429, Issue 2, 1156–1172
    The seven datasets are provided for Z/Zsun values of 0, 0.1, 0.5, 1, 2, 3 and 5.
    Using Zsun = 0.0169 the corresponding FeH values are -1, -0.301, 0.0, 0.301, 0.4771 and 0.69897.
    We use seven intervals delimited by midpoints of those values.
    """
    if feh <= -1.65:
        return [0.0, 3.39e10-3, 3.33e10-10, 1.16e10-8, 1.14e10-1, 3.98e10-3, 1.70e10-2, 1.17e10-1, 5.40e10-2, 1.11e10-2, 6.73e10-1]
    elif -1.65 < feh <= -0.65:
        return [0.0, 3.38e10-3, 1.22e10-10, 4.53e10-9, 1.14e10-1, 3.96e10-3, 1.60e10-2, 1.22e10-1, 5.28e10-2, 9.73e10-3, 6.69e10-1]
    elif -0.65 < feh <= -0.15:
        return [0.0, 3.38e10-3, 3.41e10-10, 1.37e10-8, 1.16e10-1, 4.40e10-3, 1.11e10-2, 1.36e10-1, 6.14e10-2, 9.38e10-3, 6.34e10-1]
    elif -0.15 < feh <= 0.15:
        return [0.0, 3.35e10-3, 1.25e10-9, 3.80e10-8, 1.17e10-1, 4.00e10-3, 8.26e10-3, 1.35e10-1, 6.80e10-2, 8.49e10-3, 6.10e10-1]
    elif 0.15 < feh <= 0.39:
        return [0.0, 3.29e10-3, 4.59e10-9, 9.63e10-8, 1.19e10-1, 3.86e10-3, 5.46e10-3, 1.32e10-1, 5.69e10-2, 7.14e10-3, 5.83e10-1]
    elif 0.39 < feh <= 0.59:
        return [0.0, 2.62e10-3, 2.90e10-8, 6.40e10-7, 1.12e10-1, 3.42e10-3, 3.77e10-3, 1.30e10-1, 5.33e10-2, 6.79e10-3, 5.57e10-1]
    elif 0.59 <= feh:
        return [0.0, 2.20e10-3, 1.20e10-8, 9.43e10-8, 1.40e10-1, 3.16e10-3, 2.66e10-3, 1.40e10-1, 3.91e10-2, 5.45e10-3, 5.15e10-1]

