
# Code to plot optimal barplots

n = len(categorical_columns)

r = mt.ceil(mt.sqrt(n))
c = mt.ceil(n / r)

fig, axes = plt.subplots(r, c, figsize=(15, 15))
axes = axes.flatten()

for i, column in enumerate(categorical_columns):
    agg_data = (
        analysis_data
        .groupby(column, observed=True)['User_ID']
        .nunique().reset_index()
    )
    agg_data['User_ID'] = agg_data['User_ID'] * 100 / analysis_data['User_ID'].nunique()
    sns.barplot(
        data=agg_data,
        x=column, y='User_ID', ax=axes[i]
        )
    axes[i].set_title(f'{column} vs % of Users')
    axes[i].set_xlabel(column)
    axes[i].set_ylabel('Count')

for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()


# Plot multiple graphs
import matplotlib.pyplot as plt
import seaborn as sns

r, c = get_size(categorical_columns + numerical_bucketed_columns), get_size(custom_aggs) + 1

fig, axes = plt.subplots(r, c, figsize=(r*10, c*5))

for i, column in enumerate(categorical_columns + numerical_bucketed_columns):
    agg_data, agg_columns = get_agg_data(analysis_data, column, base_aggs, custom_aggs, ret_agg_names= True)
    for j, agg_column in enumerate(agg_columns):
        sns.barplot(data=agg_data, x=column, y=agg_column, ax=axes[i][j])
        axes[i][j].set_title(f'{column} vs {agg_column}')
        axes[i][j].set_xlabel(column)
        axes[i][j].set_ylabel(agg_column)
        axes[i][j].bar_label(axes[i][j].containers[0])

plt.tight_layout()
plt.show()

#

r, c = get_size(categorical_columns), get_size(user_base_aggs) + get_size(user_agg_columns) + 1

fig, axes = plt.subplots(r, c, figsize=(r*5, c*5))

for i, column in enumerate(categorical_columns):
    for j, agg_column in enumerate(user_agg_columns):
        sns.kdeplot(data= user_agg_data, x= agg_column, hue= column, common_norm= False, ax= axes[i][j])
        axes[i][j].set_title(f'{column} vs {agg_column}')
        axes[i][j].set_xlabel(agg_column)
        axes[i][j].set_ylabel(column)

plt.tight_layout()
plt.show()
