import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

def build_classifier(args):
    # Read CSV file
    df = pd.read_csv(args.csv)
    
    # Ignore specified columns
    if args.ignore_cols:
        df = df.drop(columns=args.ignore_cols, errors='ignore')
    
    # Convert categorical columns to one-hot encoding
    categorical_cols = df.select_dtypes(include=['object']).columns
    if len(categorical_cols) > 0:
        df = pd.get_dummies(df, columns=categorical_cols)
    
    # Encode target column
    label_encoder = LabelEncoder()
    df[args.target_col] = label_encoder.fit_transform(df[args.target_col])
    
    # Split data into features and target
    X = df.drop(columns=[args.target_col])
    y = df[args.target_col]
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Choose classifier model
    if args.model == "svm":  # <== We are able to pick the right model or 'strategy' at runtime
        clf = SVC()
    elif args.model == "logreg":
        clf = LogisticRegression()
    
    # Train classifier
    clf.fit(X_train, y_train) # <== This code is the same, svm or logreg
    
    # Predict on test set
    y_pred = clf.predict(X_test) # <== This code is the same, svm or logreg
    
    # Calculate confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    
    return cm

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build a classifier")
    parser.add_argument("--model", choices=["svm", "logreg"], required=True, help="Type of classifier model")
    parser.add_argument("--csv", required=True, help="CSV input file")
    parser.add_argument("--target-col", required=True, help="Target column name")
    parser.add_argument("--ignore-cols", nargs='+', default=[], help="Columns to ignore")
    
    args = parser.parse_args()
    confusion_matrix = build_classifier(args)
    print("Confusion Matrix:")
    print(confusion_matrix)
