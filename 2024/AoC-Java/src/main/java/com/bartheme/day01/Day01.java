package com.bartheme.day01;

import com.bartheme.utils.FileReader;
import com.bartheme.utils.ColumnSplitter;

import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Day01 {
    private static final String ID = "01";

    public static void main(String[] args) {
        System.out.println(secondPartSolution());
    }

    private static int firstPartSolution() {
        Stream<String> lines = FileReader.linesStream(ID, true);
        List<List<String>> columns = ColumnSplitter.splitColumns(lines.toList());
        List<Integer> firstColumn = sortStringNums(columns.get(0));
        List<Integer> secondColumn = sortStringNums(columns.get(1));
        return sumDistances(firstColumn, secondColumn);
    }

    // input numbers are ok to use int as a sum
    private static int sumDistances(List<Integer> firstColumn, List<Integer> secondColumn) {
        return IntStream.range(0, firstColumn.size())
                .map(i -> calculateDistance(firstColumn.get(i), secondColumn.get(i)))
                .sum();

    }

    private static Integer calculateDistance(Integer first, Integer second) {
        return Math.abs(first - second);
    }

    private static List<Integer> sortStringNums(List<String> nums) {
        return nums.stream()
                .map(Integer::parseInt)
                .sorted()
                .toList();
    }

    // -------------------- second part solution --------------------
    private static int secondPartSolution() {
        Stream<String> lines = FileReader.linesStream(ID, true);
        List<List<String>> columns = ColumnSplitter.splitColumns(lines.toList());
        List<String> firstColumn = columns.get(0);
        List<String> secondColumn = columns.get(1);
        Map<String, Integer> secondColumnOccurrences = countOccurrences(secondColumn);
        return sumSimilarities(firstColumn, secondColumnOccurrences);
    }

    // could be converted to Integer stream for better performance
    private static Map<String, Integer> countOccurrences(List<String> nums) {
        return nums.stream()
                // Collectors.toMap()
                // 1. key mapper - maps the value to the map key
                // 2. value mapper - maps the value to initial value of the key, when first time encountered
                // 3. merge function - merges the value with the existing value of the key (if there are more than one same key)
                .collect(Collectors.toMap(Function.identity(), i -> 1, Integer::sum));
    }

    private static int calculateSimilarity(String num, Integer occurrences) {
        return Integer.parseInt(num) * occurrences;
    }

    // can overflow here tbh (convert to long if needed)
    private static int sumSimilarities(List<String> firstColumn, Map<String, Integer> secondColumnOccurrences) {
        return firstColumn.stream()
                // mapToInt()
                // This operation transforms each element in the stream to a primitive int (specifically, it maps each element to an int result).
                .mapToInt(num -> calculateSimilarity(num, secondColumnOccurrences.getOrDefault(num, 0)))
                .sum();
    }
}
