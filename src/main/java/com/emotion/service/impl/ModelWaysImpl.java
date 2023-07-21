package com.emotion.service.impl;

import com.emotion.service.ModelWays;
import com.emotion.tools.TodoPython;
import org.springframework.stereotype.Service;


@Service
public class ModelWaysImpl implements ModelWays {

    @Override
    public void InitializeCsv() {
        TodoPython.doPython("SentimentClassification/WeiboComments/DataProcessing/DataShuffle_10.py");
    }

    @Override
    public void GetBertWordEmbeddings() {
        TodoPython.doPython("SentimentClassification/WeiboComments/DataProcessing/DataShuffle_10.py");

    }

}
