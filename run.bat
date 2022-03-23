@REM https://www.windows-commandline.com/check-windows-32-bit-64-bit-command-line/#comment-body-45646
@ECHO OFF
:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:-------------------------------------- 

ECHO ==========================
ECHO Running scan on your machines...
ECHO ============================
@REM ECHO %PROCESSOR_ARCHITECTURE%
IF /I "%PROCESSOR_ARCHITECTURE%" EQU "X86" (
    ECHO ==========================
    ECHO This is a 32-bit Architecture
    ECHO ============================
    cmd /k ".\run_86.bat & .\run_86_static.bat"
) ELSE (
    ECHO ==========================
    ECHO This is a 64-bit Architecture
    ECHO ============================
    cmd /k ".\run_64.bat & .\run_64_static.bat"
)