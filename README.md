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

**Show Artists**
----
  Artist 데이터를  json형태로 리턴합니다.

* **URL**

  /artists

* **Method:**

  `GET`

*  **URL Params**

   **Required:**
	 None
   **Optional:**
- page=[integer]
- filed=[string],[string],...
    - 원하는 content 데이터만 있을 경우 content key값 입력
    - example: /artists/?filed=id,name

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    `{
    page:1,
    totle_page:15,
    data:[{
      "birth_year" : 1853,
      "country" : "네더란드",
      "death_year" : 1890,
      "genre" : "후기 인상주의",
      "id" : 102,
      "name" : "빈센트 반 고흐"
    },
    {
      "birth_year" : 1866,
      "country" : "프랑스",
      "death_year" : 1944,
      "genre" : "표현주의",
      "id" : 103,
      "name" : "바실리 칸딘스키"
    },...]
    }`

* **Error Response:**

  * **Code:** 400 Bad Request <br />
    **Content:** `{ code: "UnknownFiled", message : "잘못된 파라미터 요청입니다." }`

 OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ code:"Unauthorized", message : "로그인이 필요합니다." }`



**Insert Artist**
----
새로운  Artist 데이터를  입력합니다.

* **URL**

  /artists

* **Method:**

  `POST`

*  **URL Params**

   **Required:**
	 None
* **Data Params**
    - name (string, max 45 charter)
    - birth_year (int)
    - death_year (int)
    - country (string, max 45 charter)
    - genre  (string, max 45 charter)


* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    `{
      "birth_year" : 1853,
      "country" : "네더란드",
      "death_year" : 1890,
      "genre" : "후기 인상주의",
      "id" : 152,
      "name" : "빈센트 반 고흐"
    }`

* **Error Response:**

  * **Code:** 400 Bad Request <br />
    **Content:** `{ code: "OutOfRangeInput", message : "파라미터의 값이 최대 제한 범위를 넘었습니다" }`

  OR

  * **Code:** 400 Bad Request <br />
    **Content:** `{ code: "InvalidInput", message : "파라미터의 데이터형이 맞지 않습니다" }`

  OR

  * **Code:** 400 Bad Request <br />
    **Content:** `{ code: "NotInput", message : "파라미터의 데이터가 없습니다." }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ code:"Unauthorized", message : "로그인이 필요합니다." }`

  OR

  * **Code:** 403 UNAUTHORIZED <br />
    **Content:** `{ code:"Forbidden", message : "권한이 없습니다." }`


**Delete Artist**
----
Artist 데이터를 모두 삭제합니다.

* **URL**

  /artists

* **Method:**

  `Delete`

*  **URL Params**

   **Required:**
	 None
* **Data Params**
	None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    `{
      message : "삭제를 완료하였습니다."
    }`

* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ code:"Unauthorized", message : "로그인이 필요합니다." }`

  OR

  * **Code:** 403 UNAUTHORIZED <br />
    **Content:** `{ code:"Forbidden", message : "권한이 없습니다." }`



**Show Artist**
----
하나의 Artist 데이터를 리턴합니다.

* **URL**

  /artists/:id

* **Method:**

  `Get`

*  **URL Params**

   **Required:**
	 `id=[integer]`
* **Data Params**
	None

* **Success Response:**

  * **Code:** 200 <br />

    **Content:**
    `{
    data:{
      "birth_year" : 1853,
      "country" : "네더란드",
      "death_year" : 1890,
      "genre" : "후기 인상주의",
      "id" : 102,
      "name" : "빈센트 반 고흐"
    }
    }`

* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ code: "Unauthorized", message : "로그인이 필요합니다." }`

 OR

  * **Code:** 404 UNAUTHORIZED <br />
    **Content:** `{ code:"ResourceNotFound", message : "리소스를 찾을 수 없습니다." }`





**Update Artist**
----
  해당 Artist 데이터를  갱신합니다.

* **URL**

  /artists/:id

* **Method:**

  `PUT`

*  **URL Params**

   **Required:**
	 None
* **Data Params**
    - name (string, max 45 charter)
    - birth_year (int)
    - death_year (int)
    - country (string, max 45 charter)
    - genre  (string, max 45 charter)


* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    `{
      "birth_year" : 1853,
      "country" : "네더란드",
      "death_year" : 1890,
      "genre" : "후기 인상주의",
      "id" : 152,
      "name" : "빈센트 반 고흐"
    }`

* **Error Response:**

  * **Code:** 400 Bad Request <br />
    **Content:** `{ code: "OutOfRangeInput", message : "파라미터의 값이 최대 제한 범위를 넘었습니다" }`

  OR

  * **Code:** 400 Bad Request <br />
    **Content:** `{ code: "InvalidInput", message : "파라미터의 데이터형이 맞지 않습니다" }`

  OR

  * **Code:** 400 Bad Request <br />
    **Content:** `{ code: "NotInput", message : "파라미터의 데이터가 없습니다." }`

  OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ code:"Unauthorized", message : "로그인이 필요합니다." }`

  OR

  * **Code:** 403 UNAUTHORIZED <br />
    **Content:** `{ code:"Forbidden", message : "권한이 없습니다." }`



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