# -*- coding: utf-8 -*-
import pymc
import ss_data as data

cost = data.default_supplier_data[:,0]
delivery_time = data.default_supplier_data[:,1]
guarantee = data.default_supplier_data[:,2]
quality = data.default_supplier_data[:,3]

supplier = pymc.DiscreteUniform('supplier', 
                                lower=0,
                                upper=data.default_supplier_data.shape[0]-1,
                                plot=False,
                                doc='Supplier being evaluated.')

@pymc.deterministic(plot=True)
def score(s=supplier):
    return (cost[s]/9 + delivery_time[s]/2 + guarantee[s] + quality[s]/2)/4

M = pymc.MCMC(set([score, supplier]))

for supplier in range(data.default_supplier_data.shape[0]):
    M.get_node('supplier').value = supplier
    score = M.get_node('score').value
    print("Para el proveedor " + str(supplier) + " obtenemos la puntuación: " + str(score) + " (0-peor, 1-mejor)")
