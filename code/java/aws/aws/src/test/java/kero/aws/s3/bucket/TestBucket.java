package kero.aws.s3.bucket;

import static org.junit.jupiter.api.Assertions.assertNotNull;

import java.util.List; // Import List

import org.junit.jupiter.api.Test;

import kero.aws.s3.client.MyS3Client; // Add this import statement
import software.amazon.awssdk.services.s3.S3Client; // Import S3Client

public class TestBucket {

    @Test
    public void testGetBucketNameList() {
        S3Client s3 = MyS3Client.getS3Client();
        List<String> bucketList = Bucket.getBucketNameList(s3);
        assertNotNull(bucketList);
    }
}
