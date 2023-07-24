package com.emotion.service.impl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.emotion.dao.Topic;
import com.emotion.mapper.TopicMapper;
import com.emotion.service.Topics;
import org.springframework.stereotype.Service;

@Service
public class TopicsImpl extends ServiceImpl<TopicMapper, Topic > implements Topics {
}
