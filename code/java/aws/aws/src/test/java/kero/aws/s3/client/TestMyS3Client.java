package kero.aws.s3.client;

import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertNull;

import org.junit.jupiter.api.Test;

import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;

public class TestMyS3Client {

    @Test
    public void testGetAwsBasicCredentialsIsNull() {
        AwsBasicCredentials credentials = MyS3Client.getAwsBasicCredentials();

        assertNull(credentials);
    }

    @Test
    public void testGetAwsBasicCredentialsIsNotNull() {
        AwsBasicCredentials credentials = MyS3Client.getAwsBasicCredentials();

        System.setProperty("S3_ENDPOINT", "endpoint");
        assertNotNull(credentials);
    }
}
