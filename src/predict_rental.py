import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from math import sqrt

password = quote_plus('TU CONTRASEÑA')
engine = create_engine(f'mysql+mysqlconnector://root:{password}@localhost/sakila')

# Query con más features pa que aprenda mejor
query = """
SELECT
    f.film_id,
    f.title,
    f.rental_rate,
    f.length,
    f.replacement_cost,
    COUNT(r.rental_id) AS rental_count,
    c.name AS category,
    DAYNAME(r.rental_date) AS dia_semana,
    MONTHNAME(r.rental_date) AS mes,
    AVG(DATEDIFF(r.return_date, r.rental_date)) AS avg_rental_duration
FROM rental r
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE r.return_date IS NOT NULL
GROUP BY f.film_id, f.title, f.rental_rate, f.length, f.replacement_cost, c.name, dia_semana, mes;
"""

print("Conectando a MySQL...")
df = pd.read_sql(query, engine)
print(f"Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas")

df = pd.get_dummies(df, columns=['category', 'dia_semana', 'mes'], drop_first=True)
X = df.drop(['avg_rental_duration', 'film_id', 'title'], axis=1)
y = df['avg_rental_duration']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nEntrenando RandomForest...")
model = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

rmse = sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n" + "="*40)
print(f"RMSE: {rmse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R²: {r2:.4f}")
print("="*40)    , 
