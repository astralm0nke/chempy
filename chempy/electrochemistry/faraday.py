def faraday_laws(
    atomic_mass, charge, valence, constants=None, units=None
):
    """
    Faraday's 1st & 2nd Laws of Electrolysis: Mass of species liberated or deposited at an electrode
    is directly proportional to total electrical charge applied,
    but inversely proportional to valency of freed material. (Serway 2005)

    Parameters
    ----------
    atomic_mass : float
        Molar mass of chemical species being dissolved (g/mol).
    charge : integer
        Total electrical charge passed during electrolytic reaction in coloumbs.
    valency : integer
        Number of valence electrons involved in electrolytic reaction.
    constants : object (optional, default: None)
        Constant attributes accessed:
            F - Faraday constant (Col/mol)
    units : object (optional, default: None)
        Unit attributes: gram, coulomb, joule, mol.

    Returns
    -------
    Grams of substance deposited or dissolved at electrode during electrolysis. 
    """
    if constants is None:
        F = 96485.33289
        if units is not None:
            F *= units.coulomb / units.mol
    else:
        F = constants.Faraday_constant

    return (atomic_mass * charge) / (valence * F)