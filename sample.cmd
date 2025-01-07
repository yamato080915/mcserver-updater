@echo off
py main.py server.json
IF %ERRORLEVEL% == 0 (
    java -Xmx4G -Xms4G -jar server.jar
    pause
) ELSE (
    echo %ERRORLEVEL%
    pause
)
