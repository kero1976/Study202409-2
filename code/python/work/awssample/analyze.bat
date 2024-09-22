@echo off

REM 出力先ファイルを指定
set OUTPUT_FILE=dest\pylint\pylint_output.txt
if exist %OUTPUT_FILE% del %OUTPUT_FILE%

REM 処理開始時刻を取得
set START_TIME=%time%

REM 開始時刻を出力
echo START TIME: %START_TIME% >> %OUTPUT_FILE%
echo START TIME: %START_TIME%

REM awssampleプロジェクト内の全てのPythonファイルを再帰的に検索してPylintでチェック

for /r awssample %%f in (*.py) do (
    echo Checking %%f >> %OUTPUT_FILE%
    echo Checking %%f
    pylint "%%f" >> %OUTPUT_FILE%
    pylint "%%f"
)

REM 処理終了時刻を取得
set END_TIME=%time%

REM 終了時刻を出力
echo END TIME: %END_TIME% >> %OUTPUT_FILE%
echo END TIME: %END_TIME%

REM 経過時間を計算するために時間をフォーマットする
for /f "tokens=1-4 delims=:,." %%a in ("%START_TIME%") do (
    set /a START_HOUR=%%a
    set /a START_MINUTE=%%b
    set /a START_SECOND=%%c
    set /a START_MS=%%d
)

for /f "tokens=1-4 delims=:,." %%a in ("%END_TIME%") do (
    set /a END_HOUR=%%a
    set /a END_MINUTE=%%b
    set /a END_SECOND=%%c
    set /a END_MS=%%d
)

REM 開始時間と終了時間の差を計算
set /a DURATION_HOUR=END_HOUR-START_HOUR
set /a DURATION_MINUTE=END_MINUTE-START_MINUTE
set /a DURATION_SECOND=END_SECOND-START_SECOND
set /a DURATION_MS=END_MS-START_MS

REM 経過時間を出力
echo TIME: %DURATION_HOUR%H %DURATION_MINUTE%M %DURATION_SECOND%S %DURATION_MS%sss >> %OUTPUT_FILE%
echo TIME: %DURATION_HOUR%H %DURATION_MINUTE%M %DURATION_SECOND%S %DURATION_MS%sss
