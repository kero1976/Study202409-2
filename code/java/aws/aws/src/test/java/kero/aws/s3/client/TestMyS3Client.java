package kero.aws.s3.client;

import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.mockito.Mockito.mockStatic;

import org.junit.jupiter.api.Test;
import org.mockito.MockedStatic;

import kero.aws.utils.EnvironmentUtils;
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.services.s3.S3Client;

public class TestMyS3Client {

    @Test
    public void testGetAwsBasicCredentialsIsNull() {
        AwsBasicCredentials credentials = MyS3Client.getAwsBasicCredentials();

        assertNull(credentials);
    }

    @Test
    public void testGetAwsBasicCredentialsIsNotNull() {
        try (MockedStatic<EnvironmentUtils> mocked = mockStatic(EnvironmentUtils.class)) {
            mocked.when(() -> EnvironmentUtils.getEnv("S3_ENDPOINT")).thenReturn("mocked_endpoint");
            mocked.when(() -> EnvironmentUtils.getEnv("S3_AWS_ACCESS_KEY_ID")).thenReturn("mocker_access_key");
            mocked.when(() -> EnvironmentUtils.getEnv("S3_AWS_SECRET_ACCESS_KEY")).thenReturn("mocked_secret_key");

            AwsBasicCredentials credentials = MyS3Client.getAwsBasicCredentials();

            assertNotNull(credentials);

        }
    }

    @Test
    public void testGetS3ClientIsEndpoint() {
        try (MockedStatic<EnvironmentUtils> mocked = mockStatic(EnvironmentUtils.class)) {
            mocked.when(() -> EnvironmentUtils.getEnv("S3_ENDPOINT")).thenReturn("http://localhost:9000");
            mocked.when(() -> EnvironmentUtils.getEnv("S3_AWS_ACCESS_KEY_ID")).thenReturn("mocker_access_key");
            mocked.when(() -> EnvironmentUtils.getEnv("S3_AWS_SECRET_ACCESS_KEY")).thenReturn("mocked_secret_key");

            S3Client client = MyS3Client.getS3Client();

            assertNotNull(client);

        }
    }

    @Test
    public void testGetS3Client() {
        S3Client client = MyS3Client.getS3Client();

        assertNotNull(client);
    }
}
