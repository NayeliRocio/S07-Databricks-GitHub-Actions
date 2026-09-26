# S08 | AP4 | Databricks e Integraciones

**Estudiante:** Nayeli Herrera Albino  
**Actividad:** S08 | AP4 | Databricks e Integraciones  
**Fecha:** 24-09-2026

Este repositorio contiene el pipeline, notebook y guía de la entrega. **Estado verificado el 26-09-2026:** el Git Folder y el Volume existen; la sincronización automática, las tres Connections, la CLI en el equipo local y el video aún requieren completar sus pruebas.

## Estado de los cuatro puntos

| Punto | Estado comprobado |
| --- | --- |
| GitHub + Git Folder | El repositorio está clonado en Databricks bajo `/Workspace/Users/nayeli.herrera@vallegrande.edu.pe/S07-Databricks-GitHub-Actions`, rama `main`. Falta configurar los tres secrets y obtener un run exitoso del paso de sincronización. |
| Tres Connections | En `Catalog > Settings > Connections` se observan **0 conexiones**. Cada origen requiere credenciales o una autorización real; no cuenta el Git Folder como Connection. |
| CLI local | Hay un script de verificación para Windows. No se ha comprobado la instalación en el equipo local. |
| Volume | Creado `workspace.default.s08_evidencias`, ruta `/Volumes/workspace/default/s08_evidencias`. Se verificó la carga de `s08_integracion.png` y `s08_integracion.pdf`. |

## Estructura

- `.github/workflows/sync-databricks.yml`: pipeline de GitHub Actions.
- `notebooks/01_prueba_databricks.py`: notebook para comprobar el código en el Git Folder.
- `scripts/verificar_cli.ps1`: comandos de verificación para Windows.
- `docs/GUIA_VIDEO.md`: orden sugerido para grabar el video.

## Sincronización con GitHub Actions

En `Settings > Secrets and variables > Actions` de este repositorio se necesitan:

- `DATABRICKS_HOST`: `https://dbc-6d9a3ebe-2368.cloud.databricks.com`
- `DATABRICKS_TOKEN`: token personal válido del workspace; nunca debe publicarse en código, capturas o video.
- `DATABRICKS_GIT_FOLDER_PATH`: `/Workspace/Users/nayeli.herrera@vallegrande.edu.pe/S07-Databricks-GitHub-Actions`

El workflow se ejecuta en cada push a `main` o manualmente desde Actions. Primero verifica los secrets y la autenticación; luego ejecuta `databricks repos update "$DATABRICKS_GIT_FOLDER_PATH" --branch main` y `databricks repos get`. **Si falta un secret, la ejecución falla**; una ejecución verde con el paso de sincronización omitido no demuestra el punto 1.

## Tres Connections

Abrir `Catalog > Settings > Connections`. La tarea exige **tres conexiones diferentes, autenticadas y verificadas**. Elegir servicios para los que existan cuentas y permisos reales (por ejemplo GitHub con OAuth App, Google Drive, una base de datos). No crear conexiones ficticias: GitHub como Git provider en Workspace no equivale a una Connection de Unity Catalog.

## CLI en Windows

La instalación oficial admite WinGet:

```powershell
winget search databricks
winget install Databricks.DatabricksCLI
```

Abrir otra PowerShell y comprobar:

```powershell
databricks -v
databricks configure --host https://dbc-6d9a3ebe-2368.cloud.databricks.com
databricks auth describe
databricks workspace list /
databricks repos get /Workspace/Users/nayeli.herrera@vallegrande.edu.pe/S07-Databricks-GitHub-Actions
```

La versión debe ser al menos 0.205.0. La configuración con token lo solicita en la terminal; no pegarlo en archivos del repositorio ni mostrarlo en el video. La CLI instalada en Codespaces o en GitHub Actions **no sustituye** la evidencia de instalación local solicitada.

## Volume

Abrir el catálogo `workspace`, schema `default`, Volume `s08_evidencias`. En su lista de archivos aparecen una imagen PNG y un PDF cargados para probar almacenamiento no estructurado.

## Entrega

Grabar un video que muestre el run con **Sync Databricks Git Folder** realmente exitoso, el Git Folder actualizado, tres Connections reales, la CLI en el equipo local y ambos archivos en el Volume. Entregar el video y el enlace a este repositorio. No presentar los puntos pendientes como terminados.
