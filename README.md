# Binary-Classification-with-a-Software-Defects-Dataset

## Dataset Description
The dataset for this competition (both train and test) was generated from a deep learning model trained on the Software Defect Dataset. Feature distributions are close to, but not exactly the same, as the original. Feel free to use the original dataset as part of this competition, both to explore differences as well as to see whether incorporating the original in training improves model performance.

## Files
**train.csv** - the training dataset; defects is the binary target, which is treated as a boolean (False=0, True=1)
**test.csv** - the test dataset; your objective is to predict the probability of positive defects (i.e., defects=True)
**sample_submission.csv** - a sample submission file in the correct format