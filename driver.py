import math as m

def complex_to_polar(z) -> tuple:
    return m.hypot(z.real, z.imag) , m.atan2(z.imag, z.real)

def transform_xyz(xyz) -> tuple:
    '''
        this rotates the bloch sphere within the rgb color space
    '''

def vector_to_rgb(psi) -> tuple:
    psi_polar=[0,0]
    psi_polar[0] = complex_to_polar(psi[0])
    psi_polar[1] = complex_to_polar(psi[1])

    r0 = psi_polar[0][0]
    r1 = psi_polar[1][1]
    theta = m.acos(r0)

    phi = psi_polar[1][1] - psi_polar[0][1]
    xyz = ((m.sin(theta)*m.cos(phi) * 128) + 128,
           (m.sin(theta)*m.sin(phi) * 128) + 128,
           (m.cos(theta) * 128) + 128)
    
    return xyz 

psi = [0., .707107 + .707107j]
print(vector_to_rgb(psi), vector_to_rgb([0,1]), vector_to_rgb([1,0]), vector_to_rgb([-1/m.sqrt(2), 1/m.sqrt(2)]))

[[0, -.707+-.707j], [-1,-1], [.707, .5+.5j]]