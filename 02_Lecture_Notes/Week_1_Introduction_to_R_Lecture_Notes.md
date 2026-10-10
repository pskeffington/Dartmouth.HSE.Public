# Paul's Notes · Week 1: R Objects and Expression Tables

[Section index](README.md) · [Editable R Markdown](Week_1_Introduction_to_R_Lecture_Notes.Rmd) · [Repository home](../README.md)

> **Reading edition.** Code is displayed, not executed by this converter. The teaching guides provide known practice inputs and expected results; see each source for dependencies and execution checks.

## On this page

- [Purpose and dependencies](#purpose-and-dependencies)
- [Objects, types, and scientific meaning](#objects-types-and-scientific-meaning)
- [Genes, specimens, and table orientation](#genes-specimens-and-table-orientation)
- [Selection, control flow, and input contracts](#selection-control-flow-and-input-contracts)
- [Misconceptions and self-check](#misconceptions-and-self-check)

## Purpose and dependencies

Use this conceptual reference after the [complete Week 1 lesson](../03_Group_Work/Week_1_Group_Work_Narrative_Walkthrough.md). **Study time:** 25–35 minutes. **Prerequisites:** basic arithmetic; base R only. Execute the small examples in order. Construct, inspect, and explain objects before choosing a summary.

## Objects, types, and scientific meaning

An atomic vector stores one type. A list can store different kinds of objects. A matrix is rectangular with a shared type; a data frame is a collection of equally long columns. A factor records category levels rather than a measured quantity.

| Inspect | Question answered |
| --- | --- |
| `typeof(x)` / `class(x)` | Storage representation / object behavior |
| `str(x)` | Structure, classes, representative values |
| `length(x)` | Elements, or columns for a data frame |
| `dim(x)` / `nrow(x)` / `ncol(x)` | Rectangular shape |
| `names(x)` | Named components or fields |

Type is not meaning: a numeric identifier is still an identifier, and a numeric survey code is not a concentration. Coercing character text cannot reconstruct an unavailable measurement.

```r
reference_sample <- list(Sample_ID = "R01", Gene = "Feature_X", Expression = 6.5, Observed = TRUE)
print(vapply(reference_sample, class, character(1)))
print(class(c(6.5, "unavailable")))
stopifnot(is.list(reference_sample["Expression"]), is.numeric(reference_sample[["Expression"]]))
```

**Expected:** character, character, numeric, logical component classes; the mixed atomic vector is character. `[ ]` preserves a list, while `[[ ]]` extracts a component.

## Genes, specimens, and table orientation

A gene is a feature; a specimen is the material sampled. A wide gene-by-sample table places genes in rows and specimens in columns. Long form has one gene–sample pair per row. Neither the gene count nor the total cell count automatically equals the number of people.

```r
reference_expression <- data.frame(R01 = c(6.5, 12), R02 = c(8, 11), R03 = c(NA, 14),
                                   row.names = c("Feature_X", "Feature_Y"))
selected_gene <- as.numeric(reference_expression["Feature_X", ])
print(c(genes = nrow(reference_expression), specimens = ncol(reference_expression)))
stopifnot(identical(dim(reference_expression), c(2L, 3L)))
stopifnot(sum(!is.na(selected_gene)) == 2L, mean(selected_gene, na.rm = TRUE) == 7.25)
```

**Expected:** two features, three specimens, two observed Feature_X values, mean 7.25 arbitrary simulated units. These values are neither count data nor a normalized assay. A missing value is not zero; report measured and total counts separately.

## Selection, control flow, and input contracts

`table[rows, columns]` selects two dimensions; `drop = FALSE` retains them. Positions start at one. `which()` gives positions of TRUE values. `&` / `|` are elementwise; `&&` / `||` are scalar short-circuit tests. An `if` requires one nonmissing decision. Use `seq_along()` for safe iteration, including empty inputs.

```r
observed_positions <- which(!is.na(selected_gene) & selected_gene > 7)
print(observed_positions)
one_gene_table <- reference_expression["Feature_X", , drop = FALSE]
stopifnot(identical(observed_positions, 2L), nrow(one_gene_table) == 1L)
```

**Expected:** position 2 and a one-row table. Comparisons to NA are unknown; use `is.na()`. A histogram bins observed numeric values and counts specimens, not treatment effects.

CSV/TSV import requires a separator, header, missing convention, and dictionary. `header = TRUE` names columns; `row.names = 1` instead consumes the first field as row labels. CSV does not preserve factors. `getwd()` explains relative paths, and a saved script records the steps. A function should check inputs and return a result rather than only printing it.

## Misconceptions and self-check

Explain why internal factor codes are not measurements, why the three specimen columns are not three genes, and why a mean from two observed values does not represent all three. Demonstrate logical selection and a dimension-preserving subset on new invented values. For loops, import/export, error handling, histograms, and practice, use the full lesson.

[Next topic](Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.md) · [Topic index](README.md) · [R extraction](https://stat.ethz.ch/R-manual/R-devel/library/base/html/Extract.html)
