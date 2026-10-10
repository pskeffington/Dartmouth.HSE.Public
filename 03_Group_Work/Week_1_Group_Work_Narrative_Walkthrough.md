# Paul's Notes · Week 1: R Foundations

[Section index](README.md) · [Editable R Markdown](Week_1_Group_Work_Narrative_Walkthrough.Rmd) · [Repository home](../README.md)

> **Reading edition.** Code is displayed, not executed by this converter. The weekly teaching guides provide synthetic inputs and expected results; see each source for dependencies and execution checks.

This study guide uses invented paper-glider trials to practise R objects, indexing, import, plotting, and functions.

**Study time:** 75–100 minutes, including practice. **Prerequisites:** R installed, a console or script editor, and basic arithmetic. No add-on packages are required. Run the code blocks in order in a fresh R session; the Markdown edition displays code and expected results without executing them.

## On this page

- [Learning objectives](#learning-objectives)
- [1. Names, assignment, and atomic vectors](#1-names-assignment-and-atomic-vectors)
- [2. Selection and missing values](#2-selection-and-missing-values)
- [3. Lists, matrices, data frames, and factors](#3-lists-matrices-data-frames-and-factors)
- [4. Decisions, iteration, and functions](#4-decisions-iteration-and-functions)
- [5. Import, export, and reproducibility](#5-import-export-and-reproducibility)
- [6. A histogram is a distribution summary](#6-a-histogram-is-a-distribution-summary)
- [Common mistakes and debugging](#common-mistakes-and-debugging)
- [Independent practice](#independent-practice)
- [Teach-back and summary](#teach-back-and-summary)
- [Next steps and references](#next-steps-and-references)

## Learning objectives

By the end, you should be able to choose an object structure, inspect its type and dimensions, select values safely, handle missingness, write a checked function, and explain a histogram. You will also import and export a small table without needing an external dataset.

## 1. Names, assignment, and atomic vectors

R evaluates an expression and returns a value. Assignment with `<-` gives that value a reusable name. Names are case-sensitive: `glide_m` and `Glide_m` would be different objects. A comment starts with `#`; it explains the script without changing the calculation.

```r
glide_m <- c(2.4, 3.1, NA_real_, 2.8, 3.7, 3.0)
trial_id <- paste0("g", seq_along(glide_m))
length(glide_m)
typeof(glide_m)
class(glide_m)
stopifnot(length(glide_m) == 6L, is.double(glide_m))
```

**Expected:** length `6`, storage type `"double"`, and class `"numeric"`. `c()` combines values. `NA_real_` marks an unavailable numeric measurement; it is not zero. Storage type describes representation, while class helps determine how R handles an object.

An atomic vector has one common type. Common types include logical (`TRUE`/`FALSE`), integer (`4L`), double (`4.2`), and character (`"paper"`). Combining numbers with text coerces them to characters rather than creating mixed numeric/text elements:

```r
mixed_vector <- c(2.4, "unrecorded")
print(mixed_vector)
stopifnot(is.character(mixed_vector))
```

**Expected:** `"2.4" "unrecorded"`. A mathematical summary now needs a deliberate cleaning decision, not blind conversion. `as.numeric("unrecorded")` cannot recover a measurement and produces missingness with a warning. Store missing numeric values as `NA`, and explanations in a separate column.

## 2. Selection and missing values

R positions begin at one. Brackets select by position, logical condition, or name. A logical selection asks one yes/no question per element. An unknown answer can propagate into the selection, so test missingness explicitly.

```r
names(glide_m) <- trial_id
print(glide_m[c(1, 4)])
print(glide_m["g5"])
usable <- !is.na(glide_m)
long_glides <- glide_m[usable & glide_m > 3]
print(long_glides)
print(glide_m[0])
stopifnot(identical(unname(long_glides), c(3.1, 3.7)))
stopifnot(length(glide_m[0]) == 0L, sum(is.na(glide_m)) == 1L)
```

**Expected:** positions 1 and 4 give `2.4` and `2.8`; named selection `g5` gives `3.7`. The filtered values are `3.1` and `3.7`. Index zero returns an empty selection, not the first value. Missing values are tested with `is.na()`, never `x == NA`, which itself gives unknown comparisons.

```r
print(mean(glide_m))
print(mean(glide_m, na.rm = TRUE))
stopifnot(is.na(mean(glide_m)))
stopifnot(isTRUE(all.equal(mean(glide_m, na.rm = TRUE), 3)))
```

**Expected:** the unqualified mean is `NA`; the available-case mean is `3` metres from five measured trials. Removing missing values changes the denominator. Report both the total number of trials and the number measured, and investigate why a measurement was unavailable.

## 3. Lists, matrices, data frames, and factors

A list can hold heterogeneous components. Single brackets retain a list; double brackets extract one component. A matrix is a rectangular atomic object with a shared type. A data frame stores columns of different types, with the same number of rows in each column.

```r
trial_bundle <- list(label = "paper glider", distance = glide_m, measured = usable)
stopifnot(is.list(trial_bundle["distance"]))
stopifnot(is.numeric(trial_bundle[["distance"]]))
launch_grid <- matrix(c(1, 2, 3, 4, 5, 6), nrow = 2, byrow = TRUE)
print(launch_grid)
trials <- data.frame(
  trial = trial_id,
  fold = factor(c("wide", "narrow", "wide", "narrow", "wide", "narrow"),
                levels = c("narrow", "wide")),
  metres = unname(glide_m)
)
str(trials)
print(dim(trials))
stopifnot(nrow(trials) == 6L, ncol(trials) == 3L)
stopifnot(identical(levels(trials$fold), c("narrow", "wide")))
```

**Expected:** a 2-by-3 matrix with first row `1 2 3`; a six-row, three-column data frame containing character identifiers, a two-level factor, and numeric distances. `str()` shows classes and representative values; `dim()`, `nrow()`, and `ncol()` show shape. `names(trials)` shows column names.

A factor represents a category with declared levels. Level order controls display order; it does not mean the labels have a numeric distance between them. `as.numeric(trials$fold)` yields internal codes, not measured fold widths. Use meaningful labels, and check for unexpected labels before converting: labels outside supplied levels become `NA`.

```r
print(trials[1:2, c("trial", "metres")])
metres_column <- trials[, "metres"]
metres_table <- trials[, "metres", drop = FALSE]
stopifnot(is.numeric(metres_column), is.data.frame(metres_table))
stopifnot(identical(dim(metres_table), c(6L, 1L)))
```

**Expected:** the first two trial-distance pairs are `g1, 2.4` and `g2, 3.1`. Selecting a single column normally drops the table structure; `drop = FALSE` preserves a six-by-one data frame. In `table[rows, columns]`, the comma separates row and column selection; `table[columns]` selects columns as a data frame.

## 4. Decisions, iteration, and functions

`if` chooses a branch using one nonmissing logical value. A vector comparison is not a suitable `if` condition; summarize it first, or use vector operations. A loop repeats an action and is useful when you need a clearly controlled sequence.

```r
if (sum(usable) >= 4L) {
  message("Enough available trials for this descriptive exercise")
} else {
  message("Collect more practice measurements")
}
centred_m <- numeric(length(glide_m))
for (j in seq_along(glide_m)) {
  centred_m[j] <- glide_m[j] - mean(glide_m, na.rm = TRUE)
}
stopifnot(isTRUE(all.equal(unname(centred_m), unname(glide_m - 3))))
print(round(centred_m, 1))
```

**Expected:** the first message, then deviations `-0.6, 0.1, NA, -0.2, 0.7, 0.0`. Subtraction propagates missingness. The vectorized expression `glide_m - 3` does the same work here with less code. `seq_along()` safely produces an empty sequence for an empty vector; `1:length(x)` does not.

A function turns a calculation into a named operation with explicit inputs and a return value. Validation makes errors understandable at the boundary. Returning a value allows later use; printing alone should not be your data interface.

```r
measured_mean <- function(values) {
  if (!is.numeric(values)) stop("values must be numeric")
  if (all(is.na(values))) stop("at least one measurement is needed")
  return(mean(values, na.rm = TRUE))
}
print(measured_mean(glide_m))
rejected_text <- tryCatch(measured_mean("far"), error = function(e) conditionMessage(e))
print(rejected_text)
stopifnot(measured_mean(glide_m) == 3)
stopifnot(identical(rejected_text, "values must be numeric"))
```

**Expected:** `3`, then `"values must be numeric"`. The caught error is an intentional demonstration, not an unsuccessful lesson run. Before generalizing this function, decide how to handle infinite values, units, and a minimum sample size.

## 5. Import, export, and reproducibility

A text table needs a separator, column names, missing-value conventions, and a known row unit. Inspect those choices after import. This exercise writes only a temporary file created from the synthetic table and deletes it after reading.

```r
glider_file <- tempfile(fileext = ".csv")
write.csv(trials, glider_file, row.names = FALSE, na = "NA")
reloaded <- read.csv(glider_file, na.strings = "NA", stringsAsFactors = FALSE)
unlink(glider_file)
stopifnot(identical(names(reloaded), names(trials)))
stopifnot(nrow(reloaded) == 6L, sum(is.na(reloaded$metres)) == 1L)
stopifnot(isTRUE(all.equal(reloaded$metres, trials$metres)))
print(sapply(reloaded, class))
```

**Expected:** `trial` and `fold` are characters; `metres` is numeric. CSV does not preserve R factor levels, so explicitly recreate them when needed. `row.names = FALSE` avoids an unintended extra index column. In real work, use a documented relative path, keep raw data unchanged, check units and schema, and record software versions.

## 6. A histogram is a distribution summary

A histogram groups measurements into intervals. Its horizontal axis has measurement units; its vertical axis here counts measured trials, not percentages or people. Break choices can change the visual impression, especially with five observations.

```r
glide_hist <- hist(trials$metres, breaks = c(2, 2.5, 3, 3.5, 4),
                   main = "Five invented glider measurements",
                   xlab = "Flight distance (m)", ylab = "Measured trials",
                   col = "lightblue", right = FALSE)
print(glide_hist$counts)
stopifnot(identical(glide_hist$counts, c(1L, 1L, 2L, 1L)))
```

**Expected:** counts `1, 1, 2, 1`. With these left-closed intervals, a value of `3.0` belongs to the interval starting at `3.0`. The plot shows where this tiny set of invented values falls; it does not demonstrate a population distribution or evidence that one fold design is better.

## Common mistakes and debugging

- **Object not found:** run the defining block first; check capitalization and spelling.
- **Arithmetic on text:** inspect `str()` before calculating; do not replace unparseable text with zero.
- **Unexpected missing result:** count `is.na()` and state the denominator before using `na.rm`.
- **Subscript out of bounds:** inspect dimensions; remember one-based positions and the row/column comma.
- **A table became a vector:** preserve dimensions with `drop = FALSE` when later code expects a table.
- **An `if` condition is missing or has several values:** decide whether you need one summary decision or a vectorized calculation.

## Independent practice

1. Create eight invented distances with two missing values. Select values above a threshold without including unknown entries, and report the available count.
2. Add a launch-category factor with three explicit levels. Show a two-column data frame without dropping dimensions.
3. Extend `measured_mean()` to reject infinite values. Test a valid vector, all-missing input, and text input using `tryCatch()`.
4. Draw the same measurements with two different break sets. Explain why the bars change while the data do not.

## Teach-back and summary

Explain why a list can store mixed components but an atomic vector coerces types. Why does `NA` differ from zero? What information does a CSV round trip lose? What would you check before treating a graph as evidence?

The practical sequence is **construct → inspect → select → validate → summarize → explain**. Structure, missingness, and explicit assumptions matter more than memorizing function names.

## Next steps and references

[Next: Week 2](Week_2_Group_Work_Narrative_Walkthrough.md) · [Weekly lessons](README.md) · [R topic companion](../02_Lecture_Notes/Week_1_Introduction_to_R_Lecture_Notes.md) · [R function sheet](../06_RESOURCES/R/EASY_FUNCTION_SHEET.md) · [Paul's Notes](../README.md)

Reference: [R object extraction documentation](https://stat.ethz.ch/R-manual/R-devel/library/base/html/Extract.html). See also `?factor`, `?read.table`, and `?hist` in your installed R version.
