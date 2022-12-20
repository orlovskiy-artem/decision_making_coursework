import pandas as pd
import numpy as np
from collections import defaultdict
from itertools import product
from tqdm import tqdm
from copy import deepcopy

class Solution:
    def __init__(self, f_list, x_list, N):
        self.f_list = f_list
        self.x_list = x_list
        self.N = N
        self._cache = defaultdict(lambda: defaultdict())
        self._argmax = defaultdict()
        self._argmax_array = []

    def lambda_(self, k, eps):
        if k in self._cache and eps in self._cache[k]:
            return deepcopy(self._cache[k][eps])
        max_result = -1
        argmax = {}
        if k==0:
            for x_k in self.x_list[k]:
                if 0<=x_k and x_k<=eps:
                    if self.f_list[k][x_k]>max_result:
                        argmax[k] = x_k
                        max_result = self.f_list[k][x_k]
        else:
            for x_k in self.x_list[k]:
                if 0<=x_k and x_k<=eps:
                    lambda_result, argmax_inner = self.lambda_(k-1, eps-x_k)
                    result = self.f_list[k][x_k] + lambda_result
                    if result>max_result:
                        max_result = result
                        argmax_inner[k] = x_k
                        argmax = argmax_inner
       
        self._cache[k][eps] = max_result, argmax
        return max_result, argmax
    
    def solve(self):
        max_result, argmax = self.lambda_(len(self.f_list)-1, self.N)
        return max_result, argmax


class ThemeSolver:
    def __init__(self, phi_list, theta_list, L_list, N):
        self.phi_list = phi_list
        self.theta_list = theta_list
        self.L_list = L_list
        self.N = N
        self._cache = defaultdict(lambda: defaultdict())
        self._argmax = defaultdict()

    def dep_lambda_(self, k, eps):
        if k in self._cache and eps in self._cache[k]:
            return deepcopy(self._cache[k][eps])
        max_result = -1
        argmax = {}
        if k==0:
            solution = Solution(self.phi_list[k], self.theta_list[k], min(eps, self.L_list[k]))
            phi_result, phi_argmax = solution.solve()
            argmax[k] = phi_argmax
            max_result = phi_result
        else:
            for gamma_k in range(min(self.L_list[k]+1,eps+1)):
                lambda_result, inner_argmax = self.dep_lambda_(k-1, eps-gamma_k)
                sol = Solution(self.phi_list[k], self.theta_list[k], gamma_k)
                phi_result, phi_argmax = sol.solve()
                result = phi_result + lambda_result    
                if result>max_result:
                    max_result=result
                    inner_argmax[k] = phi_argmax
                    argmax = inner_argmax
        self._cache[k][eps] = max_result, argmax
        return max_result, argmax

    def solve(self):
        max_result, argmax = self.dep_lambda_(len(self.phi_list)-1, self.N)
        return max_result, argmax



# class DepSolution:
#     def __init__(self, phi_list, theta_list, L_list, N):
#         self.phi_list = phi_list
#         self.theta_list = theta_list
#         self.L_list = L_list
#         self.N = N
#         self._cache = defaultdict(lambda: defaultdict())
#         self._argmax = defaultdict()

#     def get_theta_by_eps(self, k, eps):
#         self.theta_list[k]

#     def dep_lambda_(self, k, eps, argmax):
#         if k in self._cache and eps in self._cache[k]:
#             return self._cache[k][eps], argmax
#         max_result = 0
#         if k==0:
#             solution = Solution(self.phi_list[k], self.theta_list[k], min(eps, self.L_list[k]))
#             # max_result, phi_argmax = solution.solve()
#             phi_result, phi_argmax = solution.solve()
#             argmax[k] = phi_argmax
#             max_result = phi_result
#         else:
#             for gamma_k in tqdm(range(eps)):
#             # for theta_k_bound in filter(lambda x: sum(x)<=eps, product(*self.theta_list[k])):
#                 # gamma_k = sum(theta_k_bound)
#                 lambda_result, argmax = self.dep_lambda_(k-1, eps-gamma_k, {})
#                 # phi_result = 0
#                 # for phi_k, theta_k, bound in zip(self.phi_list[k], self.theta_list[k], theta_k_bound):
#                 sol = Solution(self.phi_list[k], self.theta_list[k], min(gamma_k,self.L_list[k]))
#                 phi_result, phi_argmax = sol.solve()
#                 # self.phi_list[k], 
#                 # for phi_i,(phi ) in enumerate(zip(self.phi_list, theta_k, self.L_list)):
#                     # if phi_i<k:
#                     # sol = Solution(phi, self.theta_list[phi_i], min(eps,theta_k[phi_i],self.L_list[phi_i]))
#                         # sol = Solution(phi, self.theta_list[phi_i],min(eps,gamma_k[phi_i]))
#                     # lambda_phi_k_result, phi_argmax = sol.solve()
#                     # phi_result += lambda_phi_k_result
#                 # phi_result = sum(map(lambda item: item[0][item[1]], zip(self.phi_list[k],theta_k)))
#                 result = phi_result + lambda_result    
#                 if result>max_result:
#                     max_result=result
#                     argmax[k]=phi_argmax
#                     self._argmax = argmax

#         self._cache[k][eps] = max_result
#         return max_result, argmax

#     def solve(self):
#         max_result, _ = self.dep_lambda_(len(self.phi_list)-1, self.N, {})
#         return max_result, self._argmax



