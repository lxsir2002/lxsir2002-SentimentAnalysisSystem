package com.emotion.dao;

import org.springframework.stereotype.Component;

@Component
public class Topic {
    private Integer id;
    private String TopicName;
    private String TopicComment;

    public Integer getId() {
        return id;
    }

    public String getTopicName() {
        return TopicName;
    }

    public String getTopicComment() {
        return TopicComment;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public void setTopicName(String topicName) {
        TopicName = topicName;
    }

    public void setTopicComment(String topicComment) {
        TopicComment = topicComment;
    }

    @Override
    public String toString() {
        return "Topic{" +
                "id=" + id +
                ", TopicName='" + TopicName + '\'' +
                ", TopicComment='" + TopicComment + '\'' +
                '}';
    }
}
