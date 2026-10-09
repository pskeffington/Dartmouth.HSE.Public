# Read a plot and explain what it shows

[Resource index](README.md) · [R function sheet](R/EASY_FUNCTION_SHEET.md) · [Follow-along guide](../FOLLOW_ALONG.md)

Begin with the question, then identify the observations, axes, units and groups. Describe the visible pattern before interpreting a statistical test. The descriptions below explain plot types used in the learning material; they are not computed results from the course data.

## Distribution and comparison plots

| Plot | What to read | A useful sentence | Check before concluding |
| --- | --- | --- | --- |
| Histogram | Horizontal intervals are value ranges; bar heights count observations unless the axis states density. | “Most observations fall in ___, with a tail extending toward ___.” | Bin width can change the apparent shape. Check units and missing values. |
| Box plot with points | The center line is the median; the box covers the middle half of values. Points show individual observations. | “Group ___ has a higher median, while the points show ___ overlap.” | In the ggplot defaults used here, whiskers extend to the most extreme values within 1.5 interquartile ranges of the box. Points beyond them are not automatically errors. |
| Violin plot | Width represents estimated density at a value, rather than an individual count. | “The distribution is concentrated around ___ and appears ___.” | Shape depends on smoothing and sample size. Width does not necessarily compare group sizes. |
| Empirical cumulative distribution | The vertical axis gives the fraction at or below a horizontal value. | “At ___, approximately ___ of this sample is at or below that threshold.” | Read the plotted axis scale: it may use fractions or percentages. |
| Scatter plot | Each point is one observation; axes show two measurements. Color and shape may identify groups. | “As ___ increases, ___ tends to ___, with ___ scatter around the pattern.” | Association does not establish causation. Check for outliers, clusters and repeated observations. |

## Multivariable and gene-expression plots

| Plot | What to read | Check before concluding |
| --- | --- | --- |
| Heatmap | Rows and columns identify features and samples; the legend maps numeric values to color. Clusters group similar patterns under the chosen method. | Match sample IDs to metadata and state the scale: raw counts, transformed expression or row-standardized values. Row-standardized colors describe relative values within genes. |
| Principal component plot | Points locate samples on components summarizing variation in the input matrix. Axis labels may show the variance explained. | Separation depends on preprocessing and feature selection; it does not itself validate a classifier or identify a cause. |
| Volcano plot | Horizontal position shows an effect such as log-fold change; vertical position often shows a negative log p-value or adjusted p-value. | Read the actual labels and thresholds. Counts, the fitted model and multiple-testing choices determine the inference; plotted prominence alone does not establish biological importance. |

## Explain a line, a band or a p-value

In the reusable scatter functions, an optional straight line is a least-squares fit. With grouped points, `plt_scatter(fit = TRUE)` fits **one pooled line**. Its shaded confidence band describes uncertainty in the estimated mean response; it does not contain a fixed percentage of individual observations.

The one-call statistical functions calculate a separate test result. A correlation p-value concerns evidence against the test's null hypothesis; it is not the slope, strength of association or probability that the hypothesis is true. A Wilcoxon comparison concerns ranks; interpreting it as a median comparison requires additional distributional assumptions. Report the effect or descriptive difference, sample sizes and study design alongside the test.

## Short narration template

“This figure compares **[measure]** across **[groups]** using **[input / simulated dataset]**. The horizontal axis shows **[variable and unit]**, and the vertical axis shows **[variable and unit]**. Each **[point / bar / box]** represents **[meaning]**. The main visible pattern is **[observation after running the code]**. We checked **[missingness / group sizes / scale]** before interpreting it. This supports **[limited description]**; further inference depends on **[design or model]**.”

If the inputs are unavailable or the code has not run, explain what the figure is intended to display and leave the result unfilled.
