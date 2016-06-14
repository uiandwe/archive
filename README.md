# art_archive
===================


##3) 다음 작업을 수행하는 SQL query들과 해당 리턴 값을 작성해주시기 바랍니다.
-------------


- ‘제니 오델' 라는 name 을 가진 artist 의 image들의 title들 가져오기
```
SELECT i.title FROM artists as a, images as i
where a.id = i.artist_id
and a.name = '제니 오델';
```
```
result

title
-------
'쓰레기 셀카'
```



- ‘인상주의' artist 의 3개의 image들 가져오기
```
SELECT i.image_url FROM artists as a, images as i
where a.id = i.artist_id
and genre like '%인상주의'
limit 3;
```
```
result

image_url
-------
'http://www.vggallery.com/painting/f_0467.jpg'
'http://www.moma.org/wp/moma_learning/wp-content/uploads/2012/07/Van-Gogh.-Portrait-of-Joseph-Roulin-334x395.jpg'
'http://www.vangogh.net/images/paintings/wheat-field-with-a-reaper.jpg'
```



- images 테이블에 새로운 image 추가하기 (query statement만)
```
Insert into images (image_url, title, year, artist_id, description) Values
("https://en.wikipedia.org/wiki/The_Last_Supper_(Leonardo_da_Vinci)#/media/File:%C3%9Altima_Cena_-_Da_Vinci_5.jpg",
"The Last Supper",
1495,
(select id from artists where id = 151),
"캔버스에 유채");
```


- 가장 많은 image 들을 가진 artist 가져오기
```
SELECT a.* FROM artists as a, images as i
where a.id = i.artist_id
group by artist_id
order by artist_id desc
limit 1;
```

```
result

id    name                birth_year  death_year  country   genre
---   -------------       -----       ----------  -------   --------
151   '레오나르도 다 빈치'    '1452'      '1519'      '이탈리아'    '르네상스'
```


##4) CRUD를 간략하게 설명해주세요
-------------

CRUD는 데이터의 처리 방식으로 Create(생성), Read(읽기), Update(갱신), Delete(삭제)의 앞글자들을 따서 만든 말입니다.

디비와 Rest api에서는 각각 다음과 같이 대응됩니다.
```
단어          sql         Rest api
------      ------      ---------
Create      Insert      Post
Read        select      Get
Update      Update      Put
Delete      Delete      Delete
```

