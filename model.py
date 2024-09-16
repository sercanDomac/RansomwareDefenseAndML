import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

def train_model(data_path):
    # Veriyi yükle
    df = pd.read_csv(data_path)
    X = df[['feature1', 'feature2']]  # Özellikler
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Modeli eğit
    model = IsolationForest(contamination=0.01)
    model.fit(X_scaled)
    
    return model, scaler

def detect_anomalies(model, scaler, data_path):
    df = pd.read_csv(data_path)
    X = df[['feature1', 'feature2']]
    X_scaled = scaler.transform(X)
    
    predictions = model.predict(X_scaled)
    anomalies = df[predictions == -1]
    
    print(f"Anomali tespit edilen kayıtlar:\n{anomalies}")

if __name__ == "__main__":
    model, scaler = train_model('network_traffic.csv')
    detect_anomalies(model, scaler, 'network_traffic_test.csv')
