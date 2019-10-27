import math as m

def complex_to_polar(z) -> tuple:
    return m.hypot(z.real, z.imag) , m.atan2(z.imag, z.real)

def transform_xyz(xyz) -> tuple:
    '''
        this rotates the bloch sphere within the rgb color space
    '''

def vector_to_rgb(psi) -> tuple:
    if psi == [-1, -1]:
        return (-1,-1,-1)

    psi_polar=[0,0]
    psi_polar[0] = complex_to_polar(psi[0])
    psi_polar[1] = complex_to_polar(psi[1])

    r0 = psi_polar[0][0]
    r1 = psi_polar[1][1]
    theta = m.acos(r0)

    phi = psi_polar[1][1] - psi_polar[0][1]
    xyz = (round((m.sin(theta)*m.cos(phi) * 128) + 127),
           round((m.sin(theta)*m.sin(phi) * 128) + 127),
           round((m.cos(theta) * 128) + 127))
    
    return xyz