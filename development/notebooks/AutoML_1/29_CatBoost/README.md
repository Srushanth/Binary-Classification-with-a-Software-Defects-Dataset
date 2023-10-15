# Summary of 29_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 8
- **rsm**: 1.0
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

56.7 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.429217 | nan         |
| auc       | 0.792061 | nan         |
| f1        | 0.558586 |   0.286819  |
| accuracy  | 0.815188 |   0.513692  |
| precision | 0.791985 |   0.775328  |
| recall    | 1        |   0.0198592 |
| mcc       | 0.4239   |   0.336016  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.429217 |  nan        |
| auc       | 0.792061 |  nan        |
| f1        | 0.482571 |    0.513692 |
| accuracy  | 0.815188 |    0.513692 |
| precision | 0.660242 |    0.513692 |
| recall    | 0.380246 |    0.513692 |
| mcc       | 0.401283 |    0.513692 |


## Confusion matrix (at threshold=0.513692)
|                  |   Predicted as False |   Predicted as True |
|:-----------------|---------------------:|--------------------:|
| Labeled as False |                74186 |                4513 |
| Labeled as True  |                14294 |                8770 |

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
