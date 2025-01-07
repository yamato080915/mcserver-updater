@echo off
py main.py paper1165.json
IF %ERRORLEVEL% == 0 (
    java -Xmx4G -Xms4G -jar paper1165.jar
    pause
) ELSE (
    echo %ERRORLEVEL%
    pause
)