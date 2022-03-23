@echo off
call "%~dp0env_for_icons.bat"  %*
rem backward compatibility for non-IDLEX users
if exist "%WINPYDIR%\scripts\idlex.pyw" (
    "%WINPYDIR%\python.exe" "%WINPYDIR%\scripts\idlex.pyw" %*
) else (
    "%WINPYDIR%\python.exe" "%WINPYDIR%\lib-python\3\idlelib\idle.pyw" %*
)
