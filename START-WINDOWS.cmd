@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 (
  py -3 serve.py
  goto done
)
where python >nul 2>nul
if not errorlevel 1 (
  python serve.py
  goto done
)
where node >nul 2>nul
if not errorlevel 1 (
  node scripts\serve.mjs
  goto done
)
echo Please install Python 3.9 or newer, or Node.js 18 or newer.
echo Then run START-WINDOWS.cmd again.
:done
pause
