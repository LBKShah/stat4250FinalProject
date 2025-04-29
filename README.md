# Chemical Discrimination Using a Colorimetric Sensor Array: A Nonparametric Statistical Analysis

## Abstract
This report presents the analysis of a colorimetric sensor array's ability to distinguish between toxic industrial chemicals (TICs) after two minutes of exposure. Utilizing nonparametric methods and analyzing results from provided experimental datasets, we evaluated chemical separability through Kruskal-Wallis H-tests, Mann-Whitney U-tests, Kolmogorov-Smirnov (KS) tests, and Spearman correlations. Findings demonstrate statistically significant inter-chemical differences, supporting the feasibility of rapid chemical identification.

## Introduction
The mammalian olfactory system inspires artificial chemical detection technologies that aim to identify hazardous chemicals rapidly. This project investigates whether a colorimetric sensor array can distinguish between different TICs after brief exposure using assumption-free statistical methods. We focus solely on nonparametric analyses to avoid reliance on distributional assumptions.

## Methods
Sensor response data were collected after two minutes of chemical exposure (`DB_220_IDLH_2mins.txt`). The analysis involved the following nonparametric tests:

- **Variance Decomposition**
- **Kruskal-Wallis H-tests** (`kruskal_result.csv`)
- **Mann-Whitney U-tests** (`mannwhitney_results.csv`)
- **Kolmogorov-Smirnov tests** (`ks_test_results.csv`)
- **Spearman Correlation Analysis** (`spearman_correlation.csv`)

The `DiscriminationAnalysis.ipynb` notebook was used to organize and execute these analyses.

## Results

### Kruskal-Wallis H-Test
The Kruskal-Wallis results revealed highly significant p-values (all p < 0.001), indicating that many sensors exhibit statistically significant differences between chemical groups.

### Mann-Whitney U-Test
Pairwise comparisons further confirmed these distinctions, with the majority of sensor-chemical pairs showing significant differences at p < 0.05.

### Kolmogorov-Smirnov Test
The KS tests revealed notable distributional differences between chemical response profiles, further validating inter-chemical separability.

### Spearman Correlation
Pattern similarity analysis using Spearman correlation showed that chemically distinct groups exhibit lower correlation values, while replicates within a chemical generally maintained high internal consistency.

### Exploratory Visualizations
- **KS Test Heatmap:** A heatmap visualization of KS test p-values illustrated strong chemical separability, with low p-values (darker shades) concentrated between different chemical classes and higher p-values among replicates.
- **Spearman Correlation Matrix:** The Spearman correlation matrix revealed block-like patterns where replicates of the same chemical clustered tightly, indicating consistent internal sensor behavior, while inter-chemical blocks showed weaker correlations.
- **Mann-Whitney Test Matrix:** Visual matrices summarizing pairwise Mann-Whitney U-test results emphasized distinct separability across chemical groups, confirming findings from the KS test.
- **Variance Decomposition Plots:** Graphical representations of variance decomposition demonstrated that inter-chemical variability significantly exceeded intra-chemical variability across many sensors.
- **t-SNE Visualization:** Although not fully detailed, dimensionality reduction plots (if referenced) visually supported the numerical results by showing distinct clustering of chemical classes.

## Discussion
The results from all nonparametric methods consistently demonstrate that the colorimetric sensor array can reliably distinguish among different TICs based on short exposure durations. Despite inherent variability in sensor responses, robust statistical separation was achieved without relying on parametric assumptions. This supports the array's potential for rapid chemical identification tasks, especially in field and emergency settings.

## Conclusion
Analysis of the provided datasets confirms that colorimetric sensor arrays, evaluated through nonparametric statistical methods, can effectively discriminate between toxic industrial chemicals after just two minutes of exposure.
