# REST API для Super5

/api/v1/ - префикс для первой версии нашего API ставится перед каждым запросом

/api/v1/o/ - доступ к oauth2, никакие запросы по данному адресу не отсылаются

/api/v1/o/applications/ - форма для регистрирования приложений необходима для получения кодов client_id и client_secret.
Достпна только из браузера, и предварительно нужно пройти авторизацию как пользователь системы, а затем обратиться по
адресу страницы.  Доступ к данной форме через REST сервисы не предусмотрен.
Рекомендуемые параметры client type: confidential, authorization grant type: password.

/api/v1/o/token/ - [POST] сервис необходимы для получения access_token. То есть для обращения к каким либо сервисам
данного приложения сначала необходимо получить access_token

/api/v1/user/ - [GET] получает данные об активном пользователе.

/api/v1/user/info/ - [GET, PUT] получает данные о пользователе, изменяет личные данные пользователя.
/api/v1/user/all_info/ - [GET, PUT] получает полные данные о пользователе, изменяет полные личные данные пользователя.

/api/v1/user/target/ и /api/v1/user/zone/ - [GET, PUT] получение и изменение приоритетов и зон у текущего пользователя.

* В целях тестирования отправки запросов можно использовать консольную утилиту curl, плагин для браузера
firefox — HttpRequester, программу Soap UI или любое другое приложение на Ваше усмотрение.

* Во время отправки запросов необходимо что бы адрес к сервису закрывался слэшем, то есть /api/v1/o/token
является некорректным.

* В данный момент API активно развивается, и если какой либо сервис является недоступным получите актуальную версию
данной документации и поинтересуйтесь в чате.

## /api/v1/o/token/ 
Отсылается запрос вида аутетификация <client_id>: secret_id, данные username=<email>, password=<password> 

Из консоли можно отправить запрос следующего вида:

curl -X POST -d "grant_type=password&username=<email>&password=<password>" -u "<client_id>:<client_secret>" <host>/api/v1/o/token/

curl -X POST --data 'grant_type=password&username=test@test.ru&password=ask3jdhljvdfgzbvnm4hzhv' --user 'WErESLRwlGehlnHLracAdlBp5QVYiWO61KFevpO0:LczFoc3i1FzlhNG7LJpt36BaGzL48JRdO6u0NiamZwscrVnHsFBnNL3cQOqbvOI8fwxar83ejCq4hQb9liaMbNVzlK7HNJwnzGqY3dpOwC25TzfNo5dokb1KKqH32q8h' http://dev.super5.pmlife.me/api/v1/o/token/

curl -X POST -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -d "grant_type=password&username=m@m.ru&password=1" -u "n4ZeLE5Dg7aX8BIuXOwCOfng8PSirPQ8LXHjCprr:cuYVEhG0aXTbjtburuMFNPRwbCHHwUWC1Z3H7imMo4hI3bFBJgSQYy20oCCoUAYZ8eSMRreNYHk9x47HfyB2LVL6YYNslIVt73XZ94lehDuBmPMLPqpudztjxnVxcPNf" http://localhost:8000/api/v1/o/token/

В ответ должен прийти ответ вида:

{
    "expires_in": 36000,
    "refresh_token": "bFXwljkLVcQf24OE0qWJLQQI703V99",
    "access_token": "U2H2Q2Oa9PUmFHsJI9GnNXY76pCv8z",
    "scope": "write read",
    "token_type": "Bearer"
}


Получение нового токена при помощи refresh_token:

curl -X POST -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -d "grant_type=refresh_token&refresh_token=1WH2MjMwv2GiTJAxtcZSWT579z8bPt" -u "LHPuCtXv6Xvm5JFzQC4pOMRiU9Fftg2K3Uev1gL6:LS4cD5WBBEJL1o6Fdn1Lnusv2l2sFML3jYxs0eu2TSYsx0Qz0RDMi0NfYGGpnOv8nJsSe8Z9JKEe5Fsu3WI2ijkTtzOkwvcrj2dBZEX9WHczrfKHfCugpsp6PGI3jxvI" http://localhost:8000/api/v1/o/token/


## /api/v1/user/
Получает данные об активном пользователе.  Необходимо отправить запрос с заголовком  Authorization: Bearer <your_access_token>

Из консоли можно отправить запрос следующего вида:

curl -H "Authorization: Bearer <your_access_token>" <host>/api/v1/user/

curl -X GET -H "Authorization: Bearer <token>" http://dev.super5.pmlife.me/api/v1/user/

curl -H "Authorization: Bearer 3LHalun9RrpGU0jNzp8EbLhJ5uDMcT" http://localhost:8000/api/v1/user/

В ответ должен прийти ответ вида:

