@echo off
chcp 65001 >nul
:: 47游乐园门票系统启动脚本
color 0e

echo.
echo ===============================
echo   欢迎使用 47游乐园门票系统
set "line=-------------------------------"
echo %line%
echo 请选择启动方式：
echo 1. 直接用浏览器打开 index.html
set "line=-------------------------------"
echo 2. 启动本地服务器并自动打开网页 (推荐)
echo %line%
echo.
set /p choice=请输入选择 (1 或 2): 

if "%choice%"=="1" (
    echo 正在打开网页...
    start "" index.html
    goto :eof
) else if "%choice%"=="2" (
    echo 正在检测 Python 环境...
    python --version >nul 2>nul || (
        echo [错误] 未检测到 Python，请先安装 Python 3！
        pause
        exit /b
    )
    echo 正在启动本地服务器...
    start "" http://localhost:8000
    echo 服务器地址: http://localhost:8000
    echo 按 Ctrl+C 可停止服务器
    echo.
    python -m http.server 8000
    goto :eof
) else (
    echo 无效选择，默认直接打开网页...
    start "" index.html
)

pause
