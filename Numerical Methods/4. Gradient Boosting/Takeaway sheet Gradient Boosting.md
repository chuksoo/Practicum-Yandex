# Takeaway sheet: Gradient Boosting

**Practice**

```python
# CatBoost classifier training
# cat_features - list of categorical features
from catboost import CatBoostClassifier

model = CatBoostClassifier(loss_function="Logloss", iterations=50)
model.fit(features_train, target_train, cat_features=cat_features, verbose=10)
```

**Theory**

**Ensemble** is a set of models for solving the same problem. The strength of ensembles is that the mean error of a group of models is less significant than their individual errors.

**Boosting** is an approach to ensemble building where each subsequent model takes into account the errors of the previous one and, in the final prediction, the forecasts of basic learners.