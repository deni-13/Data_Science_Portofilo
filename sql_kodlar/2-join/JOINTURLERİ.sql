select * from users u
inner join adresses a on a.user_id=u.id
--innner join =join
select * from users u

--left 

select * from users u
left join adresses a on a.user_id=u.id


select u.username_,a.city from users u
right join adresses a on a.user_id=u.id



select u.username_,a.city from users u
full join adresses a on a.user_id=u.id


