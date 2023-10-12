import pandas as pd
import numpy as np

from sklearn import ensemble
from sklearn import model_selection
from sklearn import preprocessing
from sklearn import decomposition
from sklearn import pipeline


if __name__ == "__main__":
    df = pd.read_csv("../data/train.csv")
    X = df.drop(columns=["defects"]).values
    y = df["defects"].values

    ss = preprocessing.StandardScaler()
    pca = decomposition.PCA()
    clf = ensemble.RandomForestClassifier(n_jobs=-1)

    pl = pipeline.Pipeline(
        [
            ("ss", ss),
            ("pca", pca),
            ("clf", clf)
        ]
    )

    param_grid = {
        "pca__n_components": np.arange(2, 20, 1),
        "clf__n_estimators": np.arange(100, 1500, 100),
        "clf__max_depth": np.arange(1, 20, 1),
        "clf__criterion": ["gini", "entropy"]
    }

    model = model_selection.GridSearchCV(
        estimator=pl,
        param_grid=param_grid,
        scoring="accuracy",
        n_jobs=-1,
        cv=5,
        verbose=10
    )

    model.fit(X, y)
    print(f"Best score: {model.best_score_}")
    print(f"Best params: {model.best_params_}")
    print(f"Best estimator: {model.best_estimator_}")
