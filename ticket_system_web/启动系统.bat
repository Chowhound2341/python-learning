@echo off
echo 正在启动47游乐园门票系统...
echo.
echo 选择启动方式:
echo 1. 在默认浏览器中直接打开
echo 2. 启动本地服务器 (推荐)
echo.
set /p choice=请输入选择 (1 或 2): 

if "%choice%"=="1" (
    echo 正在打开网页...
    start index.html
) else if "%choice%"=="2" (
    echo 正在启动本地服务器...
    echo 服务器地址: http://localhost:8000
    echo 按 Ctrl+C 可停止服务器
    echo.
    python -m http.server 8000
) else (
    echo 无效选择，直接打开网页...
    start index.html
)

pause
