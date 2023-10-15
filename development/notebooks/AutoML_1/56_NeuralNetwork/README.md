# Summary of 56_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 64
- **dense_2_size**: 16
- **learning_rate**: 0.01
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
auc

## Training time

279.6 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.432479 | nan           |
| auc       | 0.787653 | nan           |
| f1        | 0.557082 |   0.277519    |
| accuracy  | 0.814068 |   0.500413    |
| precision | 0.772424 |   0.732272    |
| recall    | 1        |   1.80315e-19 |
| mcc       | 0.421777 |   0.324823    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.432479 |  nan        |
| auc       | 0.787653 |  nan        |
| f1        | 0.479434 |    0.500413 |
| accuracy  | 0.814068 |    0.500413 |
| precision | 0.655951 |    0.500413 |
| recall    | 0.377775 |    0.500413 |
| mcc       | 0.397312 |    0.500413 |


## Confusion matrix (at threshold=0.500413)
|                  |   Predicted as False |   Predicted as True |
|:-----------------|---------------------:|--------------------:|
| Labeled as False |                74129 |                4570 |
| Labeled as True  |                14351 |                8713 |

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
