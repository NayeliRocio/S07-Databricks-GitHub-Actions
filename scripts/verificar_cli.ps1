Write-Host "=== S08 AP4 | Verificacion Databricks CLI ==="
Write-Host ""

Write-Host "1) Version instalada:"
databricks -v

Write-Host ""
Write-Host "2) Estado de autenticacion:"
databricks auth describe

Write-Host ""
Write-Host "3) Listado basico del workspace:"
databricks workspace list /

Write-Host ""
Write-Host "4) Git Folders administrables por la cuenta:"
databricks repos list

Write-Host ""
Write-Host "Listo. No muestres tu TOKEN en el video."
