import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Cargar los datos
data = pd.read_csv('data/funnel_data.csv')

# Limpieza básica
data.dropna(inplace=True)

# Análisis exploratorio
stage_counts = data['stage'].value_counts()
print(stage_counts)

# Visualización del funnel
sns.countplot(data['stage'], order=stage_counts.index)
plt.title('Funnel de Ventas - Spotify Ads')
plt.xlabel('Etapa del Funnel')
plt.ylabel('Número de Oportunidades')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Modelo predictivo: ¿se cerrará esta oportunidad?
X = pd.get_dummies(data[['stage', 'region']], drop_first=True)
y = data['won']  # 1 si ganó, 0 si no

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
