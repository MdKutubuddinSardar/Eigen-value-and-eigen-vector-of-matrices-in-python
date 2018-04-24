import numpy as NP
from scipy import linalg as LA
A=[[2,3,4],[4,0,-1],[2,8,7]]
e_vals, e_vecs = LA.eig(A)
print "Eigen Values are ", e_vals
print "Eigen vectors are ", e_vecs
