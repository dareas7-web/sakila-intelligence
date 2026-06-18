# Sakila Intelligence 🎬

Análisis + Machine Learning con la base de datos Sakila de MySQL. 
Proyecto end-to-end: ETL → Modelado → Predicción de renta de películas.

### **Qué hace**
Predice `duration_days` = días que un cliente se queda una película rentada, 
usando features de `film`, `inventory` y `rental`.

### **Stack usado**
- **Python**: pandas, scikit-learn 
- **Base de datos**: MySQL + Sakila sample DB
- **Modelo**: RandomForestRegressor
- **Dashboard**: Streamlit `dashboard/app.py`

### **Métricas actuales**
| Métrica | Valor |
| --- | --- |
| RMSE | 11.09 días |
| MAE | 6.34 días |
| R² | -0.0012 |

> Nota: R² negativo indica que el modelo actual no explica la varianza. 
> Siguiente paso: agregar `length + replacement_cost` como features.

### **Cómo correrlo**

1. **Clonar repo**
```bash
git clone https://github.com/dareas7-web/sakila-intelligence.git
cd sakila-intelligence
