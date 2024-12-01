package com.bartheme.utils;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.logging.Logger;
import java.util.stream.Stream;

public class FileReader {
    private FileReader() {
        throw new IllegalStateException("Utility class");
    }
    private static final String PATH_PREFIX = "src/main/resources/inputs/";
    private static final String FILE_EXTENSION = ".txt";
    private static Logger logger = Logger.getLogger(FileReader.class.getName());

    public static Stream<String> linesStream(String filename, boolean isFirstPart) {
        String filePath = PATH_PREFIX + filename + (isFirstPart ? "a" : "b") + FILE_EXTENSION ;
        Path path  = Paths.get(filePath);
        try {
            return Files.lines(path);
        } catch (IOException e) {
            logger.info("File not found");
            return Stream.empty();
        }
    }
}
