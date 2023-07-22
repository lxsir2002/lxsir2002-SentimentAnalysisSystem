package com.emotion.service.impl;

import com.emotion.service.ModelWays;
import com.emotion.tools.TodoPython;
import org.springframework.stereotype.Service;

import java.io.IOException;


@Service
public class ModelWaysImpl implements ModelWays {

    @Override
    public String GetEmotion(String text) throws IOException, InterruptedException {
        String emotion =  TodoPython.useModel("path", text);
        return emotion;
    }

}
