package com.bartheme.utils;

public class StringSplitter {
    private StringSplitter() {
        throw new IllegalStateException("Utility class");
    }
    public static String[] splitWhiteSpace(String line) {
        return line.split("\\s+");
    }
}
