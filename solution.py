import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_chisquare

chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    prop = proportions_chisquare([x_success, x_cnt], 
                                 [y_success, y_cnt])
    p = prop[1]
    if (p > 0.08) and (x_success/x_cnt < y_success/y_cnt):
        return True
    else:
        return False
