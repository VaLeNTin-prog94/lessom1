data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(args):
    b=args[:1]
    k=0
    for a in b:
        if isinstance(a,list):
            for j in a:
                if isinstance(j,str):k+=len(k)
                else: k+=j
        if isinstance(a, dict):
            for j in a.keys():
                k+=len(j)
            for j in a.values():
                k += j
        if isinstance(a,tuple):
            for j in a:
                if isinstance(j,int):k+=j
                if isinstance(j, dict):
                    for t in j.keys():
                        k += len(t)
                    for t in j.values():
                        k += t
                m = []
                while isinstance(j, list) == True:
                    m += [list(j[0])]
                    j = j.pop()
                for l1 in m:
                    if isinstance(l1, int):
                        k += l1
                    if isinstance(l1, str):
                        k += len(l1)
                    if isinstance(l1, tuple):
                        for r in l1:
                            if isinstance(r, int): k += r
                            if isinstance(r, str): k += len(r)
                    for l2 in l1:
                        for l in l2:
                            if isinstance(l,int):
                                k+=l
                            if isinstance(l, str):
                                k += len(l)
                            if isinstance(l, tuple):
                                for r in l:
                                    if isinstance(r, int): k += r
                                    if isinstance(r, str): k += len(r)
        if isinstance(a, str):
            k+=len(a)
    if len(args)>1:
        return k+calculate_structure_sum(args[1:])
    return k
result = calculate_structure_sum(data_structure)
print(result)

