package kero.aws.s3.bucket;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.ListBucketsResponse;
import software.amazon.awssdk.services.s3.model.S3Exception;

public class Bucket {

    // Loggerインスタンスを作成
    private static final Logger logger = LoggerFactory.getLogger(Bucket.class);

    public static List<String> getBucketNameList(S3Client s3) {
        logger.debug("START(S3Client={})", s3);
        try {
            ListBucketsResponse bucketsResponse = s3.listBuckets();
            List<String> bucketNameList = bucketsResponse.buckets().stream().map(bucket -> bucket.name())
                    .collect(java.util.stream.Collectors.toList()); // バケット名のリストを取得

            logger.debug("SUCCESS: Get bucket name list.(Bucket Size={})", bucketNameList.size());
            return bucketNameList;
        } catch (S3Exception e) {
            logger.error("ERROR: Failed to get bucket name list.", e);
            return null;
        }
    }

}