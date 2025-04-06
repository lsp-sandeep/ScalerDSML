import math as mt
from basics import *
import scipy.stats as st

def get_confidence_interval(data, sample_pct, width):
    if sample_pct < 1:
        sample_data = data.sample(frac= sample_pct)
    else:
        sample_data = data

    sample_size, sample_mean, sample_std = sample_data.shape[0], sample_data.mean(), sample_data.std()

    sample_se = sample_std / mt.sqrt(sample_size)

    lower_width, upper_width = (1 - width)/2, width - ((1-width)/2)
    sample_lower, sample_upper = (
        sample_mean + (st.norm.ppf(lower_width) * sample_se),
        sample_mean + (st.norm.ppf(upper_width) * sample_se)
        )

    return [sample_lower, sample_upper]


def get_ttest_result(left_data, right_data, alpha):
    
    two_tailed_t_stat, two_tailed_p_val = st.ttest_ind(left_data, right_data, alternative= 'two-sided')

    two_tailed_result = 'same' if two_tailed_p_val > alpha else 'different'

    alternative = 'less' if left_data.mean() < right_data.mean() else 'greater'

    one_tailed_t_stat, one_tailed_p_val = st.ttest_ind(left_data, right_data, alternative= alternative)

    one_tailed_result = 'same' if one_tailed_p_val > alpha else alternative

    result = {
        'two_tailed_p_val'  : round(two_tailed_p_val, 5),
        'two_tailed_result' : two_tailed_result,
        'one_tailed_p_val'  : round(one_tailed_p_val, 5),
        'one_tailed_result' : one_tailed_result
    }

    return result