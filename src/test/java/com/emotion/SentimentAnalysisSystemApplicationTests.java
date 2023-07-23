package com.emotion;

import com.emotion.service.ModelWays;
import com.emotion.tools.TodoPython;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.io.IOException;

@SpringBootTest
class SentimentAnalysisSystemApplicationTests {
   @Autowired
    ModelWays modelWays;
    @Test
    void testDoPython() throws IOException, InterruptedException {
         modelWays.GetEmotion("我好高兴");
    }

}
