# AssemblyInfo

[assembly: log4net.Config.XmlConfigurator(Watch = true)]

# App.config

## コンソール

<?xml version="1.0" encoding="utf-8" ?>
<configuration>

  <configSections>
    <section name="log4net"
             type="log4net.Config.Log4NetConfigurationSectionHandler,log4net" />
  </configSections>

  <log4net>
    <appender name="ConsoleLog" type="log4net.Appender.ConsoleAppender">
      <layout type="log4net.Layout.PatternLayout">
        <conversionPattern value="%d[%t] %p - %m%n"/>
      </layout>
    </appender>

    <root>
      <!-- 使用するアペンダを設定 -->
      <appender-ref ref="ConsoleLog" />
    </root>

  </log4net>

  <startup> 
        <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.7.2" />
    </startup>
</configuration>

## ファイル

<?xml version="1.0" encoding="utf-8" ?>
<configuration>

  <configSections>
    <section name="log4net"
             type="log4net.Config.Log4NetConfigurationSectionHandler,log4net" />
  </configSections>

  <log4net>
    <appender name="ConsoleLog" type="log4net.Appender.ConsoleAppender">
      <layout type="log4net.Layout.PatternLayout">
        
        <!--
        %d	ログ日時の出力
        %L	行番号の出力
        %m	メッセージを出力
        %n	改行文字の出力
        %p	ログレベルの出力
        %t	ログを生成したスレッドの出力
        %M	ログを出力したメソッド名
        %logger	ログクラスのGetLoggerメソッドの引数に渡した値
-->
        <conversionPattern value="%d[%t] %p %logger.%M[line=%L] - %m%n"/>
      </layout>
    </appender>

    <appender name="FileLog" type="log4net.Appender.RollingFileAppender">

      <param name="File" value=".\logs\Meron.log" />
      <param name="AppendToFile" value="true" />

      <param name="rollingStyle" value="Size" />
      <param name="maxSizeRollBackups" value="3" />
      <param name="maximumFileSize" value="5KB" />
      <param name="staticLogFileName" value="false" />


      <layout type="log4net.Layout.PatternLayout">
        <conversionPattern value="%d[%t] %p %logger.%M[line=%L] - %m%n"/>
      </layout>
    </appender>

    <root>

      <level value="INFO" />

      <!-- 使用するアペンダを設定 -->
      <appender-ref ref="ConsoleLog" />
      <appender-ref ref="FileLog" />
    </root>

  </log4net>

  <startup> 
        <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.7.2" />
    </startup>
</configuration>

# 宣言

        private static readonly log4net.ILog _logger =

log4net.LogManager.GetLogger(
System.Reflection.MethodBase.GetCurrentMethod().DeclaringType);

# 使用例

            _logger.Debug("Debug!!");
            _logger.Info("Info!!");
            _logger.Warn("Warn!!");
            _logger.Error("Error!!");
            _logger.Fatal("Fatal!!");
