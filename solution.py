import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_chisquare

chat_id = 1126746074 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p_ar = []
    p1 = len(x_success)/len(x_cnt)
    p2 = len(y_success)/len(y_cnt)
    for i in range(1000):
        n1 = np.random.binomial(1, p1, size = 5000)
        n2 = np.random.binomial(1, p2, size = 5000)
        p_ar.append(mannwhitneyu(n1, n2, alternative = 'greater').pvalue)
        break
    p_ar = np.array(p_ar)
    
    if (np.mean(p_ar > 0.92) > 0.92) and (p2 > p1):
        return True
    else:
        return False
        
