CREATE TABLE `zsj_blog` (
 `zid` bigint(255) NOT NULL AUTO_INCREMENT COMMENT '博文ID',

 `zuser_id` bigint(20) NOT NULL COMMENT '发表用户ID',

 `zblog_title` text NOT NULL COMMENT '博文标题',

 `zblog_content` longtext NOT NULL COMMENT '博文内容(长文本)',

 `zblog_views` bigint(20) NOT NULL COMMENT '浏览量(大整数)',

 `zblog_comment_count` bigint(20) NOT NULL COMMENT '评论总数(大整数)',

 `zcreate_date` datetime DEFAULT NULL COMMENT '发表时间',

 `zblog_like_count` bigint(20) NOT NULL commit '点赞数量',

 PRIMARY KEY (`zid`),

 KEY `zuser_id` (`zuser_id`),

 CONSTRAINT `blog_user` FOREIGN KEY (`fid`) REFERENCES `zj_users` (`user_id`)

) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;