# -*- coding: utf-8 -*-
from ..faraday import faraday_laws
from chempy.util.testing import requires
from chempy.units import default_units, default_constants, units_library, allclose


def test_faraday_equation():
    """
    Test case obtained from the Chemistry Department at Prince Sattam Bin Abdulaziz University.
    """
    # 𝐂𝐮𝟐+(𝐚𝐪) + 𝟐 𝐞− → 𝐂𝐮 (𝐬)
    assert(faraday_laws(63.5, 2, 1) == 0.404)
    
@requires(units_library)
def test_faraday_laws_units():
    J = default_units.joule
    K = default_units.kelvin
    coulomb = default_units.coulomb
    v = faraday_laws(145, 15, 1, 310 * K, default_constants)
    assert allclose(1000 * v, 60.605 * J / coulomb, rtol=1e-4)