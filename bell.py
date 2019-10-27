import qsharp
import transform
import parse
import json
import serial

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

def build_matrix_bell():

    run_sim()
    get_states = parse.get_states

    matrix = []
    ZERO_RGB = (0,0,0)

    # populate the initial states
    initial = [ transform.vector_to_rgb(get_states("00.txt")),
                transform.vector_to_rgb(get_states("01.txt")),
                ZERO_RGB,
                ZERO_RGB ]

    matrix.append(initial)

    # first hadamard transform
    matrix.append([GATE_COLOR,
                   transform.vector_to_rgb(get_states("01.txt")),
                   ZERO_RGB,
                   ZERO_RGB ])

    # result from hadamard
    h1 = [ transform.vector_to_rgb(get_states("10.txt")),
           transform.vector_to_rgb(get_states("11.txt")),
           ZERO_RGB,
           ZERO_RGB]

    matrix.append(h1)

    # cnot
    matrix.append([GATE_COLOR,
                   GATE_COLOR,
                   ZERO_RGB,
                   ZERO_RGB])

    # result from cnot
    c1 = [ transform.vector_to_rgb(get_states("20.txt")),
           transform.vector_to_rgb(get_states("21.txt")),
           ZERO_RGB,
           ZERO_RGB]

    matrix.append(c1)

    # measure
    matrix.append([MEAS_COLOR,
                   MEAS_COLOR,
                   ZERO_RGB,
                   ZERO_RGB])

    # final result
    m1 = [ transform.vector_to_rgb(get_states("30.txt")),
           transform.vector_to_rgb(get_states("31.txt")),
           ZERO_RGB,
           ZERO_RGB]

    matrix.append(m1)

    return {"results" : matrix}

m = build_matrix_bell()

res = json.dumps(m, ensure_ascii=True)

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
ser.open()
ser.write(bytes(res,"utf-8"))
