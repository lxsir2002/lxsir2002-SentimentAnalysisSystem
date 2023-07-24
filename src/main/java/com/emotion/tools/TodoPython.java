package com.emotion.tools;


import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVPrinter;

import java.io.*;
import java.util.ArrayList;
import java.util.List;


public final  class TodoPython {
    public static String getEmotionByOne(String path, String text) throws IOException, InterruptedException {
        // 构建进程
        ProcessBuilder pb = new ProcessBuilder("D:/Anaconda/envs/pyt/python.exe", path, text);
        pb.redirectErrorStream(true);

        // 启动进程
        Process process = pb.start();

        // 等待进程完成
        int exitCode = process.waitFor();

        // 获取进程的输出
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String line;
        List<String> output = new ArrayList<>();

        while ((line = reader.readLine()) != null) {
            output.add(line);
        }


        return output.get(3);
    }

   public static void toCSV(List<String> list) throws IOException {
       String filePath = "SentimentClassification/file/data.csv";
       FileWriter file = new FileWriter(filePath);

       // 创建CSVPrinter对象
       CSVPrinter csvPrinter = new CSVPrinter( file, CSVFormat.DEFAULT);
       // 将Java列表写入CSV文件
       for (String record : list) {
           csvPrinter.printRecord(record);
       }
       // 关闭CSVPrinter对象
       csvPrinter.close();
   }



   public static String[] getEmotionByAll(String PythonPath, String CSVPath) throws IOException, InterruptedException {
        // 构建进程
       ProcessBuilder pb = new ProcessBuilder("D:/Anaconda/envs/pyt/python.exe", PythonPath, CSVPath);
       pb.redirectErrorStream(true);

       // 启动进程
       Process process = pb.start();

       // 等待进程完成
       int exitCode = process.waitFor();

       // 获取进程的输出
       BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
       String line;
       List<String> output = new ArrayList<>();

       while ((line = reader.readLine()) != null) {
           output.add(line);
       }
       String[] emotion = {output.get(3), output.get(4)};

       return emotion;
   }
}
