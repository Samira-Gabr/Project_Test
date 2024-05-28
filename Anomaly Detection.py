#Develop an anomaly detection model using historical data.
from sklearn.ensemble import IsolationForest
import numpy as np

# Example data: features might include login times, file access frequency, etc.
data = np.array([[1, 200], [2, 220], [3, 210], [10, 1000], [4, 215], [5, 230]])
model = IsolationForest(contamination=0.1)
model.fit(data)

# Predict anomalies
anomalies = model.predict(data)
print("Anomalies detected:", anomalies)

