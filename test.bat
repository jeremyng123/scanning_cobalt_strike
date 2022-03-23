for /f "tokens=1,*" %%i in ('fsutil fsinfo drives') do (
  :: work with %%j here
  echo %%j
)