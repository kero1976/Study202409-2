# 1.はじめに

MySQLのDockerイメージはOSがOracleLinuxだった。

# 2. パッケージのインストールについて

パッケージ管理ソフトとして、apt-get、yum、dnf、がインストールされていなかった。
microdnfを使用する必要がある。

## 2-1.yumのインストール

```
microdnf install yum
```
