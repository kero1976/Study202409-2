package com.example;

import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.mockito.Mockito.*;
import java.util.List;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.InjectMocks;
import org.mockito.MockitoAnnotations;
import static org.assertj.core.api.Assertions.*;

public class S3BucketTest {

    @InjectMocks
    private S3Bucket s3Bucket;

    @BeforeEach
    public void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    public void testGetNames() {
        String bucketName = "test-bucket";
        List<String> result = s3Bucket.getNames(bucketName);
        assertNotNull(result);
        // resultの要素数が1であることを検証する
        assertThat(result)
                .hasSize(2) // リストの要素数が1であることを確認
                .contains("test1"); // "element" を含んでいることを確認
    }
}