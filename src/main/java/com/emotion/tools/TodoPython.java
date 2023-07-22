package com.emotion.tools;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;


public final  class TodoPython {
    public static void doPythons(String path, String text) throws IOException, InterruptedException {

            // 构建进程
            ProcessBuilder pb = new ProcessBuilder("E:/TEST/venv/Scripts/python.exe", path,text);
            pb.redirectErrorStream(true);

            // 启动进程
            Process process = pb.start();
            List<String> output = new ArrayList<>();
            // 读取进程输出
            java.util.Scanner scanner = new java.util.Scanner(process.getInputStream());

            while (scanner.hasNextLine()) {
                output.add(scanner.nextLine());
                System.out.println(scanner.nextLine());
            }

            // 等待进程结束
            int exitCode = process.waitFor();
            if (exitCode != 0) {
                System.err.println("Python script exited with code " + exitCode);
            }
        System.out.println("输出值");
        System.out.println(output);
        System.out.println(output.size());
        System.out.println(output.get(0));



    }

    public static void useModel(String path, String text) throws IOException, InterruptedException {
        // 构建进程
        ProcessBuilder pb = new ProcessBuilder("E:/TEST/venv/Scripts/python.exe", path, text);
        pb.redirectErrorStream(true);

        // 启动进程
        Process process = pb.start();

        // 等待进程完成
        int exitCode = process.waitFor();

        // 获取进程的输出
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        String line;
        List<String> output = new ArrayList<>();
       // StringBuilder output = new StringBuilder();
        while ((line = reader.readLine()) != null) {
            output.add(line);
        }


        // 输出进程的返回值和输出
        System.out.println("进程返回值：" + exitCode);
        System.out.println("进程输出：\n" + output.get(3));

    }

    public static String doPython(String path, String text) throws IOException, InterruptedException {
        // 构建进程
        ProcessBuilder pb = new ProcessBuilder("E:/TEST/venv/Scripts/python.exe", path, text);
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

}
