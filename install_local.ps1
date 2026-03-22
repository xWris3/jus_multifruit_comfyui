$DestRoot = "D:\AI\Stability_Matrix_Install\Data\Packages\ComfyUI_Cloud\custom_nodes"
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue "$DestRoot\$PSScriptRoot"
Copy-Item -Path $PSScriptRoot -Destination $DestRoot -Recurse -Force -Exclude "install_local.ps1", ".git"