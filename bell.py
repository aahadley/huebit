import qsharp
import transform
import parse 

from Quantum.Bell import BellTest

GATE_COLOR = (255,255,255)
MEAS_COLOR = GATE_COLOR

def run_sim():

    initials = ( qsharp.Result.Zero, qsharp.Result.One )

    for initial in initials:
        res = BellTest.simulate(count=1, initial=initial)
        #print(res)
        #print("Init:"+str(initial.name) + "\t0s="+str(numZeros) + "\t1s="+str(numOnes) + "\tagree="+str(agree))
    return res

def build_matrix():
    
    run_sim()
    get_states = parse.get_states

    matrix = []

    # populate the initial states
    initial = [ transform.vector_to_rgb(get_states("00.txt")), 
                transform.vector_to_rgb(get_states("01.txt")) ]

    matrix.append(initial)

    # first hadamard transform
    matrix.append([GATE_COLOR,
                   transform.vector_to_rgb(get_states("01.txt")) ])

    # result from hadamard
    h1 = [ transform.vector_to_rgb(get_states("10.txt")),
           transform.vector_to_rgb(get_states("11.txt"))]
    
    matrix.append(h1)

    # cnot
    matrix.append([GATE_COLOR,
                   GATE_COLOR])

    # result from cnot
    c1 = [ transform.vector_to_rgb(get_states("20.txt")),
           transform.vector_to_rgb(get_states("21.txt"))]

    matrix.append(c1)

    # measure
    matrix.append([MEAS_COLOR,
                  MEAS_COLOR])
    
    # final result
    m1 = [ transform.vector_to_rgb(get_states("30.txt")),
           transform.vector_to_rgb(get_states("31.txt"))]
    matrix.append(m1)

    return matrix

print(build_matrix())