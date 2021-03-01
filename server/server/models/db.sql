
-- user用户个人信息表
CREATE TABLE user (
  account varchar(10) NOT NULL,
  nick_name varchar(20) NOT NULL,
  password varchar(20) NOT NULL,
  tel varchar(13) DEFAULT NULL,
  register_time datetime DEFAULT NULL,
  update_time datetime default  NULL ,
  PRIMARY KEY (`account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8




-- person_game_info个人答题信息记录
-- 字段说明
--id 自增主键
-- user_id 用户id
-- level_grade 用户等级
-- integral_score 用户积分
-- win_rate 胜率（胜利次数/比赛次数）
-- win_num 胜利次数
-- streak_num 最大连胜次数
-- contest_num 比赛次数
-- average_score 平均成绩
-- average_time 平均用时
-- correct_rate 平均总正确率
-- rescue_rate 救援知识答题正确率（本次正确率+以往正确率/总共比赛次数）
-- structure_rate 构造知识答题正确率
-- predict_rate 预测预警知识答题正确率
create table if not exists person_game_info(
--  id INT NOT NULL AUTO_INCREMENT,
  user_id varchar (10) not null ,
  level_grade smallint default 0,
  integral_score int default 0,
  win_rate decimal (3,2) default 0.00,
  win_num int default 0,
  streak_num int default 0,
  contest_num int default 0,
  average_score int default 0,
  average_time int default 0,
  correct_rate decimal (3,2) default 0.00,
  rescue_rate decimal (3,2) default 0.00,
  structure_rate decimal (3,2) default 0.00,
  predict_rate decimal (3,2) default 0.00,
  primary key (user_id),
  foreign key (user_id) references user(account)
  on delete cascade
  on update cascade ,
)ENGINE=InnoDB default charset=utf8 ;


-- 比赛信息表，储存全部比赛记录
create table if not exists contest_info(
  id INT NOT NULL AUTO_INCREMENT,
  userA_id varchar (10) not null,
  userB_id varchar (10) not null,
  winer_id varchar (10) not null,
  userA_score smallint not null ,
  userB_score smallint not null ,
  start_time datetime not null ,
  end_time datetime not null,
  primary key(id),
  foreign key (userA_id) references user(account),
  foreign key (userB_id) references user(account),
  foreign key (winer_id) references user(account)
)ENGINE=InnoDB default charset=utf8 ;



--question_set考题信息
CREATE TABLE  earthquake_structure(
    id INT NOT NULL AUTO_INCREMENT,
    question_info JSON,
    PRIMARY KEY(id)

)ENGINE=InnoDB default charset=utf8 auto_increment=1;
# create table if not exists question_info(
#   title varchar(30) not null ,
#   choice text not null ,
#   result char(1) not null
#   is_single char(1) not null ,
#   primary key (title))ENGINE =InnoDB default charset =utf8





insert into user(account, nick_name, password, tel, register_time) values (04171224,'Steve',000,119,'2019-9-28')

insert into user(account, nick_name, password, tel, register_time) values (%s,%s,%s,%s,%s)',('04171225','xiaoming','0000','233','2019-9-22')


