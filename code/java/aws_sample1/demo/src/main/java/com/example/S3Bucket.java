package com.example;

import java.util.ArrayList;
import java.util.List;

public class S3Bucket {

    public List<String> getNames(final String BucketName) {
        List<String> list = new ArrayList<String>();
        list.add("test1");
        list.add("test2");
        return list;
    }
}
