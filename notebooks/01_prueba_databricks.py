# Databricks notebook source
# MAGIC %md
# MAGIC # S08 | AP4 | Databricks e Integraciones
# MAGIC **Estudiante:** Nayeli
# MAGIC
# MAGIC Este notebook sirve como evidencia de que el contenido del repositorio GitHub
# MAGIC se encuentra sincronizado con el Git Folder de Databricks.

# COMMAND ----------

print("GitHub -> Databricks Git Folder: sincronización correcta")

# COMMAND ----------

df = spark.range(1, 6).withColumnRenamed("id", "numero")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Evidencia
# MAGIC Si este archivo aparece dentro del Git Folder de Databricks después de ejecutar
# MAGIC el workflow de GitHub Actions, el punto 1 de la actividad queda demostrado.
