# CutOfWood
 
Для запуска требуется:
1) git clone https://github.com/00MRX00/CutOfWood.git           // Клонируем рупозиторий
2) cd CutOfWood                                                 // Переходим в папку с проектом
3) docker-compose up                                            // Собираем образ с бэкендом и запускаем его
4) cd CutOfWood/frontend                                        // Переходим в папку с фронтендом
5) npm install                                                  // Установка необходимых пакетов
6) npm run start                                                // Запускаем клиент


Список доступных API:
1) RegisterAPI                                                  // Регистрация
    URL: http://localhost:8000/api/auth/register
    Method: POST
    Headers: Content-Type: application/json
    Fields:
    {
        "email": "test@test.ru",      	                        // email пользователя
 	    "username": "test",                                     // никнейм пользователя
 	    "first_name": "Тест",                                   // Имя
 	    "last_name": "Тестов",        	                        // Фамилия
 	    "patronymic": "Тестович",     		                    // Отчество
 	    "phone_number": "+79061234565",                     	// Номер телефона
        "password": "123456"                                    // Пароль
    }

2) LoginAPI                                                     // Авторизация
    URL: http://localhost:8000/api/auth/login
    Method: POST
    Headers: Content-Type: application/json
    Fields:
    {
        "email": "test@test.ru",                                // Email
        "password": "123456"                                    // Пароль
    }

3) LogoutAPI                                                    // Выход
    URL: http://localhost:8000/api/auth/logout
    Method: POST
    Headers: Authorization: Token [токен пользователя]
    
4) UserAPI                                                      // Информация о пользователе по его токену
    URL: http://localhost:8000/api/user
    Method: GET
    Headers: Authorization: Token [токен пользователя]

5) UsersListView                                                // Список пользователей с их данными (не использовать на фронте)
    URL: http://localhost:8000/api/users
    Method: GET
    Headers: Authorization: Token [токен пользователя]