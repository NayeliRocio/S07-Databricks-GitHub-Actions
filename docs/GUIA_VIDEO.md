# Guía rápida para grabar el video de evidencia

Graba un solo video corto, siguiendo este orden para que el profesor pueda revisar los 4 puntos sin buscar nada.

## Punto 1 — GitHub + Git Folder + GitHub Actions

1. Abre este repositorio en GitHub.
2. Muestra `.github/workflows/sync-databricks.yml`.
3. En Databricks abre **Workspace** y entra al Git Folder clonado desde este repositorio.
4. Muestra el archivo `notebooks/01_prueba_databricks.py`.
5. Vuelve a GitHub y entra a **Actions**.
6. Abre la última ejecución y muestra que el paso **Sync Databricks Git Folder** terminó correctamente.

Frase sencilla para decir:
> "Este repositorio está conectado con un Git Folder de Databricks. El workflow se ejecuta al hacer push a main y actualiza automáticamente el Git Folder."

## Punto 2 — Tres conexiones

1. En Databricks entra a **Catalog**.
2. Abre la rueda de configuración.
3. Entra a **Connections**.
4. Muestra las tres conexiones diferentes creadas y que no tengan error.

Frase:
> "Aquí se observan tres conexiones diferentes habilitadas correctamente desde Unity Catalog."

## Punto 3 — Databricks CLI

En PowerShell muestra:

```powershell
databricks -v
databricks auth describe
databricks workspace list /
databricks repos list
```

Frase:
> "Instalé Databricks CLI en mi equipo local y configuré el acceso al workspace usando HOST y TOKEN."

**No abras ni muestres el TOKEN completo.**

## Punto 4 — Volume

1. En Databricks abre **Catalog**.
2. Entra al catálogo y schema donde creaste el Volume.
3. Abre el Volume.
4. Muestra una imagen y un PDF cargados.

Frase:
> "En este Volume de Unity Catalog cargué archivos no estructurados, en este caso una imagen y un PDF."

## Cierre

Muestra nuevamente el repositorio y di:

> "Con esto se evidencian los cuatro puntos solicitados: sincronización con GitHub Actions, tres conexiones, Databricks CLI y uso de Volumes."
