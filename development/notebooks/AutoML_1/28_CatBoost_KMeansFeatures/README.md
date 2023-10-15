# Summary of 28_CatBoost_KMeansFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.05
- **depth**: 8
- **rsm**: 0.8
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

163.3 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.429186 | nan         |
| auc       | 0.791519 | nan         |
| f1        | 0.558465 |   0.286854  |
| accuracy  | 0.815169 |   0.512661  |
| precision | 0.793327 |   0.7875    |
| recall    | 1        |   0.0282969 |
| mcc       | 0.424466 |   0.337081  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.429186 |  nan        |
| auc       | 0.791519 |  nan        |
| f1        | 0.482516 |    0.512661 |
| accuracy  | 0.815169 |    0.512661 |
| precision | 0.660167 |    0.512661 |
| recall    | 0.380203 |    0.512661 |
| mcc       | 0.401213 |    0.512661 |


## Confusion matrix (at threshold=0.512661)
|                  |   Predicted as False |   Predicted as True |
|:-----------------|---------------------:|--------------------:|
| Labeled as False |                74185 |                4514 |
| Labeled as True  |                14295 |                8769 |

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
