# Lecture Notes

Narrative teaching companions for **HSE 711: Foundations in Data Science**. Each document explains the motivation for a method, how the code operates and what can reasonably be concluded. These are independent study notes, not official lecture handouts.

## File naming convention

Use `Week_<number>_<Topic>_<Purpose>.<extension>` for lecture materials. Separate words with underscores, use the same stem for the editable source and generated reading edition, and avoid assignment-specific words in filenames.

- `Week_1_Introduction_to_R_Lecture_Notes.Rmd` and `.md`: primary student-facing notes
- `Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.Rmd` and `.md`: same role in later weeks
- `Week_2_Data_Wrangling_and_Visualization_Lecture_Reference.R` and `.md`: supplemental chunk-by-chunk reference

**Purpose suffixes:** `Lecture_Notes` means the guided, mastery-based lesson; `Lecture_Reference` means the detailed, comment-only transcript companion. Keep group-work and assignment filenames in their own folders. Update all local links together when renaming a file, and regenerate reading editions with `python3 06_RESOURCES/Presentation/build_reading_editions.py --check`.

## Available lessons

| Week | Topic | Material |
| --- | --- | --- |
| 1 | Introduction to R: methods for approaching Assignment 1 | [Lecture notes (read)](Week_1_Introduction_to_R_Lecture_Notes.md) |
| 2 | Data wrangling and visualization | [Methods + mastery](Week_2_Data_Wrangling_and_Visualization_Lecture_Notes.md) · [44-chunk reference](Week_2_Data_Wrangling_and_Visualization_Lecture_Reference.md) |
| 3 | Data visualization and analytics | [Methods + mastery](Week_3_Data_Visualization_and_Analytics_Lecture_Notes.md) · [21-chunk reference](Week_3_Data_Visualization_and_Analytics_Lecture_Reference.md) |
| 4 | Introduction to Bash scripting | [Methods + mastery](Week_4_Introduction_to_Bash_Lecture_Notes.md) |

**Reading the files:** The links above open formatted Markdown reading editions. Each edition links to its original `.R` or `.Rmd` source. Week 2 and Week 3 `.R` files are comment-only chunk-by-chunk references; the new `.Rmd` methods guides contain executable independent practice examples and weekly mastery standards. `.Rmd` walkthroughs can be opened in RStudio and knitted with their packages and local inputs.

[Follow-along guide](../FOLLOW_ALONG.md) · [R function sheet](../06_RESOURCES/R/EASY_FUNCTION_SHEET.md) · [Bash command sheet](../06_RESOURCES/Bash/EASY_COMMAND_SHEET.md)

## Related resources

The [Week 4 Bash operation sheet](../06_RESOURCES/Bash/BASH_OPERATION_SHEET.md) provides an annotated command reference. The [APA 7 student manuscript template](../06_RESOURCES/LaTeX/) supports a formatted student learning report. The [summary statistics guide](../06_RESOURCES/SUMMARY_STATISTICS.md) covers mean, standard deviation, quartiles, IQR, missingness and automatically generated narrative interpretation.

For lectures requiring data files, first confirm that the local `data/` directory contains the relevant classroom inputs. Do not commit those inputs to this public repository.
