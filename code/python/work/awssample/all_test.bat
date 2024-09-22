@echo off

REM 出力ディレクトリを指定
set OUTPUT_DIR=dest\test

REM 出力ディレクトリが存在しない場合は作成
if not exist %OUTPUT_DIR% (
    mkdir %OUTPUT_DIR%
)

REM pytestを実行し、カバレッジレポートを出力
pytest --cov=awssample --cov-report=html:%OUTPUT_DIR% --cov-report=term

REM 処理結果を確認
if %errorlevel% neq 0 (
    echo Tests failed. Check the output for more details.
) else (
    echo Tests passed successfully.
)

