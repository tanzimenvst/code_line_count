@echo off
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed.
    exit /b
)
start /min cmd /c python "%~dp0line_count.py"
exit