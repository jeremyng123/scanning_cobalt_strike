@echo off
call "%~dp0env_for_icons.bat"  %*
"%WINPYDIR%\python.exe" "%WINPYDIR%\lib-python\3\idlelib\idle.pyw" %*

