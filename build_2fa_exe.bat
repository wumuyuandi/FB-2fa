@echo off
chcp 65001 >nul
echo ========================================
echo 2FA 验证码生成器 打包脚本
echo ========================================
echo.

python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo [1/4] 正在安装 PyInstaller...
    python -m pip install pyinstaller
    if errorlevel 1 (
        echo 错误：无法安装 PyInstaller
        pause
        exit /b 1
    )
) else (
    echo [1/4] PyInstaller 已安装
)

python -c "import pyotp" 2>nul
if errorlevel 1 (
    echo [2/4] 正在安装 pyotp...
    python -m pip install pyotp
    if errorlevel 1 (
        echo 错误：无法安装 pyotp
        pause
        exit /b 1
    )
) else (
    echo [2/4] pyotp 已安装
)

echo.
echo [3/4] 正在清理旧的构建文件...
if exist build\2FA验证码生成器 rmdir /s /q build\2FA验证码生成器
if exist dist\2FA验证码生成器.exe del /q dist\2FA验证码生成器.exe

echo.
echo [4/4] 正在打包程序...
python -m PyInstaller --onefile --windowed --name "2FA验证码生成器" --clean --noconfirm 2fa.py

if errorlevel 1 (
    echo.
    echo 打包失败！
    pause
    exit /b 1
)

echo.
echo ========================================
echo 打包完成！
echo ========================================
echo.
echo exe 文件位置：dist\2FA验证码生成器.exe
echo.
pause
