import pandas as pd

from sklearn import ensemble
from sklearn import model_selection


if __name__ == "__main__":
    df = pd.read_csv("../data/train.csv")
    X = df.drop(columns=["defects"]).values
    y = df["defects"].values

    clf = ensemble.RandomForestClassifier(n_jobs=-1)
    param_grid = {
        "n_estimators": [100, 200, 300, 400, 500],
        "max_depth": [1, 3, 5, 7],
        "criterion": ["gini", "entropy"]
    }

    model = model_selection.GridSearchCV(
        estimator=clf,
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
