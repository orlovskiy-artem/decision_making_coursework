import pandas as pd
import numpy as np
from collections import defaultdict

class Solution:
    def __init__(self, f_list, x_list, N):
        self.f_list = f_list
        self.x_list = x_list
        self.N = N
        self._cache = defaultdict(lambda: defaultdict())
        
    def lambda_(self, k, eps):
        if k in self._cache and eps in self._cache[k]:
            return self._cache[k][eps]
        max_result = 0
        if k==0:
            for x_k in self.x_list[k]:
                if 0<=x_k and x_k<=eps:
                    if self.f_list[k][x_k]>max_result:
                        max_result = self.f_list[k][x_k]
        else:
            for x_k in self.x_list[k]:
                if 0<=x_k and x_k<=eps:
                    if max_result==22:
                        print("asd")
                    lambda_result = self.lambda_(k-1, eps-x_k)
                    result = self.f_list[k][x_k] + lambda_result
                    if result>max_result:
                        max_result = result
                        
        self._cache[k][eps] = max_result
        return max_result
    
    def solve(self):
        return self.lambda_(len(self.f_list)-1, self.N)


class DepSolution:
    def __init__(self, phi_list, theta_list, L_list, N):
        self.phi_list = phi_list
        self.theta_list = theta_list
        self.L_list = L_list
        self.N = N
        self._cache_dep = defaultdict(lambda: defaultdict())
        
    def dep_lambda_(self, k, eps):
        for theta_k in self.theta_list[k]:
