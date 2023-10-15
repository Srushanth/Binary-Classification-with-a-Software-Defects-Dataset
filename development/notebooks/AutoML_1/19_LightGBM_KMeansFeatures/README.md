# Summary of 19_LightGBM_KMeansFeatures

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **num_leaves**: 15
- **learning_rate**: 0.05
- **feature_fraction**: 0.8
- **bagging_fraction**: 0.5
- **min_data_in_leaf**: 50
- **metric**: auc
- **custom_eval_metric_name**: None
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
auc

## Training time

44.2 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.429084 | nan         |
| auc       | 0.791761 | nan         |
| f1        | 0.558546 |   0.287215  |
| accuracy  | 0.815002 |   0.484851  |
| precision | 0.81215  |   0.77227   |
| recall    | 1        |   0.0340987 |
| mcc       | 0.423447 |   0.339354  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.429084 |  nan        |
| auc       | 0.791761 |  nan        |
| f1        | 0.496146 |    0.484851 |
| accuracy  | 0.815002 |    0.484851 |
| precision | 0.648182 |    0.484851 |
| recall    | 0.401882 |    0.484851 |
| mcc       | 0.407127 |    0.484851 |


## Confusion matrix (at threshold=0.484851)
|                  |   Predicted as False |   Predicted as True |
|:-----------------|---------------------:|--------------------:|
| Labeled as False |                73668 |                5031 |
| Labeled as True  |                13795 |                9269 |

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
