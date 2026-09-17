@echo off
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0scripts\start-dashboard.ps1" -NoOpen
if errorlevel 1 exit /b %errorlevel%
start "" "http://127.0.0.1:8792/results"
