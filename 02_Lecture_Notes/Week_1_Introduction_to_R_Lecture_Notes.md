# HSE 711 — Week 1: Introduction to R Lecture Notes

[Section index](README.md) · [Editable R Markdown](Week_1_Introduction_to_R_Lecture_Notes.Rmd) · [Repository home](../README.md)

> **Reading edition.** Code is displayed, not executed by this converter. The weekly teaching guides provide synthetic inputs and expected results; see each source for dependencies and execution checks.

## On this page

- [Purpose and learning objectives](#purpose-and-learning-objectives)
- [1. Understanding R objects before classifying them](#1-understanding-r-objects-before-classifying-them)
- [2. Comparing numbers safely, making factors, and locating positions](#2-comparing-numbers-safely-making-factors-and-locating-positions)
- [3. Importing a gene-by-sample expression table](#3-importing-a-gene-by-sample-expression-table)
- [4. Choosing one gene and reading its histogram](#4-choosing-one-gene-and-reading-its-histogram)
- [5. Selecting rows and columns, then exporting carefully](#5-selecting-rows-and-columns-then-exporting-carefully)
- [6. Writing a reusable categorization function](#6-writing-a-reusable-categorization-function)
- [7. Explaining your method, not just showing output](#7-explaining-your-method-not-just-showing-output)
- [8. Final self-check](#8-final-self-check)

## Purpose and learning objectives

These independent notes cover R objects, indexing, logical operations, tabular structures, data import, graphics, and reusable functions. They do not supply the official assignment, data, or graded implementation. To perform Geisel-specific coursework, consult the authorized lecture and assignment files in a private workspace.

**Required source boundary:** Readers need separately distributed Geisel instructional files to know the real assessed questions, schemas, and deliverables. Public sample code demonstrates general methods only.

## 1. Understanding R objects before classifying them

**Lecture idea:** R stores values inside named objects. `<-` assigns a value; `class()` describes an object's class. A list can contain different classes in separate elements, unlike an atomic vector.

```r
practice_list <- list(12, "alpha", TRUE, 2.5)

# Inspect one component; double brackets extract its contents.
class(practice_list[[1]])
class(practice_list[[2]])

# Revisit the loop syntax from the lecture.
practice_types <- character(length(practice_list))
for (i in seq_along(practice_list)) {
  practice_types[i] <- class(practice_list[[i]])
}
practice_types
table(practice_types)
```

**Why it works:** `seq_along()` supplies the positions of the list; `[[i]]` retrieves each underlying value; `class()` converts the observed class into a label. `table()` counts repeated labels. An alternative is `vapply(practice_list, class, character(1))` when each element has one class label.

**Checkpoint:** Explain why `class(practice_list)` alone is not an answer to the question about *each component*.

## 2. Comparing numbers safely, making factors, and locating positions

A comparison like `value > threshold` only makes sense if the value has a compatible type. An `if` statement executes only when the condition is a single TRUE or FALSE. `&&` is appropriate for a scalar short-circuit condition inside this loop.

```r
mixed_list <- list("north", 3, 11, "south", 7)
n_large <- 0L

for (value in mixed_list) {
  if (is.numeric(value) && length(value) == 1L &&
      !is.na(value) && value > 6) {
    n_large <- n_large + 1L
  }
}
n_large

# Categorical classes can be represented with a factor.
practice_factor <- factor(vapply(mixed_list, class, character(1)))
levels(practice_factor)

# which() gives one-based positions, not the matching values.
positions <- which(vapply(
  mixed_list,
  function(value) is.numeric(value) && length(value) == 1L &&
    !is.na(value) && value == 7,
  logical(1)
))
positions
```

**Why it works:** The type check protects the numeric comparison. `factor()` constructs category levels; `which()` converts TRUE entries of a logical vector to indices. R indices start at **1**, not 0.

**Checkpoint:** Change the search target and predict whether the result will contain zero, one, or multiple indices.

## 3. Importing a gene-by-sample expression table

**Lecture idea:** Inspect a data frame's structure *before* processing it. `read.delim()` reads tab-separated files. `header = TRUE` uses the top row for column labels; `row.names = 1` uses the first column for row identifiers. These are different options.

The illustrative code below is intentionally **not run**: the exercise's original clinical trial file is an independently supplied classroom input, not a public repository asset.

```r
input_path <- "data/your_local_expression_table.txt"
stopifnot(file.exists(input_path))

expression_df <- read.delim(
  file = input_path,
  header = TRUE,
  row.names = 1,
  check.names = FALSE
)

dim(expression_df)             # rows, columns together
nrow(expression_df)            # number of gene rows
ncol(expression_df)            # number of sample columns
head(rownames(expression_df))  # gene identifiers
head(colnames(expression_df))  # sample identifiers
str(expression_df)             # storage types
```

**Why it works:** Each gene is an observation along the row axis and each sample occupies a column in this file layout. `check.names = FALSE` avoids automatic renaming of sample identifiers. `head()` and `str()` help confirm the file was interpreted correctly.

**Checkpoint:** A table is sometimes oriented with samples in rows. How would you establish the actual orientation instead of assuming it?

## 4. Choosing one gene and reading its histogram

A histogram describes the **distribution of numeric values** for one selected gene across the samples. It displays how many values fall inside intervals; it does not identify patient-level clinical outcomes or establish treatment effects.

```r
# Small demonstration table, unrelated to the assigned trial.
toy_expression <- data.frame(
  sample_a = c(3, 12, 6),
  sample_b = c(7, 14, 9),
  sample_c = c(5, 11, 8),
  sample_d = c(6, 13, 7),
  row.names = c("gene_a", "gene_b", "gene_c")
)

gene_id <- "gene_b"
gene_values <- as.numeric(toy_expression[gene_id, ])

hist(
  gene_values,
  breaks = 3,
  main = paste("Distribution for", gene_id),
  xlab = "Expression value (illustrative units)",
  ylab = "Number of samples"
)
```

**Read the plot:** The horizontal axis is the measured expression value; the vertical axis counts samples in each interval. The number of bins affects appearance. A long tail suggests a few comparatively high observations, but a histogram alone does not explain their cause.

**Checkpoint:** Why must the selected row become a numeric vector before calling `hist()`?

## 5. Selecting rows and columns, then exporting carefully

R's two-dimensional syntax is `data[rows, columns]`. Always inspect the expected resulting dimensions before writing a file. `drop = FALSE` retains a table-like object even when one row or one column is selected.

```r
toy_sub <- toy_expression[1:2, 1:2, drop = FALSE]
dim(toy_sub)
rownames(toy_sub)
colnames(toy_sub)

# To export an independently created practice table:
# write.csv(toy_sub, file = "toy_sub.csv", row.names = TRUE)
```

**Checkpoint:** Why is `[1:2, 1:2]` not equivalent to `[1:2]`? How do row identifiers appear in the exported CSV?

## 6. Writing a reusable categorization function

**Lecture idea:** A function accepts an argument, performs the same logic consistently, and returns a result. The `if/else` branches belong **inside** the function, and the function is called only after it has been defined.

```r
group_measurements <- function(values, cutoff = 10) {
  lower <- numeric(0)
  higher <- numeric(0)

  for (value in values) {
    if (is.na(value)) {
      next
    } else if (value <= cutoff) {
      lower <- c(lower, value)
    } else {
      higher <- c(higher, value)
    }
  }

  list(
    at_or_below = sort(lower),
    above = sort(higher)
  )
}

practice_values <- c(14, 3, 8, 12, 5)
practice_result <- group_measurements(practice_values)
str(practice_result)
```

**Why it works:** The function parameter `values` is local to the function. `cutoff` has a default, so the same method can be tried with a different threshold. The returned list preserves both categories for later use. `next` explicitly skips missing values; for real analyses, the decision to omit missing values must be justified.

**Checkpoint:** Predict the output before changing the cutoff. What needs to change if the input contains strings instead of numeric values?

## 7. Explaining your method, not just showing output

For each independent practice activity, write one or two sentences answering: **What object did I start with? What did this function, loop, or index operation do? How did I check the result?** Distinguish a descriptive graph from an inferential result.

A useful repeatable workflow is: inspect the data, choose the operation, run a small test, verify dimensions or positions, and only then apply the method to the full input. Keep your own solutions and any classroom-restricted data in the appropriate private or submission location.

## 8. Final self-check

- Can I explain `class()`, `table()`, `factor()`, `which()`, and why the list requires component-wise inspection?
- Can I describe why `row.names = 1` is distinct from `header = TRUE`?
- Can I identify the gene and sample axes and confirm an export's dimensions?
- Can I explain each argument to `hist()` without claiming an unsupported biological finding?
- Can I trace a function call into its loop, branches, and return value?

**Related:** [Week 1 group-work walkthrough](../03_Group_Work/Week_1_Group_Work_Narrative_Walkthrough.md) · [R function sheet](../06_RESOURCES/R/EASY_FUNCTION_SHEET.md) · [Lecture index](README.md)
