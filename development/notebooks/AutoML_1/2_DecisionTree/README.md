# Summary of 2_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: gini
- **max_depth**: 4
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
auc

## Training time

16.5 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.433397 |  nan        |
| auc       | 0.783386 |  nan        |
| f1        | 0.553159 |    0.264769 |
| accuracy  | 0.813105 |    0.509901 |
| precision | 0.791818 |    0.698781 |
| recall    | 1        |    0.054456 |
| mcc       | 0.417927 |    0.346919 |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.433397 |  nan        |
| auc       | 0.783386 |  nan        |
| f1        | 0.476104 |    0.509901 |
| accuracy  | 0.813105 |    0.509901 |
| precision | 0.652768 |    0.509901 |
| recall    | 0.374696 |    0.509901 |
| mcc       | 0.393615 |    0.509901 |


## Confusion matrix (at threshold=0.509901)
|                  |   Predicted as False |   Predicted as True |
|:-----------------|---------------------:|--------------------:|
| Labeled as False |                74102 |                4597 |
| Labeled as True  |                14422 |                8642 |

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
