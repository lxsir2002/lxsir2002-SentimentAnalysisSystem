package com.emotion.tools;


import java.io.IOException;


public final  class TodoPython {
    public static void doPython(String path) throws IOException, InterruptedException {

            // 构建进程
            ProcessBuilder pb = new ProcessBuilder("D:/Anaconda/envs/pyt/python.exe", path);
            pb.redirectErrorStream(true);

            // 启动进程
            Process process = pb.start();

            // 读取进程输出
            java.util.Scanner scanner = new java.util.Scanner(process.getInputStream());
            while (scanner.hasNextLine()) {
                System.out.println(scanner.nextLine());
            }

            // 等待进程结束
            int exitCode = process.waitFor();
            if (exitCode != 0) {
                System.err.println("Python script exited with code " + exitCode);
            }




    }

    public static String useModel(String path, String text) throws IOException, InterruptedException {
        String emotion = null;
        ProcessBuilder pb = new ProcessBuilder("D:/Anaconda/envs/pyt/python.exe", path, text);
        pb.redirectErrorStream(true);
        Process process = pb.start();

        // 读取进程输出
        java.util.Scanner scanner = new java.util.Scanner(process.getInputStream());
        while (scanner.hasNextLine()) {
            System.out.println(scanner.nextLine());
            emotion = scanner.nextLine();
        }

        // 等待进程结束
        int exitCode = process.waitFor();
        if (exitCode != 0) {
            System.err.println("Python script exited with code " + exitCode);
        }
        return emotion;
    }

}
