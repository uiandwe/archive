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
151,
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



##5) art_archive 데이터를 활용한 CRUD 기반의 REST API를 설계 및 Documentation
-------------

url | GET  |  POST  | PUT  |  DELETE
------------ | ------------- | ------------- | ------------- | -------------
/artists | artist 리스트 | artist 추가 | X (사용하지 않음) | 전체 삭제
/artists/:id | 해당 artist 정보 | X (사용하지 않음) | 해당 artist 정보 갱신 | 해당 artist 삭제
/artists/:id/images | 해당 artist의 image 리스트 | image 추가 | X (사용하지 않음) | 해당 artist의 image 전체 삭제
/artists/:id/images/:id | 해당 artist의 image 정보 | X (사용하지 않음) | 해당 image 갱신 | 해당 image 삭제
/images | image 리스트 | image 추가 | X (사용하지 않음) | 전체 삭제
/images/:id | 해당 image 정보 | X (사용하지 않음) | 해당 image 갱신 | 해당 image 삭제

- [artist 관련 문서] (https://github.com/uiandwe/art_archive/blob/master/documentation/artists.md)
- [image 관련 문서] (https://github.com/uiandwe/art_archive/blob/master/documentation/images.md)


##6) TDD를 설명해주세요. 이 개발 방식의 장단점
-------------

TDD는 Test Driven Development의 줄임말로 "테스트 주도적 개발"를 뜻합니다.

TDD는 기존 코드 작성이 완료 된 후 테스트 하는것과 달리 테스트 코드를 작성 후 테스트를 통과하는 실제 코드를 목표로 합니다.

TDD의 절차는 다음과 같습니다.
```
1. 무엇을 테스트 해야 하는지 정의 한다.

2. 실패하는 테스트코드와 성공하는 테스트코드를 작성한다.

3. 테스트 코드에서 실패 및 성공에 부합하는 실제 코드를 작성한다.

4. 위의 단계를 반복한다.
```

프로그램의 시작 단계의 '설계를 완벽하게'가 아닌 느슨하게 만든 다음 테스트를 거치며 지속적인 수정을 통해 프로그램을 완성해 나갑니다.

*장점*
* 단위별 테스트를 통해 구현해야 할 동작에 대해서 정확하게 명시할 수 있습니다.
* 코드가 완성된 후 결함이 있을시 연관된 모든 코드를 재설계하는 상황을 피할수 있습니다.
* 테스트를 통과한 결과물에 대한 리뷰 및 피드백을 통해 추가 구현 및 수정을 빠르게 진행할수 있습니다.

*단점*
* DB, UI, 아직 구현되지 않은 다른 클래스와의 강한 의존성 등이 있을 경우  테스트 코드를 작성하는데 어려움이 있습니다.
* 언어별 다른 테스트 라이블러리 사용과 다양한 테스트 케이스 작성에 따른 초기 진입의 어려움이 있을 수 있습니다.