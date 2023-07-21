package com.emotion.service.impl;

import com.emotion.service.ModelWays;
import org.springframework.stereotype.Service;

import java.io.IOException;

@Service
public class ModelWaysImpl implements ModelWays {
    @Override
    public void InitializeCsv() {
                try {
                    // 构建进程
                    ProcessBuilder pb = new ProcessBuilder("D:/Anaconda/envs/pyt/python.exe",
                                                                     "SentimentClassification/WeiboComments/DataProcessing/DataShuffle_10.py");
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
                } catch (IOException | InterruptedException e) {
                    e.printStackTrace();
                }
            }

}
