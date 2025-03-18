from basics import *

def get_agg_data(data, groupby_coulmns, base_aggs, custom_aggs, include= 'custom', ret_agg_names= False):
    base_agg_data = data.groupby(groupby_coulmns, observed= True).agg(**base_aggs)
    base_agg_names = list(base_aggs.keys())
    if include == 'base':
        if ret_agg_names:
            return base_agg_data.reset_index(), base_agg_names
        return base_agg_data.reset_index()

    custom_agg_names = []
    agg_data = base_agg_data.copy()
    for agg_type, agg_columns in custom_aggs.items():
        if agg_type == '%':
            for column in agg_columns:
                new_column = remove_prefixes(column, ['#', '$'])
                agg_data[f'% {new_column}'] = agg_data[column] * 100 / agg_data[column].sum()
                custom_agg_names.append(f'% {new_column}')
        elif agg_type == 'Avg.':
            for numerator, denominators in agg_columns.items():
                new_numerator = remove_prefixes(numerator, ['#', '$'])
                for denominator in denominators:
                    new_denominator = remove_prefixes(denominator, ['#', '$'])
                    agg_data[f'Avg. {new_numerator} per {new_denominator}'] = agg_data[numerator] / agg_data[denominator]
                    custom_agg_names.append(f'Avg. {new_numerator} per {new_denominator}')
    
    if include == 'both':
        if ret_agg_names:
            return agg_data.reset_index(), base_agg_names + custom_agg_names
        return agg_data.reset_index()

    if ret_agg_names:
        return agg_data.drop(columns= base_agg_data.columns.tolist()).reset_index(), custom_agg_names
    return agg_data.drop(columns= base_agg_data.columns.tolist()).reset_index()