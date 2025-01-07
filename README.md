# Minecraft Server Updater
Paperサーバー、PurpurサーバーとVelocityサーバーを自動で最新のビルドに更新します。\
apiから最新のビルドを取得してjsonファイルと照合します。

## jsonファイルの説明
`file` : サーバーのjarファイルのjsonファイルからの相対パスまたは絶対パス(存在しない場合は生成されます)\
`software` : 使用するソフトウェア("purpur"または"paper"または"velocity")\
`version` : Minecraftのバージョン(プロキシサーバーの場合はソフトウェアのバージョン)\
`build` : ビルドの番号\
`version-up` : Minecraftのバージョンの最新版を使用する場合にこれをtrueに設定します。プロキシサーバーの場合、この項は不要です。

## 新しいサーバーを建てる場合
サーバーを建てる場合、ブラウザからサーバーファイルをダウンロードせずとも、jsonファイルを次のように作成することで最新のビルドのサーバーファイルをダウンロードします。\
_sample.json_
```
{
  "file": "(任意のjarファイル名を入力してください。存在しない場合、生成されます。)",
  "software": "purpur",
  "version": "1.21.4('version-up'をtrueに設定している、または、プロキシサーバーの場合、任意の文字列)",
  "build": 0(自動で最新のビルドに変更されます),
  "version-up": false(常に最新のバージョンで実行したい場合、trueに設定してください。)
}
```
batファイルを例のように作成して実行すると、サーバー起動前に更新を確認して、サーバーを起動します。\
_sample.cmd_
```
@echo off
py main.py sample.json
IF %ERRORLEVEL% == 0 (
    java -Xmx4G -Xms4G -jar server.jar
    pause
) ELSE (
    echo %ERRORLEVEL%
    pause
)
```
