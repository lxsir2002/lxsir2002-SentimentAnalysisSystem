package com.emotion.tools;


import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;


public final  class TodoPython {
    public static String doPython(String path, String text) throws IOException, InterruptedException {
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

}
