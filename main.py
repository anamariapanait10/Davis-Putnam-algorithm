
def print_set(name, s, end="\n"):
    if len(s) == 0:
        print(f"{name} = \u2205", end=end)
    elif len(s) == 1 and s == ["□"]:
        print(f"{name} = {{□}}", end=end)
    else:
        print(f"{name} = {{", end="")
        for ind in range(len(s)):
            if ind != len(s) - 1:
                if "□" == s[ind]:
                    print("□", end=", ")
                else:
                    print("{" + ",".join(s[ind]), end="}, ")
            else:
                if "□" == s[ind]:
                    print("□", end="")
                else:
                    print("{" + ",".join(s[ind]), end="}")
        print("}", end=end)


def davis_putnam(i, Si, var):
    T1 = []
    T0 = []
    for C in Si:
        if var[i-1] in C:
            T1.append(C)
        if "¬" + var[i-1] in C:
            T0.append(C)
    U = []
    if T1 != [] and T0 != []:
        for C1 in T1:
            for C0 in T0:
                aux = []
                if len(C1) != 1:
                    aux = C1[:]
                    aux.remove(var[i-1])
                if len(C0) != 1:
                    aux2 = C0[:]
                    aux2.remove("¬"+var[i-1])
                    aux += aux2
                    aux = sorted(set(aux), key=aux.index)

                if len(aux) == 0:
                    U.append("□")
                else:
                    U.append(aux)
    Si_1_prim = []
    for C in Si:
        if C not in T0 and C not in T1:
            Si_1_prim.append(C)
    for C in U:
        if C not in Si_1_prim:
            Si_1_prim.append(C)
    Si_1 = Si_1_prim[:]
    for C in Si_1[:]:
        for v in C:
            if "¬"+v in C:
                Si_1.remove(C)

    if i == 1:
        print("i = 1, S1 = S")
    print(f"P{i}.1\tx{i} = {var[i-1]}")
    print_set(f"\t\tT{i}\u00b9", T1)
    print_set(f"\t\tT{i}\u2070", T0)
    print(f"P{i}.2\t", end="")
    print_set(f"U{i}", U)
    print(f"P{i}.3 ", end=" ")
    print_set(f"\tS{i+1}'", Si_1_prim, end="")
    if Si_1_prim == Si_1:
        print(f" = S{i+1}")
    else:
        print()
        print_set(f"\t\tS{i+1}", Si_1)
    print(f"P{i}.4\t", end="")
    if len(Si_1) == 0:
        print(f"S{i+1} = \u2205=> S e satisfiabila")
    elif "□" in Si_1:
        print(f"□ ∈ S{i+1} => S este nesatisfiabila")
    else:
        print(f"i = {i + 1}", end="\n\n")
        davis_putnam(i+1, Si_1, var)


if __name__ == '__main__':
    # {{¬v1, v2, ¬v4}, {¬v3, ¬v2}, {v1, v3}, {v1}, {v3}, {v4}}
    # {{v1, ¬v3},{v2, v1}, {v2, ¬v1, v3}}
    # {{-v2},{-v2, -v3},{-v3,v4},{-v3},{-v1,v2},{v1},{-v3,-v4},{-v4}}
    # {{-v0, -v1, v2}, {-v3,v1,v4},{-v0,-v4,v5},{-v2,v6},{-v5,v6},{-v0,v3},{v0},{-v6}}
    # {{¬v1, ¬v2, ¬v4}, {¬v2, ¬v3}, {v1, ¬v3}, {v1, v4}, {v3}}
    inp = input("S = ").replace("-", "¬").replace(",", " ").replace("}", "|").replace("{", "|").split("|")

    S = []
    for elem in inp:
        if elem != "" and elem != " " and elem != "  ":
            S.append(elem.split())
    var = set()
    for elem in S:
        for v in elem:
            if "¬" not in v:
                var.add(v)
            else:
                var.add(v[1:])
    var = sorted(var)

    inp2 = input("var = ")
    if len(inp2) != 0:
        var = inp2.replace(",", "").split()

    print()
    print_set("S", S)
    davis_putnam(1, S, var)