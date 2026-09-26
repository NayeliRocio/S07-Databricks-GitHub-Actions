# S08 | AP4 | Databricks e Integraciones

**Estudiante:** Nayeli Herrera Albino  
**Actividad:** S08 | AP4 | Databricks e Integraciones  
**Fecha:** 24-09-2026

Este repositorio contiene el pipeline, notebook y guía de la entrega. **Estado verificado el 26-09-2026:** el Git Folder está sincronizado en el workspace `dbc-2aa79bb9-b5b2`. El Volume fue comprobado en el workspace anterior `dbc-6d9a3ebe-2368`; se debe verificar o recrear en el workspace de entrega. La captura de Catalog muestra cuatro Connections (GitHub, Google Drive, Neon PostgreSQL y otra de Drive). La usuaria informó que funcionan; falta registrar su prueba y la evidencia en video, además de comprobar el Volume en este workspace.

## Estado de los cuatro puntos

| Punto | Estado comprobado |
| --- | --- |
| GitHub + Git Folder | El repositorio está clonado en Databricks bajo `/Workspace/Users/nayeli.herrera@vallegrande.edu.pe/S07-Databricks-GitHub-Actions`, rama `main`. Sincronización verificada: `main`, commit `dd7485f9ca42c89b67286bb6ee1379c0b39aef91`, [ejecución exitosa](https://github.com/NayeliRocio/S07-Databricks-GitHub-Actions/actions/runs/36259034654). |
| Tres Connections | La captura del 26-09-2026 muestra cuatro: `nayeli_github`, `nayeli_google_drive`, `nayeli_neon_postgresql` y `s08_google_drive`. Hay tres tipos distintos. La usuaria informa que funcionan; conservar en video una prueba visible de cada una. |
| CLI local | La CLI responde en PowerShell local. Falta repetir la autenticación con el host correcto y registrar la evidencia en video. |
| Volume | Se creó `workspace.default.s08_evidencias` en el workspace anterior (`dbc-6d9a3ebe-2368`) y se verificaron `s08_integracion.png` y `s08_integracion.pdf`. Falta confirmar que el Volume y los archivos sean visibles en el workspace objetivo (`dbc-2aa79bb9-b5b2`); si no aparecen, crear allí un Volume y subirlos de nuevo. |

## Estructura

- `.github/workflows/sync-databricks.yml`: pipeline de GitHub Actions.
- `notebooks/01_prueba_databricks.py`: notebook para comprobar el código en el Git Folder.
- `scripts/verificar_cli.ps1`: comandos de verificación para Windows.
- `docs/GUIA_VIDEO.md`: orden sugerido para grabar el video.

## Sincronización con GitHub Actions

En `Settings > Secrets and variables > Actions` de este repositorio están configurados:

- `DATABRICKS_HOST`: `https://dbc-2aa79bb9-b5b2.cloud.databricks.com`
- `DATABRICKS_TOKEN`: token personal del mismo workspace; nunca debe publicarse en código, capturas o video. Revocar cualquier token expuesto.
- `DATABRICKS_GIT_FOLDER_PATH`: `/Workspace/Users/nayeli.herrera@vallegrande.edu.pe/S07-Databricks-GitHub-Actions`

El workflow se ejecuta en cada push a `main` o manualmente desde Actions. Primero verifica los secrets y la autenticación; luego ejecuta `databricks repos update "$DATABRICKS_GIT_FOLDER_PATH" --branch main` y `databricks repos get`. **Si falta un secret, la ejecución falla**; una ejecución verde con el paso de sincronización omitido no demuestra el punto 1.

## Tres Connections

Abrir `Catalog > Settings > Connections`. La tarea exige **tres conexiones diferentes, autenticadas y verificadas**. Mostrar en el video GitHub, Google Drive y Neon PostgreSQL, con una comprobación de funcionamiento de cada una. Los cuatro objetos de la captura pertenecen a Catalog > Connections; el Git Folder es una integración distinta.

## CLI en Windows

La instalación oficial admite WinGet:

```powershell
winget search databricks
winget install Databricks.DatabricksCLI
```

Abrir otra PowerShell y comprobar:

```powershell
databricks -v
databricks configure --host https://dbc-2aa79bb9-b5b2.cloud.databricks.com
databricks auth describe
databricks workspace list /
databricks repos get /Workspace/Users/nayeli.herrera@vallegrande.edu.pe/S07-Databricks-GitHub-Actions
```

La versión debe ser al menos 0.205.0. La configuración con token lo solicita en la terminal; no pegarlo en archivos del repositorio ni mostrarlo en el video. La CLI instalada en Codespaces o en GitHub Actions **no sustituye** la evidencia de instalación local solicitada.

## Volume

Abrir el catálogo `workspace`, schema `default`, Volume `s08_evidencias`. Comprobar en el workspace objetivo que aparezcan una imagen PNG y un PDF; la comprobación previa corresponde al otro workspace.

## Entrega

Grabar un video que muestre la [ejecución exitosa del pipeline](https://github.com/NayeliRocio/S07-Databricks-GitHub-Actions/actions/runs/36259034654), el Git Folder actualizado, tres Connections reales, la CLI en el equipo local y ambos archivos en el Volume. Entregar el video y el enlace a este repositorio. No presentar los puntos pendientes como terminados.
