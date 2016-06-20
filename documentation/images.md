
## 3. /artists/:id/images

### 3-1 **Show Image**
----
해당  Artist의 image 데이터들을 리턴합니다.

* **URL**

  /artists/:id/images

* **Method:**

  `GET`

*  **URL Params**

   **Required:**
	 None
   **Optional:**
- page=[integer]
- filed=[string],[string],...
    - 원하는 content 데이터만 있을 경우 content key값 입력
    - example: /artists/1/images?filed=id,image_url,title

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    `{
    page:1,
    totle_page:6,
    data:[{
      "id" : 1,
      "image_url"  : "http://www.vggallery.com/painting/f_0467.jpg",
      "title" : "밤의 카페 테라스",
      "year" : 1888,
      "arist_id" : 102,
      "description" : "캔버스에 유채"
    },
    {
      "id" : 2,
      "image_url"  : "http://www.wassilykandinsky.net/images/works/370.jpg,
      "title" : "동심원들과 정사각형들",
      "year" : 1913,
      "arist_id" : 102,
      "description" : "수채, 과슈, 초크"
    },...]
    }`

* **Error Response:**

  * **Code:** 400 Bad Request <br />
    **Content:** `{ code: "UnknownFiled", message : "잘못된 파라미터 요청입니다." }`

 OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ code:"Unauthorized", message : "로그인이 필요합니다." }`

 OR

  * **Code:** 404 UNAUTHORIZED <br />
    **Content:** `{ code:"ResourceNotFound", message : "리소스를 찾을 수 없습니다." }`



### 3-2 **Insert Image**
----
Artist의 새로운 image 데이터를  입력합니다.

* **URL**

  /artists/:id/images

* **Method:**

  `POST`

*  **URL Params**

   **Required:**
	 None
* **Data Params**
    - image_url (string, max 255 charter)
    - title (string, max 255 charter)
    - year (int)
    - artist_id (int)
    - description (string, max 255 charter)


* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    `{
      "id" : 66,
      "image_url"  : "http://www.wassilykandinsky.net/images/works/370.jpg,
      "title" : "동심원들과 정사각형들",
      "year" : 1913,
      "arist_id" : 103,
      "description" : "수채, 과슈, 초크"
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




### 3-3  **Delete iamge**
----
해당 Artist의 image 데이터들을 모두 삭제합니다.

* **URL**

  /artists/:id/images

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





## 4. /artists/:id/images/:id
### 4-1 **Show Image**
----
해당 Artist의 하나의 image 데이터를 리턴합니다.

* **URL**

  /artists/:artist_id/images/:image_id

* **Method:**

  `Get`

*  **URL Params**

   **Required:**
	 `artist_id=[integer]
	 image_id=[interger]`

* **Data Params**
	- filed=[string],[string],...
    - 원하는 content 데이터만 있을 경우 content key값 입력
    - example: /artists/1/images/1?filed=id,image_url...

* **Success Response:**

  * **Code:** 200 <br />

    **Content:**
    `{
    data:{
      "id" : 1,
      "image_url"  : "http://www.vggallery.com/painting/f_0467.jpg",
      "title" : "밤의 카페 테라스",
      "year" : 1888,
      "arist_id" : 102,
      "description" : "캔버스에 유채"
    }
    }`

* **Error Response:**
	* **Code:** 400 Bad Request <br />
    **Content:** `{ code: "UnknownFiled", message : "잘못된 파라미터 요청입니다." }`

 OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ code: "Unauthorized", message : "로그인이 필요합니다." }`

 OR

  * **Code:** 404 UNAUTHORIZED <br />
    **Content:** `{ code:"ResourceNotFound", message : "리소스를 찾을 수 없습니다." }`




### 4-2 **Update Image**
----
  Artist의 해당 image 데이터를  갱신합니다.

* **URL**

  /artists/:artist_id/images/:image_id

* **Method:**

  `PUT`

*  **URL Params**

   **Required:**
	 None
* **Data Params**
    - image_url (string, max 255 charter)
    - title (string, max 255 charter)
    - year (int)
    - artist_id (int)
    - description (string, max 255 charter)

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    `{
      "id" : 66,
      "image_url"  : "http://www.wassilykandinsky.net/images/works/370.jpg,
      "title" : "동심원들과 정사각형들",
      "year" : 1913,
      "arist_id" : 103,
      "description" : "수채, 과슈, 초크"
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



### 4-3 **Delete Image**
----
artist의 해당 Image 데이터를 삭제합니다.

* **URL**

  /artists/:artist_id/images/:image_id

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



## 5. /images
### 5-1 **Show Image**
----
image 데이터들을 리턴합니다.

* **URL**

  /images

* **Method:**

  `GET`

*  **URL Params**

   **Required:**
	 None
   **Optional:**
- page=[integer]
- filed=[string],[string],...
    - 원하는 content 데이터만 있을 경우 content key값 입력
    - example: /artists/1/images?filed=id,image_url,title

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    `{
    page:1,
    totle_page:6,
    data:[{
      "id" : 1,
      "image_url"  : "http://www.vggallery.com/painting/f_0467.jpg",
      "title" : "밤의 카페 테라스",
      "year" : 1888,
      "arist_id" : 102,
      "description" : "캔버스에 유채"
    },
    {
      "id" : 2,
      "image_url"  : "http://www.wassilykandinsky.net/images/works/370.jpg,
      "title" : "동심원들과 정사각형들",
      "year" : 1913,
      "arist_id" : 103,
      "description" : "수채, 과슈, 초크"
    },...]
    }`

* **Error Response:**

  * **Code:** 400 Bad Request <br />
    **Content:** `{ code: "UnknownFiled", message : "잘못된 파라미터 요청입니다." }`

 OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ code:"Unauthorized", message : "로그인이 필요합니다." }`

 OR

  * **Code:** 404 UNAUTHORIZED <br />
    **Content:** `{ code:"ResourceNotFound", message : "리소스를 찾을 수 없습니다." }`



### 5-2 **Insert Image**
----
새로운 image 데이터를  입력합니다.

* **URL**

/images

* **Method:**

  `POST`

*  **URL Params**

   **Required:**
	 None
* **Data Params**
    - image_url (string, max 255 charter)
    - title (string, max 255 charter)
    - year (int)
    - artist_id (int)
    - description (string, max 255 charter)


* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    `{
      "id" : 66,
      "image_url"  : "http://www.wassilykandinsky.net/images/works/370.jpg,
      "title" : "동심원들과 정사각형들",
      "year" : 1913,
      "arist_id" : 103,
      "description" : "수채, 과슈, 초크"
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




### 5-3 **Delete iamge**
----
 image 데이터들을 모두 삭제합니다.

* **URL**

/images

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





## 6. /images/:id
### 6-1 **Show Image**
----
하나의 image 데이터를 리턴합니다.

* **URL**

/images/:id

* **Method:**

  `Get`

*  **URL Params**

   **Required:**
	 `artist_id=[integer]
	 image_id=[interger]`

* **Data Params**
	- filed=[string],[string],...
    - 원하는 content 데이터만 있을 경우 content key값 입력
    - example: /artists/1/images/1?filed=id,image_url...

* **Success Response:**

  * **Code:** 200 <br />

    **Content:**
    `{
    data:{
      "id" : 1,
      "image_url"  : "http://www.vggallery.com/painting/f_0467.jpg",
      "title" : "밤의 카페 테라스",
      "year" : 1888,
      "arist_id" : 102,
      "description" : "캔버스에 유채"
    }
    }`

* **Error Response:**
	* **Code:** 400 Bad Request <br />
    **Content:** `{ code: "UnknownFiled", message : "잘못된 파라미터 요청입니다." }`

 OR

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ code: "Unauthorized", message : "로그인이 필요합니다." }`

 OR

  * **Code:** 404 UNAUTHORIZED <br />
    **Content:** `{ code:"ResourceNotFound", message : "리소스를 찾을 수 없습니다." }`




### 6-1 **Update Image**
----
  Artist의 해당 image 데이터를  갱신합니다.

* **URL**

  /images/:_id

* **Method:**

  `PUT`

*  **URL Params**

   **Required:**
	 None
* **Data Params**
    - image_url (string, max 255 charter)
    - title (string, max 255 charter)
    - year (int)
    - artist_id (int)
    - description (string, max 255 charter)

* **Success Response:**

  * **Code:** 200 <br />
    **Content:**
    `{
      "id" : 66,
      "image_url"  : "http://www.wassilykandinsky.net/images/works/370.jpg,
      "title" : "동심원들과 정사각형들",
      "year" : 1913,
      "arist_id" : 103,
      "description" : "수채, 과슈, 초크"
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



### 6-1 **Delete Image**
----
artist의 해당 Image 데이터를 삭제합니다.

* **URL**

/images/:id

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


