# Summary of 62_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 8
- **rsm**: 0.9
- **loss_function**: Logloss
- **eval_metric**: AUC
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
auc

## Training time

78.9 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.429247 | nan         |
| auc       | 0.791969 | nan         |
| f1        | 0.558253 |   0.309343  |
| accuracy  | 0.81454  |   0.512832  |
| precision | 0.783874 |   0.773924  |
| recall    | 1        |   0.0231646 |
| mcc       | 0.424508 |   0.322452  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.429247 |  nan        |
| auc       | 0.791969 |  nan        |
| f1        | 0.480755 |    0.512832 |
| accuracy  | 0.81454  |    0.512832 |
| precision | 0.657758 |    0.512832 |
| recall    | 0.378815 |    0.512832 |
| mcc       | 0.398984 |    0.512832 |


## Confusion matrix (at threshold=0.512832)
|                  |   Predicted as False |   Predicted as True |
|:-----------------|---------------------:|--------------------:|
| Labeled as False |                74153 |                4546 |
| Labeled as True  |                14327 |                8737 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)
