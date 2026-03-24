# クッキーのIDを使用する

1. JMETER_HOME\bin\jmeter.propertiesを開きます。

2. 「#CookieManager.save.cookies=false」となっている個所を「CookieManager.save.cookies=true」に修正する。

3. "${COOKIE_sessionId}"のように使用する。sessionId部分は環境に合わせる。
