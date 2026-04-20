from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def get_preprocessor_linear():
    """Preprocessor for Linear / Ridge (scaled + one‑hot)."""
    numerical_cols = ["temp", "hum", "windspeed", "hr_sin", "hr_cos", "mnth_sin", "mnth_cos"]
    ordinal_cols   = ["season", "weekday", "weathersit"]
    binary_cols    = ["holiday", "workingday", "yr"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical_cols),
            ("ord", OneHotEncoder(drop="first"), ordinal_cols),
            ("bin", "passthrough", binary_cols),
        ],
        remainder="drop"
    )
    return preprocessor


def get_preprocessor_tree():
    """Preprocessor for RandomForest (no scaling + label‑encoded ordinals)."""
    numerical_cols = ["temp", "hum", "windspeed", "hr_sin", "hr_cos", "mnth_sin", "mnth_cos"]
    ordinal_cols   = ["season", "weekday", "weathersit"]
    binary_cols    = ["holiday", "workingday", "yr"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", "passthrough", numerical_cols),
            ("ord", "passthrough", ordinal_cols),
            ("bin", "passthrough", binary_cols),
        ],
        remainder="drop"
    )
    return preprocessor

# comment out for debugging
"""
linear_pre = get_preprocessor_linear()
tree_pre = get_preprocessor_tree()

print("Linear preprocessor:", linear_pre)
print("Tree preprocessor:", tree_pre)
"""