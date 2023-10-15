# Summary of 68_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **num_leaves**: 31
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

28.4 seconds

## Metric details
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.429641 | nan         |
| auc       | 0.791207 | nan         |
| f1        | 0.559336 |   0.276     |
| accuracy  | 0.814628 |   0.475293  |
| precision | 0.800557 |   0.777056  |
| recall    | 1        |   0.0264018 |
| mcc       | 0.423673 |   0.333483  |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.429641 |  nan        |
| auc       | 0.791207 |  nan        |
| f1        | 0.495129 |    0.475293 |
| accuracy  | 0.814628 |    0.475293 |
| precision | 0.646853 |    0.475293 |
| recall    | 0.401058 |    0.475293 |
| mcc       | 0.405844 |    0.475293 |


## Confusion matrix (at threshold=0.475293)
|                  |   Predicted as False |   Predicted as True |
|:-----------------|---------------------:|--------------------:|
| Labeled as False |                73649 |                5050 |
| Labeled as True  |                13814 |                9250 |

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
