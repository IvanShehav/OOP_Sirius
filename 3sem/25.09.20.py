import Tlogelement

elAnd = Tlogelement.TAnd()
elNot = Tlogelement.TNot()
notA  = Tlogelement.TNot()
notB  = Tlogelement.TNot()
and1  = Tlogelement.TAnd()
and2  = Tlogelement.TAnd()
or1   = Tlogelement.TOr()

elAnd.link(elNot, 1)


print("  A | B | not(A&B)")
print("-------------------")

for A in range(2):
    elAnd.In1 = bool(A)
    for B in range(2):
        elAnd.In2 = bool(B)
        print(" ", A, "|", B, "|", int(elNot.Res))


print("=========XOR==========")
print("  A | B | A xor B")
print("-------------------")
for A in range(2):
    for B in range(2):
        notA.In1 = bool(A)
        notB.In1 = bool(B)

        and1.In1 = bool(A)
        and1.In2 = notB.Res

        and2.In1 = notA.Res
        and2.In2 = bool(B)

        or1.In1 = and1.Res
        or1.In2 = and2.Res

        xor_res = or1.Res
        print(" ", A, "|", B, "|", int(xor_res))
