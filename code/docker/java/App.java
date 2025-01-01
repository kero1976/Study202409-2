import java.util.Properties;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        System.out.println("Hello, Docker!");

        System.out.println("****************************************************************************************");
        System.out.println("Properties");
        System.out.println("****************************************************************************************");
        
        Properties properties = System.getProperties();

        // すべてのプロパティと値を表示
        properties.forEach((key, value) -> {
            System.out.println(key + ": " + value);
        });

        System.out.println("");
        System.out.println("****************************************************************************************");
        System.out.println("env");
        System.out.println("****************************************************************************************");

        // 環境変数を取得
        Map<String, String> env = System.getenv();

        // すべての環境変数と値を表示
        env.forEach((key, value) -> {
            System.out.println(key + ": " + value);
        });
    }
}