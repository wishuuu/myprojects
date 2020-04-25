namespace HelloWorld {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;

    operation SayHello() : Unit {
        Message("Helo from quantum world!");
    }
}