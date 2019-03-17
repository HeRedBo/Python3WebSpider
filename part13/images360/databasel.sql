
CREATE TABLE `images` (
  `id` varchar(255) NOT NULL DEFAULT  '' COMMENT 'ID',
  `title` varchar(255) NOT NULL DEFAULT  '' COMMENT '图片标题',
  `url` varchar(255) NOT NULL DEFAULT  '' COMMENT '图片链接',
  `thumb` varchar(255) NOT NULL DEFAULT  '' COMMENT '图片缩略图链接',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
) ENGINE=InnoDB  DEFAULT CHARSET=utf8mb4 COMMENT='360爬虫图片存储表';
