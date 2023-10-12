# Binary-Classification-with-a-Software-Defects-Dataset

## Dataset Description
The dataset for this competition (both train and test) was generated from a deep learning model trained on the Software Defect Dataset. Feature distributions are close to, but not exactly the same, as the original. Feel free to use the original dataset as part of this competition, both to explore differences as well as to see whether incorporating the original in training improves model performance.

## Files
**train.csv** - the training dataset; defects is the binary target, which is treated as a boolean (False=0, True=1)
**test.csv** - the test dataset; your objective is to predict the probability of positive defects (i.e., defects=True)
**sample_submission.csv** - a sample submission file in the correct format

## Evaluation
Submissions are evaluated by Area Under the ROC Curve (AUC).

## Submission File Format
The submission file should be a csv file with two columns: id and predicted_probability. The id column should contain the id of each test example. The predicted_probability column should contain the probability that the corresponding id in the id column is a positive example.

## Submission
Submit your predictions to the leaderboard to see your score.

## Data Fields
id - an id that represents a test example
defects - whether a given test example is a defect or not (True=1, False=0)
time - the number of minutes it took to generate the test example
enhancements - the number of enhancement changes made to the test example
files - the number of files changed in the test example
lines - the number of lines changed in the test example
classes - the number of classes changed in the test example
methods - the number of methods changed in the test example
comments - the number of comments changed in the test example
complexity - the number of times the test example was flagged as having too-high complexity

## Acknowledgements
The Software Defect Prediction Dataset is based on the paper:

<NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>, <NAME>,