def ferma(heads, legs):
    duck = (4*heads - legs) // 2
    rabbit = heads - duck
    return duck, rabbit

print(ferma(35, 94))
