
## 1. /artists

### 1-1 **Show Artists**
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
    total_page:15,
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

  * **Code:** 401 Unauthorized <br />
    **Content:** `{ code:"Unauthorized", message : "로그인이 필요합니다." }`



### 1-2 **Insert Artist**
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

  * **Code:** 201 <br />
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
    **Content:** `{ code: "WrongInput", message : "파라미터의 값이 잘못되었습니다" }`

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

  * **Code:** 403 Forbidden <br />
    **Content:** `{ code:"Forbidden", message : "권한이 없습니다." }`


### 1-3 **Delete Artist**
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

  * **Code:** 403 Forbidden <br />
    **Content:** `{ code:"Forbidden", message : "권한이 없습니다." }`

## 2. /artists/:id

### 2-1 **Show Artist**
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

  * **Code:** 401 Unauthorized <br />
    **Content:** `{ code: "Unauthorized", message : "로그인이 필요합니다." }`

 OR

  * **Code:** 404 Not Found <br />
    **Content:** `{ code:"ResourceNotFound", message : "리소스를 찾을 수 없습니다." }`





### 2-2 **Update Artist**
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

  * **Code:** 401 Unauthorized <br />
    **Content:** `{ code:"Unauthorized", message : "로그인이 필요합니다." }`

  OR

  * **Code:** 403 Forbidden <br />
    **Content:** `{ code:"Forbidden", message : "권한이 없습니다." }`



### 2-3 **Delete Artist**
----
해당 Artist 데이터를 삭제합니다.

* **URL**

  /artists/:id

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

  * **Code:** 401 Unauthorized <br />
    **Content:** `{ code:"Unauthorized", message : "로그인이 필요합니다." }`

  OR

  * **Code:** 403 Forbidden <br />
    **Content:** `{ code:"Forbidden", message : "권한이 없습니다." }`


