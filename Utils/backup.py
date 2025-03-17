
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