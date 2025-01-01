package com.example;

import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.ListBucketsResponse;
import software.amazon.awssdk.services.s3.model.S3Exception;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
                // S3 クライアントを作成
        try (S3Client s3 = S3Client.create()) {
            // バケットの一覧を取得
            ListBucketsResponse bucketsResponse = s3.listBuckets();

            // バケット名を出力
            System.out.println("S3 バケット一覧:");
            bucketsResponse.buckets().forEach(bucket -> System.out.println(bucket.name()));
        } catch (S3Exception e) {
            System.err.println("エラー: " + e.awsErrorDetails().errorMessage());
        }
    }
}