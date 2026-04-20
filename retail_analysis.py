import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import warnings

warnings.filterwarnings('ignore')

# Настройка стиля графиков
plt.style.use('seaborn-v0_8')

print("Step 1: Loading data...")

# 1. ЗАГРУЗКА ДАННЫХ
try:
    df = pd.read_csv('/home/nataly/online_retail.csv', encoding='utf-8', on_bad_lines='skip')
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns.")
    print(df.head())
except FileNotFoundError:
    print("Error: File not found. Please check the path '/home/nataly/online_retail.csv'")
    exit()

# 2. ОЧИСТКА ДАННЫХ
print("\nStep 2: Cleaning data...")

# Удаляем строки с отрицательным количеством (возвраты)
df = df[df['Quantity'] >= 0].copy()

# Удаляем пустые значения в важных колонках
df = df.dropna(subset=['Quantity', 'UnitPrice'])

print(f"Rows after cleaning: {len(df)}")

# 3. ПОДГОТОВКА ПЕРЕМЕННЫХ
# Создаем целевую переменную: High_Quantity (1 если Quantity > 10, иначе 0)
df['High_Quantity'] = (df['Quantity'] > 10).astype(int)

# Выбираем признаки (X) и цель (y)
features = ['Quantity', 'UnitPrice']
X = df[features]
y = df['High_Quantity']

print(f"Features used: {features}")
print(f"Target distribution:\n{y.value_counts()}")

# 4. РАЗДЕЛЕНИЕ ДАННЫХ (70% тренировка, 30% тест)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
print(f"Training set size: {len(X_train)}")
print(f"Test set size: {len(X_test)}")

# 5. ОБУЧЕНИЕ МОДЕЛИ (Random Forest)
print("\nStep 5: Training Random Forest model...")
model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)
print("Training complete.")

# 6. ОЦЕНКА МОДЕЛИ
print("\nStep 6: Evaluating model...")
y_pred = model.predict(X_test)

accuracy = accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 7. ВИЗУАЛИЗАЦИЯ РЕЗУЛЬТАТОВ
print("\nStep 7: Generating charts...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 7.1 Матрица ошибок
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[0,0])
axes[0,0].set_title('Confusion Matrix')
axes[0,0].set_xlabel('Predicted')
axes[0,0].set_ylabel('Actual')

# 7.2 Важность признаков
feature_importance = pd.DataFrame({
    'feature': features,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=True)

axes[0,1].barh(feature_importance['feature'], feature_importance['importance'])
axes[0,1].set_title('Feature Importance')

# 7.3 Распределение целевой переменной
y.value_counts().plot(kind='pie', ax=axes[1,0], autopct='%1.1f%%')
axes[1,0].set_title('Distribution of High Quantity Orders')

# 7.4 Scatter Plot
axes[1,1].scatter(df['Quantity'], df['UnitPrice'], c=df['High_Quantity'], alpha=0.5)
axes[1,1].set_title('Quantity vs UnitPrice')
axes[1,1].set_xlabel('Quantity')
axes[1,1].set_ylabel('UnitPrice')

plt.tight_layout()

# Сохранение графика
output_image_path = '/home/nataly/retail_analysis_report.png'
plt.savefig(output_image_path, dpi=300, bbox_inches='tight')
print(f"Charts saved to: {output_image_path}")

# 8. СОХРАНЕНИЕ МЕТРИК В ФАЙЛ
results_df = pd.DataFrame({
    'Accuracy': [accuracy],
    'Model': ['Random Forest'],
    'Train_Size': [len(X_train)],
    'Test_Size': [len(X_test)]
})

output_csv_path = '/home/nataly/model_results.csv'
results_df.to_csv(output_csv_path, index=False)
print(f"Metrics saved to: {output_csv_path}")

print("\nAnalysis finished successfully.")