# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# === Configuration ===
INPUT_CSV = "Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
OUTPUT_CSV = "cleaned_cicids_data.csv"

def clean_cicids_data(input_path, output_path):
    print("[*] Loading data...")
    df = pd.read_csv(input_path)

    print("[*] Cleaning column names...")
    df.columns = df.columns.str.strip()
    df = df.loc[:, ~df.columns.duplicated()]

    print("[*] Dropping non-informative columns...")
    nunique = df.nunique()
    non_informative_cols = nunique[nunique <= 1].index.tolist()
    df.drop(columns=non_informative_cols, inplace=True)

    print("[*] Converting labels to binary...")
    df['Label'] = df['Label'].apply(lambda x: 0 if x == 'BENIGN' else 1)

    print("[*] Removing NaN and infinite values...")
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)

    print(f"[*] Final shape: {df.shape}")
    print("[*] Saving cleaned data...")
    df.to_csv(output_path, index=False)
    print(f"[+] Cleaned data saved to '{output_path}'")

if __name__ == "__main__":
    clean_cicids_data(INPUT_CSV, OUTPUT_CSV)

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
def preprocess_data(df):
    X = df.drop('Label', axis=1)
    y = df['Label']

    # Encode categorical features if any
    for col in X.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])

    # Normalize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Build TensorFlow model
def build_model(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(input_dim,)),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model

def main():
    df = pd.read_csv("cleaned_cicids_data.csv")
    print("Preprocessing...")
    X_train, X_test, y_train, y_test = preprocess_data(df)

    print("Building model...")
    model = build_model(X_train.shape[1])

    print("Training model...")
    model.fit(X_train, y_train, epochs=10, batch_size=256, validation_split=0.2)

    print("Evaluating model...")
    y_pred = (model.predict(X_test) > 0.5).astype("int32")
    print(classification_report(y_test, y_pred))

    # Save model
    model.save("cicids_anomaly_model.h5")
    print("Model saved as cicids_anomaly_model.h5")

if __name__ == "__main__":
    main()

"""# New Section"""