'''

Algorithmic Thinking (part1), programming application  2, question 5
Connected components and graph resilience,
https://class.coursera.org/algorithmicthink1-003/human_grading/view/courses/975649/assessments/32/submissions
Author: Sakari Hakala

'''

import alg_application2_provided as provided
import matplotlib.pyplot as plt
import algo_pa2 as pa2
import algo_app2_1 as app2

cn =  provided.load_graph(provided.NETWORK_URL)
upa = app2.create_UPA(1239,2)
uer = app2.undirected_ER(1239,0.004)

order_cn = app2.fastTargetedOrder(cn)
order_upa = app2.fastTargetedOrder(upa)
order_uer = app2.fastTargetedOrder(uer)

resillience_cn = pa2.compute_resilience(cn, order_cn)
resillience_upa = pa2.compute_resilience(upa, order_upa)
resillience_uer = pa2.compute_resilience(uer, order_uer)

plt.plot(resillience_cn, '-b', label = 'Provided computer network')
plt.plot(resillience_upa, '-r', label = 'UPA graph, m = 2')
plt.plot(resillience_uer, '-g', label = 'uER graph, p = 0.004')
plt.title('Graph resillience under targeted attack')
plt.xlabel('Number of nodes attacked')
plt.ylabel('Size of a largest connected component')
plt.legend(loc = 'upper right')
plt.savefig('algo_app2_plot3_2')
