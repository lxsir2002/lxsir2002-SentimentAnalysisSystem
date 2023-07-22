package com.emotion.controller;

import com.emotion.service.ModelWays;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;

@RestController
@RequestMapping("/class")
public class ModelController {
    @Autowired
    private ModelWays modelWays;

    @GetMapping("/{text}")
    public String AnalyzeEmotion(@PathVariable String text) throws IOException, InterruptedException {
        System.out.println(text);
//        String emotion = modelWays.GetEmotion(text);

         return "lx";
    }

}
