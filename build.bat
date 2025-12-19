@echo off
echo ==========================================
echo 🔨 Starting Rock Paper Scissors Build
echo ==========================================

:: 1. Activate virtual environment
:: (If your venv folder has a different name, update ".venv" below)
if exist .venv\Scripts\activate (
    call .venv\Scripts\activate
) else (
    echo ⚠️ Warning: Virtual environment not found. Using global Python...
)

:: 2. Run PyInstaller
echo.
echo ⏳ Generating executable...
pyinstaller --onefile --name "RockPaperScissors" main.py

:: 3. Cleanup (Optional)
:: Removes the 'build' folder and .spec file to keep the project clean
echo.
echo 🧹 Cleaning up temporary files...
if exist build rmdir /s /q build
if exist RockPaperScissors.spec del RockPaperScissors.spec

echo.
echo ==========================================
echo ✅ SUCCESS! Executable created in 'dist' folder
echo ==========================================
pause