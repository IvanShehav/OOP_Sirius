import Tlogelement

elAnd = Tlogelement.TAnd()
elNot = Tlogelement.TNot()

elAnd.link(elNot, 1)

notA = Tlogelement.TNot()
notB = Tlogelement.TNot()
and1 = Tlogelement.TAnd()
and2 = Tlogelement.TAnd()
xor_or = Tlogelement.TOr()

notB.link(and1, 2)      # выход NOT B -> второй вход AND(A, NOT B)
notA.link(and2, 1)      # выход NOT A -> первый вход AND(NOT A, B)
and1.link(xor_or, 1)    # выход AND(A, NOT B) -> первый вход OR
and2.link(xor_or, 2)    # выход AND(NOT A, B) -> второй вход OR

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
        and2.In2 = bool(B)

        xor_res = xor_or.Res
        print(" ", A, "|", B, "|", int(xor_res))
