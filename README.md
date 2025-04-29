**Statistical Analysis of Colorimetric Sensor Array Responses for Rapid Chemical Detection**

## Project Description
This project investigates the statistical behavior of a colorimetric sensor array exposed to various toxic industrial chemicals (TICs) for short periods (2 minutes). Specifically, it examines whether the variance between different chemical groups is statistically greater than the variance within replicates of the same chemical, thus assessing the reliability and discriminatory power of the sensor array.

The study draws inspiration from the mammalian olfactory system, using a colorimetric approach to simulate chemical "fingerprints" and explores the potential of such an array for rapid, portable chemical detection.

## Research Question
**How consistent are sensor array responses across replicates for each chemical, and are inter-chemical differences statistically greater than intra-chemical variance?**

## Data
- **DB_220_IDLH_2mins.txt**: Sensor array response data. Includes multiple replicate measurements for different chemicals after 2 minutes of exposure.

## Methodology
- **Exploratory Data Analysis (EDA)** to understand the structure and distribution of sensor responses.
- **Non-parametric statistical tests** applied:
  - Kruskal-Wallis H-test (multiple group comparison)
  - Mann-Whitney U-test (pairwise group comparison)
  - Kolmogorov-Smirnov test (distribution comparison)
  - Spearman correlation analysis (response pattern relationships)
- Focus on measuring within-group (intra-chemical) vs between-group (inter-chemical) variability.

## Files
- `DB_220_IDLH_2mins.txt` - Raw sensor response data.
- `EDA.py` - Python script for initial exploratory analysis.
- `kruskal_result.csv` - Results of Kruskal-Wallis tests.
- `mannwhitney_results.csv` - Results of Mann-Whitney U-tests.
- `ks_test_results.csv` - Results of Kolmogorov-Smirnov tests.
- `spearman_results.csv` - Results of Spearman correlation analysis.
- `kenfig1b.pptx` - Background material on olfactory systems and artificial chemical sensing.

## Next Steps / To-Do
- Further refine statistical analysis (e.g., effect size measurements).
- Visualize intra- vs inter-chemical variance.
- Explore multivariate analysis methods (e.g., PCA, clustering).
- Formalize conclusions and practical implications for sensor design.

## References
- Wang, Luthey-Schulten, Suslick, PNAS 2003, *"Colorimetric sensor arrays"*.

---
*This README is a living document and will be updated as the project evolves.*