# def get_x(theta, eps):
#     cache = set()
#     def backtrack(eps, path):
#         if eps==0:
#             path_tuple = [*map(lambda item: item[1],sorted(path.items(),key=lambda item: item[0]))]
#             n = len(path_tuple)
#             for _ in range(len(theta)-n):
#                 path_tuple.append(0)
#             path_tuple = tuple(path_tuple)
#             cache.add(path_tuple)
#             return
#         else:
#             for i in range(len(theta)):
#                 if i not in path:
#                     for j in range(len(theta[i])):
#                         if eps-theta[i][j]>=0:
#                             # print(i,j)
#                             path_inner = deepcopy(path)
#                             path_inner[i]=j
#                             backtrack(eps-theta[i][j], path_inner)
#         if eps>0:
#             path = {}   
#     backtrack(eps, {})
#     return cache




# class Solution:
#     def __init__(self, f_list, x_list, N):
#         self.f_list = f_list
#         self.x_list = x_list
#         self.N = N
#         self._cache = defaultdict(lambda: defaultdict())
#         self._argmax = defaultdict()
#         self._argmax_array = []

#     def lambda_(self, k, eps, argmax, argmax_list):
#         # if k in self._cache and eps in self._cache[k]:
#         #     return self._cache[k][eps], argmax, argmax_list
#         max_result = 0
#         if k==0:
#             for x_k in self.x_list[k]:
#                 if 0<=x_k and x_k<=eps:
#                     argmax[k] = x_k
#                     if self.f_list[k][x_k]>max_result:
#                         # argmax[k] = x_k
#                         max_result = self.f_list[k][x_k]
#                         argmax_list.append((k,x_k))
#         else:
#             for x_k in self.x_list[k]:
#                 if 0<=x_k and x_k<=eps:
#                     lambda_result, argmax, argmax_list = self.lambda_(k-1, eps-x_k, {}, [])
#                     result = self.f_list[k][x_k] + lambda_result
#                     if result>max_result:
#                         max_result = result
#                         argmax[k] = x_k
#                         argmax_list.append((k,x_k))
#                         self._argmax = argmax
#                         self._argmax_list = argmax_list
#         self._cache[k][eps] = max_result
#         return max_result, argmax, argmax_list
    
#     def solve(self):
#         max_result, _, argmax_list = self.lambda_(len(self.f_list)-1, self.N, {}, [])
#         return max_result, self._argmax, argmax_list




# class DepSolution:
#     def __init__(self, phi_list, theta_list, L_list, N):
#         self.phi_list = phi_list
#         self.theta_list = theta_list
#         self.L_list = L_list
#         self.N = N
#         self._cache = defaultdict(lambda: defaultdict())
#         self._argmax = defaultdict()

#     def dep_lambda_(self, k, eps, argmax):
#         if k in self._cache and eps in self._cache[k]:
#             return self._cache[k][eps], argmax
#         max_result = 0
#         if k==0:
#             solution = Solution(self.phi_list[k], self.theta_list[k], min(eps, self.L_list[k]))
#             phi_result, phi_argmax = solution.solve()
#             argmax[k] = phi_argmax
#             max_result = phi_result
#         else:
#             for gamma_k in range(eps+1):
#                 lambda_result, dep_argmax = self.dep_lambda_(k-1, eps-gamma_k, {})
#                 sol = Solution(self.phi_list[k], self.theta_list[k], min(gamma_k,self.L_list[k]))
#                 phi_result, phi_argmax = sol.solve()
#                 result = phi_result + lambda_result    
#                 if result>max_result:
#                     max_result=result
#                     argmax.update(dep_argmax)
#                     argmax[k]=dep_argmax
#                     self._argmax = argmax

#         self._cache[k][eps] = max_result
#         return max_result, argmax

#     def solve(self):
#         max_result, argmax = self.dep_lambda_(len(self.phi_list)-1, self.N, {})
#         return max_result, self._argmax



# class ThemeSolution:
#     def __init__(self, phi_list, theta_list, L_list, N):
#         self.phi_list = phi_list
#         self.theta_list = theta_list
#         self.L_list = L_list
#         self.N = N
#         self._cache = defaultdict(lambda: defaultdict())
#         self._argmax = defaultdict()

#     def dep_lambda_(self, k, eps):
#         if k in self._cache and eps in self._cache[k]:
#             return deepcopy(self._cache[k][eps])
#         max_result = -1
#         argmax = {}
#         if k==0:
#             solution = Solution(self.phi_list[k], self.theta_list[k], min(eps, self.L_list[k]))
#             phi_result, phi_argmax = solution.solve()
#             argmax[k] = phi_argmax
#             max_result = phi_result
#         else:
#             # eps = min(eps, self.L_list[k])
#             for gamma_k in range(min(self.L_list[k]+1,eps+1)):
#             # for gamma_k in tqdm(range(eps)):
#                 lambda_result, inner_argmax = self.dep_lambda_(k-1, eps-gamma_k)
#                 # sol = Solution(self.phi_list[k], self.theta_list[k], min(gamma_k,self.L_list[k]))
#                 sol = Solution(self.phi_list[k], self.theta_list[k], gamma_k)
#                 phi_result, phi_argmax = sol.solve()
#                 result = phi_result + lambda_result    
#                 if result>max_result:
#                     max_result=result
#                     inner_argmax[k] = phi_argmax
#                     argmax = inner_argmax
#                     # argmax[k]=dep_argmax
#         self._cache[k][eps] = max_result, argmax
#         return max_result, argmax

#     def solve(self):
#         max_result, argmax = self.dep_lambda_(len(self.phi_list)-1, self.N)
#         return max_result, argmax



