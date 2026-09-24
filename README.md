# S08 | AP4 | Databricks e Integraciones

**Estudiante:** Nayeli  
**Actividad:** S08 | AP4 | Databricks e Integraciones  
**Fecha:** 24-09-2026

Este repositorio contiene las evidencias técnicas para:

1. Sincronizar GitHub con un **Git Folder de Databricks** mediante **GitHub Actions**.
2. Registrar **3 conexiones diferentes** desde `Catalog > Settings > Connections`.
3. Instalar y comprobar **Databricks CLI** usando HOST y TOKEN.
4. Trabajar con un **Volume de Unity Catalog** para cargar imágenes y PDF.

## Estructura

- `.github/workflows/sync-databricks.yml`: pipeline de GitHub Actions.
- `notebooks/01_prueba_databricks.py`: notebook simple para comprobar sincronización.
- `scripts/verificar_cli.ps1`: comandos de verificación para Windows.
- `docs/GUIA_VIDEO.md`: orden sugerido para grabar el video de evidencia.

## 1. Git Folder + GitHub Actions

En Databricks:

1. Ir a **Workspace**.
2. Elegir la carpeta donde se creará el proyecto.
3. Pulsar **Create > Git folder**.
4. Pegar la URL de este repositorio.
5. Seleccionar **GitHub**.
6. Usar la rama `main`.
7. Crear el Git Folder.

Luego copiar la ruta completa del Git Folder de Databricks.

En GitHub, ir a:

`Settings > Secrets and variables > Actions > New repository secret`

Crear estos 3 secretos:

- `DATABRICKS_HOST`: URL del workspace de Databricks.
- `DATABRICKS_TOKEN`: token personal de Databricks.
- `DATABRICKS_GIT_FOLDER_PATH`: ruta completa del Git Folder, por ejemplo:
  `/Workspace/Users/correo@dominio.com/S07-Databricks-GitHub-Actions`

Cuando estos secretos estén configurados, cada push a `main` hará que GitHub Actions ejecute:

```bash
databricks repos update "$DATABRICKS_GIT_FOLDER_PATH" --branch main
```

## 2. Tres conexiones

La evidencia se revisa desde:

`Catalog > rueda de configuración > Connections`

Debes mostrar **3 conexiones creadas y exitosas**. Pueden ser, según lo que tu cuenta permita:

- GitHub / servicio externo compatible
- Amazon S3 o un origen cloud compatible
- Base de datos, por ejemplo PostgreSQL, MySQL o SQL Server

> Importante: las conexiones disponibles dependen de la edición, permisos y cloud de tu workspace.

## 3. Databricks CLI en Windows

Instalación recomendada:

```powershell
winget search databricks
winget install Databricks.DatabricksCLI
```

Cerrar y volver a abrir PowerShell o CMD y comprobar:

```powershell
databricks -v
```

Configurar con HOST y TOKEN:

```powershell
databricks configure
```

Luego comprobar la autenticación:

```powershell
databricks auth describe
databricks workspace list /
```

No muestres el TOKEN completo en el video.

## 4. Volume para imágenes y PDF

En Databricks:

1. Ir a **Catalog**.
2. Elegir un catálogo y schema.
3. Crear un **Volume**.
4. Abrir el Volume.
5. Subir al menos:
   - una imagen (`.png` o `.jpg`)
   - un PDF (`.pdf`)
6. Mostrar ambos archivos dentro del Volume.

Ruta típica:

```text
/Volumes/<catalog>/<schema>/<volume>/
```

## Evidencia final

En el video muestra:

- repositorio en GitHub;
- archivo del workflow;
- ejecución exitosa en **Actions**;
- Git Folder actualizado en Databricks;
- 3 Connections visibles;
- Databricks CLI funcionando desde terminal;
- imagen y PDF dentro de un Volume.
