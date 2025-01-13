package kero.aws.utils;

/**
 * 環境変数を取得するユーティリティクラス
 * テストをやりやすくするために作成
 */
public final class EnvironmentUtils {

    // プライベートコンストラクタでインスタンス化を防止
    private EnvironmentUtils() {
    }

    public static String getEnv(String name) {
        return System.getenv(name);
    }
}
