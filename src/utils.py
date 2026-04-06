# type: ignore
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


def get_preprocessor_linear():
    """Preprocessor for Linear / Ridge (scaled + one‑hot)."""
    numerical_cols = ["temp", "atemp", "hum", "windspeed"]
    ordinal_cols   = ["season", "mnth", "hr", "weekday", "weathersit"]
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
    numerical_cols = ["temp", "atemp", "hum", "windspeed"]
    ordinal_cols   = ["season", "mnth", "hr", "weekday", "weathersit"]
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