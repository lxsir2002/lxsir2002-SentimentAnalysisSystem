package com.emotion.service;

import com.emotion.tools.TodoPython;

import java.io.IOException;

public interface ModelWays {

    public String GetEmotion(String text) throws IOException, InterruptedException;

}
