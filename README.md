# Chemical Discrimination Testing with Colorimetric Sensor Arrays

## Overview

This project evaluates whether a colorimetric sensor array can reliably distinguish between different toxic industrial chemicals (TICs) based on sensor response data collected after 2 minutes of exposure. The work is inspired by the structure of the mammalian olfactory system and aims to determine whether statistically distinct patterns emerge between chemical groups despite short exposure durations.

## Research Objectives

- Primary Research Question:  
  Are inter-chemical differences significantly greater than intra-chemical variability (within replicates)?

- Goal:  
  Use nonparametric statistical methods to evaluate chemical separability in a robust, assumption-free way.

## Nonparametric Modeling Approach

To answer the research question, the following nonparametric methods were used:

- Variance decomposition: Compare inter- versus intra-chemical variance
- Kruskal-Wallis H-test: Identify sensors with statistically significant group-level differences
- Mann-Whitney U-tests: Perform pairwise chemical comparisons
- Kolmogorov-Smirnov tests: Evaluate distributional shape differences
- Spearman correlation: Assess pattern similarity across chemical profiles
- t-SNE: Visualize chemical separation in a fully nonparametric way

These methods avoid assumptions of normality, linearity, and homogeneity of variance, making them suitable for sensor data with complex or unknown distributional properties.

## Comparison to Parametric Methods

Advantages of nonparametric methods:

- Do not require assumptions about data distribution
- More robust to outliers and small sample sizes
- Well-suited to complex, nonlinear chemical response profiles

Disadvantages compared to parametric models:

- Lower statistical power when parametric assumptions are valid
- Limited interpretability and no coefficient estimates
- Nonlinear visualizations (e.g., t-SNE) are harder to interpret quantitatively

Overall, nonparametric methods are a better fit for this application due to the unpredictable nature of chemical sensor output.

## File Descriptions

| File | Description |
|------|-------------|
| `DB_220_IDLH_2mins.txt` | Raw sensor response data for 2-minute chemical exposures. Each column is a sample. |
| `EDA` | Folder with python script for initial Exploratory Data Analysis and related results
| `DiscriminationAnalysis.pdf` | Final project report combining analysis, visualizations, and discussion. |
| `kenfig1b.pptx` | Background presentation on olfactory systems and sensor design. |
| `results` | Plots and graphs from the notebook |
| `Table of Contents.html` | HTML page for navigation and project overview. |
| `README.md` | This file. High-level summary of project purpose, methods, and contents. |

## Summary

This project demonstrates that nonparametric statistical methods can effectively identify chemically meaningful separation in a colorimetric sensor array. Despite short exposure times, sensor profiles show statistically significant distinctions between chemical groups. These results support the feasibility of using such arrays for rapid, robust chemical detection in field settings.
