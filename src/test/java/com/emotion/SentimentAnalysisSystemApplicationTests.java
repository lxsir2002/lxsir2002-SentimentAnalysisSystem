package com.emotion;

import com.emotion.dao.Topic;
import com.emotion.service.ModelWays;
import com.emotion.service.Topics;
import com.emotion.service.impl.TopicsImpl;
import com.emotion.tools.TodoPython;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@SpringBootTest
class SentimentAnalysisSystemApplicationTests {
   @Autowired
    ModelWays modelWays;
    @Autowired
    TopicsImpl topicsImpl;
    @Test
    void testDoPython() throws IOException, InterruptedException {
         modelWays.GetEmotion("我好高兴");
    }

    @Test
    void ConvertToCSV() throws IOException {
        List<Topic> list = topicsImpl.list();

        List<String> content = new ArrayList<>();
        for(int i = 0 ; i <list.size(); i++){
            content.add(list.get(i).getTopicComment());
        }

       TodoPython.toCSV(content);
    }

    @Test
    void testCSVPath() throws IOException, InterruptedException {
        String[] emotions = TodoPython.getEmotionByAll("SentimentClassification/getAll.py", "SentimentClassification/file/data.csv");
        for (String emotion : emotions) {
            System.out.println(emotion);
        }
    }

}
