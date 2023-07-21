package com.emotion;

import com.emotion.service.ModelWays;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class SentimentAnalysisSystemApplicationTests {
   @Autowired
    ModelWays modelWays;
    @Test
    void testInitializeCsv() {
        modelWays.InitializeCsv();
    }

}
