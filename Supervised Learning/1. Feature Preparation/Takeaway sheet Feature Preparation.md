# Takeaway sheet: Feature Preparation

# Practice

```python
# One-hot-encoding: obtain dummy features
# drop_first = True - drop first column (avoiding dummy traps)

pd.get_dummies(df['column'])
pd.get_dummies(df['column'], drop_first_True)
```

```python
# Ordinal Encoding

from sklearn.preprocessing import OrdinalEncoder

encoder = OrdinalEncoder()
encoder.fit(data)
data_ordinal = encoder.transform(data)

# adding column names

data_ordinal = pd.DataFrame(encoder.transform(data), columns=data.columns)

# automated training and transforming
from sklearn.preprocessing import OrdinalEncoder

encoder = OrdinalEncoder()
data_ordinal = pd.DataFrame(encoder.fit_transform(data), columns=data.columns)

```

```python
# Standardizing

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(df)
df_scaled = scaler.transform(df)
```