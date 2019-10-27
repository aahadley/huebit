namespace Quantum.Bell
{
    open Microsoft.Quantum.Diagnostics;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;

    operation Set(desired: Result, q1: Qubit) : Unit 
    {
        if (desired != M(q1)) 
        {
            X(q1);
        }
    }

operation BellTest (count : Int, initial: Result) : (Int, Int, Int) {
        mutable numOnes = 0;
        mutable agree = 0;
        
        using (qubits = Qubit[2]) {
            for (test in 1..count)
            {
                Set (initial, qubits[0]);
                Set (Zero, qubits[1]);

                DumpRegister("00.txt", qubits[0..0]);
                DumpRegister("01.txt", qubits[0..0]);

                H(qubits[0]);
                DumpRegister("10.txt", qubits[0..0]);
                DumpRegister("11.txt", qubits[1..1]);

                CNOT(qubits[0],qubits[1]);
                DumpRegister("20.txt", qubits[0..0]);
                DumpRegister("21.txt", qubits[1..1]);

                let res = M (qubits[0]);
                DumpRegister("30.txt", qubits[0..0]);
                DumpRegister("31.txt", qubits[1..1]);

                if (M (qubits[1]) == res) {
                    set agree += 1;
                }

                // Count the number of ones we saw:
                if (res == One) {
                    set numOnes += 1;
                }
                
            }
            
            Set(Zero, qubits[0]);
            Set(Zero, qubits[1]);
        }

        // Return number of times we saw a |0> and number of times we saw a |1>
        return (count-numOnes, numOnes, agree);
    }
}