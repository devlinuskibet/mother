import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

print("📂 Loading dataset...")
try:
    df = pd.read_csv("Dataset - Updated.csv")
except FileNotFoundError:
    print("❌ ERROR: File not found.")
    exit()

# 1. Clean Column Names (Strip spaces)
df.columns = df.columns.str.strip()
print(f"📊 Columns found: {list(df.columns)}")

# 2. Define Target (RiskLevel)
# We know your file uses 'RiskLevel' (no space)
target_col = 'RiskLevel'

if target_col not in df.columns:
    print(f"❌ CRITICAL: Could not find '{target_col}' column.")
    exit()

# 3. Clean Data
df_clean = df.dropna()
X = df_clean.drop(target_col, axis=1)
y = df_clean[target_col]

# 4. Define Features (Only the ones present in your file)
# Note: We removed BMI and Diabetes because they are missing from this file.
numerical_cols = ['Age', 'SystolicBP', 'DiastolicBP', 'BS', 'BodyTemp', 'HeartRate']

# 5. Setup Pipeline
# We only have numerical columns now, so we don't need the 'binary' section.
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols)
    ]
)

pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=200, random_state=42, class_weight='balanced'))
])

# 6. Train & Save
print("🔄 Training model on available features...")
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

pipeline.fit(X, y_encoded)

print("💾 Saving new model files...")
joblib.dump(pipeline, 'maternal_risk_pipeline.joblib')
joblib.dump(label_encoder, 'label_encoder.joblib')

print("✅ SUCCESS! Model trained on the 'Lite' dataset.")