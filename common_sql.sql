/*
	用户注册数(根据渠道划分)
	根据年月日分组
*/
	
SELECT 
	count(*) as allnum,created, FROM_UNIXTIME(created) AS createtime,
	FROM_UNIXTIME(created, '%Y-%m-%d') AS createdata, 'pc注册' as columnname
FROM `user` 
WHERE
created > UNIX_TIMESTAMP(DATE_SUB(CURDATE(), INTERVAL 100 DAY))
and register_channel='pc'
GROUP BY createdata
union all
(
	SELECT 
		count(*) as allnum,created, FROM_UNIXTIME(created) AS createtime,
		FROM_UNIXTIME(created, '%Y-%m-%d') AS createdata, '安卓' as columnname
	FROM `user` 
	WHERE
	created > UNIX_TIMESTAMP(DATE_SUB(CURDATE(), INTERVAL 100 DAY))
	and register_channel ='android'
	GROUP BY createdata
)
union all
(
	SELECT 
		count(*) as allnum,created, FROM_UNIXTIME(created) AS createtime,
		FROM_UNIXTIME(created, '%Y-%m-%d') AS createdata, 'ios' as columnname
	FROM `user` 
	WHERE
	created > UNIX_TIMESTAMP(DATE_SUB(CURDATE(), INTERVAL 100 DAY))
	and register_channel ='ios'
	GROUP BY createdata
)
union all
(
	SELECT 
		count(*) as allnum,created, FROM_UNIXTIME(created) AS createtime,
		FROM_UNIXTIME(created, '%Y-%m-%d') AS createdata, '总和' as columnname
	FROM `user` 
	WHERE
	created > UNIX_TIMESTAMP(DATE_SUB(CURDATE(), INTERVAL 100 DAY))
	GROUP BY createdata
)