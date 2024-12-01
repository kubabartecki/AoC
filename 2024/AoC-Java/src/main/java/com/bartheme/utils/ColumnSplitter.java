package com.bartheme.utils;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ColumnSplitter {
    private ColumnSplitter() {
        throw new IllegalStateException("Utility class");
    }

    public static List<List<String>> splitColumns(List<String> lines) {
        List<List<String>> columns = new ArrayList<>();
        int columnCount = StringSplitter.splitWhiteSpace(lines.getFirst()).length;
        for (int i = 0; i < columnCount; i++) {
            columns.add(new ArrayList<>());
        }
        lines.stream()
                .map(StringSplitter::splitWhiteSpace)
                .map(Arrays::asList)
                .forEach(row -> {
                    for (int i = 0; i < row.size(); i++) {
                        columns.get(i).add(row.get(i));
                    }
                });
        return columns;
    }
}
