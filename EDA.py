import pandas as pd
from scipy.stats import kruskal, mannwhitneyu, spearmanr, ks_2samp

# Load and clean the data
df = pd.read_csv("DB_220_IDLH_2mins.txt", sep='\t', header=None)
df.rename(columns={0: 'sample'}, inplace=True)
data = df.set_index('sample').T
clean_data = data.apply(pd.to_numeric, errors='coerce').dropna(axis=1, how='all')

samples = clean_data.columns.tolist()

### 1. Kruskal-Wallis Test
kruskal_result = kruskal(*(clean_data[col].dropna() for col in samples))
print(f"Kruskal-Wallis Test Statistic: {kruskal_result.statistic:.2f}, p-value: {kruskal_result.pvalue:.4e}")

### 2. Mann-Whitney U Test (pairwise)
mannwhitney_results = []

for i in range(len(samples)):
    for j in range(i + 1, len(samples)):
        sample1 = clean_data[samples[i]].dropna()
        sample2 = clean_data[samples[j]].dropna()
        stat, p_value = mannwhitneyu(sample1, sample2, alternative='two-sided')
        mannwhitney_results.append({
            'Sample A': samples[i],
            'Sample B': samples[j],
            'U Statistic': stat,
            'p-value': p_value,
            'Significant?': '✅' if p_value < 0.05 else '❌'
        })

mannwhitney_df = pd.DataFrame(mannwhitney_results).sort_values(by='p-value')


### 3. Spearman’s Rank Correlation (pairwise, fixed to match lengths)
spearman_results = []

for i in range(len(samples)):
    for j in range(i + 1, len(samples)):
        sample1 = clean_data[samples[i]].dropna()
        sample2 = clean_data[samples[j]].dropna()

        min_len = min(len(sample1), len(sample2))
        sample1 = sample1.iloc[:min_len]
        sample2 = sample2.iloc[:min_len]

        corr, p_value = spearmanr(sample1, sample2)
        spearman_results.append({
            'Sample A': samples[i],
            'Sample B': samples[j],
            'Spearman Rho': corr,
            'p-value': p_value,
            'Significant?': '✅' if p_value < 0.05 else '❌'
        })

spearman_df = pd.DataFrame(spearman_results).sort_values(by='p-value')


### 4. Kolmogorov-Smirnov Test (pairwise)
ks_results = []

for i in range(len(samples)):
    for j in range(i + 1, len(samples)):
        sample1 = clean_data[samples[i]].dropna()
        sample2 = clean_data[samples[j]].dropna()

        stat, p_value = ks_2samp(sample1, sample2)
        ks_results.append({
            'Sample A': samples[i],
            'Sample B': samples[j],
            'KS Statistic': stat,
            'p-value': p_value,
            'Significant?': '✅' if p_value < 0.05 else '❌'
        })

ks_df = pd.DataFrame(ks_results).sort_values(by='p-value')

### 5. Display or Save the Tables
print("\n--- Mann-Whitney U Test Results ---")
print(mannwhitney_df)

print("\n--- Spearman’s Rank Correlation Results ---")
print(spearman_df)

print("\n--- Kolmogorov-Smirnov Test Results ---")
print(ks_df)

mannwhitney_df.to_csv('mannwhitney_results.csv', index=False)
spearman_df.to_csv('spearman_results.csv', index=False)
ks_df.to_csv('ks_test_results.csv', index=False)
pd.DataFrame([{'Test': 'Kruskal-Wallis', 'Statistic': kruskal_result.statistic, 'p-value': kruskal_result.pvalue}]).to_csv('kruskal_result.csv', index=False)