[
    {
        "email": "admin@admin.ru",
        "is_staff": true
    }
]

## /api/v1/user/all_info/
[GET] Возвращает подробные данные о пользователе (в том числе и о зонах и приоритетах), необходимо отправить
только заголовок Authorization: Bearer <your_access_token>


## /api/v1/user/info/ 
[GET] Возвращает подробные данные о пользователи, необходимо отправить только заголовок Authorization: Bearer <your_access_token>

curl -H "Authorization: Bearer <your_access_token>" <host>/api/v1/user/info/

curl -H "Authorization: Bearer 3LHalun9RrpGU0jNzp8EbLhJ5uDMcT" http://localhost:8000/api/v1/user/info/

Ответ следующего содержания:

{"height":180,"width":70,"gender":0,"training_duration":"01:00:00","birthday":"1992-11-25","confirmed":false}

[PUT] такой же формат как и у GET запроса, добавляется только набор полей которые необходимо изменить в формате json,
при помощи curl json использовать не надо, нужно лишь перечислить параметры для изменения с ключом -d(--data)

curl -X PUT -H "Authorization: Bearer <your_access_token>" -d <field>=<data>  <host>/api/v1/user/info/

curl -X PUT -H "Authorization: Bearer 3LHalun9RrpGU0jNzp8EbLhJ5uDMcT" -d width=80 -d height=220 http://localhost:8000/api/v1/user/info/

В ответ приходят изменённые данные:

{"height":220,"width":80,"gender":0,"training_duration":"01:00:00","birthday":"1992-11-25","confirmed":false}

* Приятная возможность данные в поле "training_duration" нужно отправлять в текстовом формате, и причём если вы вдруг
превысили какой либо временной интервал, он автоматически пересчитается.
То есть, если отправить   "training_duration":"30:40:90", то в ответ мы получим уже скорректированный временной
интервал "training_duration": "1 06:41:30"(секунды перешли в минуты, а  часы в дни).

## /api/v1/user/target/ и /api/v1/user/zone/
в текущей версии API данные методы работают схожим образом, поэтому перечисляются вместе, и здесь рассматриваются
на примере приоритетных зон

[GET] Возвращает набор данных установленный для данного пользователя, либо приоритет целей, либо приоритет зон. 

curl -H "Authorization: Bearer <your_access_token>" <host>/api/v1/user/zone/

curl -H "Authorization: Bearer 3LHalun9RrpGU0jNzp8EbLhJ5uDMcT" http://localhost:8000/api/v1/user/zone/

В ответ приходит информация по зонам/приоритетам

[{"priority":1,"zone_priority":{"name":"Спина"}},{"priority":2,"zone_priority":{"name":"Руки"}},{"priority":3,"zone_priority":{"name":"Грудь"}},{"priority":4,"zone_priority":{"name":"Пресс-талия"}},{"priority":5,"zone_priority":{"name":"Ноги и ягодицы"}}]

[PUT] Устанавливает приорит зоне, подразумевается что приоритет 1 является максимальным, и в данный момент можно
изменять только по одному приоритету за запрос.

curl -H "Authorization: Bearer <your_access_token>" -H "Content-Type: application/json" -X PUT -d <data in json format> <host>/api/v1/user/zone/

curl -H "Authorization: Bearer 3LHalun9RrpGU0jNzp8EbLhJ5uDMcT" -H "Content-Type: application/json" -X PUT -d '{"priority":7,"zone_priority":{"name":"Руки"}}' http://localhost:8000/api/v1/user/zone/

При корректном запросе в ответ приходит приоритет с изменёнными данными: 

{"priority":7,"zone_priority":{"name":"Руки"}}

## /api/v1/user/day_week/
Записывает дни недели в личные данные юзера.

[PUT] нужно указать параметр week_day с ключом -d(--data):

curl -X PUT -H "Authorization: Bearer <your_access_token>" -d <week_day>=<data>  <host>/api/v1/user/day_week/

curl -X PUT -H "Authorization: Bearer 3LHalun9RrpGU0jNzp8EbLhJ5uDMcT" -d week_day=[0,1,2,3,4] http://localhost:8000/api/v1/user/day_week/

В ответ приходят дни недели, которые были записаны для юзера:

 {
 	"week_day":"[0,1,2,3,4]"
 }
 

## /api/v1/routed/training/
Отдает пользователю пользователю тренировки, доступно через веб-интерфейс. Можно получить как историю, так и будущие тренировки при помощи фильтра по дате: /api/v1/routed/training/?from_date=2015-10-04&to_date=2015-10-06 . Даты отдаются, включая границы фильтра.

## /api/v1/routed/register-user/
Дает пользователю возможность зарегистрироваться по логину-паролю. Доступно через веб-интерфейс.