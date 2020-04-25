namespace Operations {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;

    operation RandomNumber() : Result {
        using (q1 = Qubit()){
            H(q1);
            let r = M(q1);
            Reset(q1);
            return r;
        }
    }
}
