import pandas as pd
import numpy as np

from sklearn import ensemble
from sklearn import model_selection


if __name__ == "__main__":
    df = pd.read_csv("../data/train.csv")
    X = df.drop(columns=["defects"]).values
    y = df["defects"].values

    clf = ensemble.RandomForestClassifier(n_jobs=-1)
    param_grid = {
        "n_estimators": np.arange(100, 1500, 100),
        "max_depth": np.arange(1, 20, 1),
        "criterion": ["gini", "entropy"]
    }

    model = model_selection.RandomizedSearchCV(
        estimator=clf,
        param_distributions=param_grid,
        n_iter=10,
        scoring="accuracy",
        n_jobs=-1,
        cv=5,
        verbose=10
    )

    model.fit(X, y)
    print(f"Best score: {model.best_score_}")
    print(f"Best params: {model.best_params_}")
    print(f"Best estimator: {model.best_estimator_}")
