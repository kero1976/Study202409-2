# 事前準備として以下のコマンドを実行する
# Set-ExecutionPolicy Unrestricted
# Unblock-File -Path "C:\Path\To\Your\Script.ps1"

# 出力先ファイルを指定
$OUTPUT_FILE = "dest\pylint_output.txt"
if (Test-Path $OUTPUT_FILE) {
    Remove-Item $OUTPUT_FILE
}

# 処理開始時刻を取得
$START_TIME = Get-Date

# 開始時刻を出力
$START_TIME_STR = $START_TIME.ToString("HH:mm:ss.fff")
Add-Content $OUTPUT_FILE "START TIME: $START_TIME_STR"
Write-Host "START TIME: $START_TIME_STR"

# 警告が出たかどうかのフラグ
$warning_found = $false

# 警告の除外条件
$disable_rule = ""

# awssampleプロジェクト内の全てのPythonファイルを再帰的に検索してPylintでチェック
Get-ChildItem -Recurse -Filter *.py -Path "awssample" | ForEach-Object {
    $file = $_.FullName
    Add-Content $OUTPUT_FILE "Checking $file"
    Write-Host "Checking $file"
    
    # Pylintコマンドの実行結果を取得
    if (-not $disable_rule) {
         $pylint_output = Invoke-Expression "pylint $file"
    } else {
         $pylint_output = Invoke-Expression "pylint --disable=$disable_rule $file"
    }

    # 結果を出力ファイルに追加
    Add-Content $OUTPUT_FILE $pylint_output
    Write-Host $pylint_output
    
    # 警告が含まれているか確認
    if ($pylint_output -match "warning|W:") {
        $warning_found = $true
    }
}

# 処理終了時刻を取得
$END_TIME = Get-Date

# 終了時刻を出力
$END_TIME_STR = $END_TIME.ToString("HH:mm:ss.fff")
Add-Content $OUTPUT_FILE "END TIME: $END_TIME_STR"
Write-Host "END TIME: $END_TIME_STR"

# 経過時間を計算
$DURATION = $END_TIME - $START_TIME

# 経過時間を出力
$DURATION_STR = $DURATION.ToString("hh\:mm\:ss\.fff")
Add-Content $OUTPUT_FILE "TIME: $DURATION_STR"
Write-Host "TIME: $DURATION_STR"

# 警告が出たかどうかを出力
if ($warning_found) {
    Add-Content $OUTPUT_FILE "Warning found during Pylint check."
    Write-Host "Warning found during Pylint check."
} else {
    Add-Content $OUTPUT_FILE "No warnings found during Pylint check."
    Write-Host "No warnings found during Pylint check."
}
