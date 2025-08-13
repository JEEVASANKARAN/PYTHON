import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Generate sample data
np.random.seed(0)
n_samples = 10
feature_1 = np.random.rand(n_samples, 1)
target = 3 * feature_1 + np.random.randn(n_samples, 1) * 0.1  # add noise

# Step 2: Create DataFrame and save to CSV
df = pd.DataFrame({
    'feature_1': feature_1.ravel(),
    'target': target.ravel()
})
csv_path = 'sample_data.csv'
df.to_csv(csv_path, index=False)

# Step 3: Load the CSV file
data = pd.read_csv(csv_path)
X = data[['feature_1']]  # 2D input for sklearn
y = data['target']

# Step 4: Fit linear regression model
lin_reg = LinearRegression()
lin_reg.fit(X, y)
y_pred = lin_reg.predict(X)

# Step 5: Plot results
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='black', label='Actual Data', alpha=0.7)
plt.plot(X, y_pred, color='red', label='Linear Regression Line')
plt.title('Linear Regression with Feature 1')
plt.xlabel('Feature 1')
plt.ylabel('Target')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
