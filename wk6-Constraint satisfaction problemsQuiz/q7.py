import itertools, copy 
from csp import *

def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x: v for x, v in zip(names, values)}
        if all(satisfies(assignment, constraint) for constraint in csp.constraints):
            yield assignment
            


def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    tda = {(x, c) for c in csp.constraints for x in scope(c)}
    while tda:
        x, c = tda.pop()
        ys = list(scope(c) - {x})
        new_domain = set()
        for xval in csp.var_domains[x]:
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):
                    new_domain.add(xval)
                    break
        if csp.var_domains[x] != new_domain:
            csp.var_domains[x] = new_domain
            for cprime in set(csp.constraints) - {c}:
                if x in scope(c):
                    for z in scope(cprime):
                        if x != z:
                            tda.add((z, cprime))
    return csp

cryptic_puzzle = CSP(
    var_domains={x: set(range(0, 10)) for x in 'twofur'},
    constraints={
        lambda t, w, o, f, u, r: len({t, w, o, f, u, r}) == 6 and f == 1 and t > 0,
        lambda o, r: o + o == r or o + o == r + 10,
        lambda w, u: w + w == u or w + w == u + 10 or w + w + 1 == u or w + w + 1 == u + 10,
        lambda t, o: t + t == o or t + t == o + 10 or t + t + 1 == o or t + t + 1 == o + 10,
        lambda t, w, o, f, u, r: (100 * t + 10 * w + o) * 2 == (1000 * f + 100 * o + 10 * u + r)})