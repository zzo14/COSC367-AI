import re

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 31 Jul 2019

    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")
        
        
def forward_deduce (kb):
    c = []
    clause = list(clauses(kb))
    i = 0
    while i < len(clause):
        for item in clause:
            if set(item[1]) <= set(c) and item[0] not in c:
                c.append(item[0])
                clause.remove(item)
                i = 0
            else:
                i += 1 
    return c
