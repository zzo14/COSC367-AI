def posterior(prior, likelihood, observation):
    t_part , f_part, normal = prior, 1-prior, 0
    for p, o in zip(likelihood, observation):
        if o:
            t, f = p[o], p[1-o]
            t_part *= t
            f_part *= f
        else:
            t, f = 1 - p[1- o], 1- p[o]
            t_part *= t
            f_part *= f            
    normal = 1/(t_part + f_part)
    return t_part*normal



prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, True, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))  