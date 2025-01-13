package kero.aws.s3.client;

import java.net.URI;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import kero.aws.utils.EnvironmentUtils;
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
import software.amazon.awssdk.auth.credentials.StaticCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.S3Configuration;

/**
 * S3_ENDPOINTが指定されている場合に、以下の値から
 * S3_AWS_ACCESS_KEY_ID
 * S3_AWS_SECRET_ACCESS_KEY
 */
public class MyS3Client {

    // Loggerインスタンスを作成
    private static final Logger logger = LoggerFactory.getLogger(MyS3Client.class);

    public static S3Client getS3Client() {
        logger.debug("START");
        String endpoint = EnvironmentUtils.getEnv("S3_ENDPOINT");
        if (endpoint != null) {
            logger.debug("S3_ENDPOINT: {}", endpoint);
            AwsBasicCredentials credentials = getAwsBasicCredentials();
            if (credentials != null) {
                S3Client client = S3Client.builder()
                        .credentialsProvider(StaticCredentialsProvider.create(credentials))
                        .region(Region.AP_NORTHEAST_1) // リージョンの設定
                        .endpointOverride(URI.create(endpoint)) // エンドポイントの指定
                        .serviceConfiguration(S3Configuration.builder()
                                .pathStyleAccessEnabled(true) // パススタイルを有効化（MinIOや一部の互換サービスに必要）
                                .build())
                        .build();
                logger.debug("SUCCESS: Created S3Client");
                return client;
            }

            logger.error("ERROR: Failed to create S3Client");
            return null;
        }
        S3Client client = S3Client.builder()
                .region(Region.AP_NORTHEAST_1)
                .credentialsProvider(DefaultCredentialsProvider.create()) // 環境変数または設定ファイルから認証情報を取得
                .build();
        logger.debug("SUCCESS: Created S3Client");
        return client;
    }

    /**
     * S3_ENDPOINTが指定されている場合に、以下の値から
     * S3_AWS_ACCESS_KEY_ID
     * S3_AWS_SECRET_ACCESS_KEY
     * を取得して、AwsBasicCredentialsを作成する
     * 
     * @return AwsBasicCredentials
     */
    static AwsBasicCredentials getAwsBasicCredentials() {
        logger.debug("START");
        String endpoint = EnvironmentUtils.getEnv("S3_ENDPOINT");
        if (endpoint != null) {
            logger.debug("S3_ENDPOINT: {}", endpoint);
            String accessKeyId = EnvironmentUtils.getEnv("S3_AWS_ACCESS_KEY_ID");
            String secretAccessKey = EnvironmentUtils.getEnv("S3_AWS_SECRET_ACCESS_KEY");
            logger.debug("S3_AWS_ACCESS_KEY_ID: {}, S3_AWS_SECRET_ACCESS_KEY: {}", accessKeyId, secretAccessKey);
            try {
                AwsBasicCredentials credentials = AwsBasicCredentials.create(
                        accessKeyId,
                        secretAccessKey);
                logger.debug("SUCCESS: Created AwsBasicCredentials");
                return credentials;
            } catch (Exception e) {
                logger.error("ERROR: Failed to create AwsBasicCredentials");
                return null;
            }
        }
        logger.error("ERROR: S3_ENDPOINT is not set");
        return null;
    }
}
