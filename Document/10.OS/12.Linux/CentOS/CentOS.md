#CentOS7

## Proxy

ブラウザのプロキシ設定を手動で行う

### 証明書の更新

```
cp 証明書 /etc/pki/ca-trust/source/anchors/
sudo update-ca-trust extract
```

### yum

