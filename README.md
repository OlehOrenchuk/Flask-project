# Варіант 20 (python 3.7.*, pipenv)
### Оренчук Олег
* Клонувати репозиторій
    ```
    git clone https://github.com/OlehOrenchuk/Pipenv-WSGI.git
    ``` 

* Створити віртуальне середовище 
    ```
    pip install --user pipenv
    ``` 
    ```
    setx PATH "%PATH%;C:\Users\Olafus\AppData\Roaming\Python\Python37\Scripts"
    ``` 
    автоматично знайде необхідний інтерпретатор при створенні проекту

* Активувати віртуальне середовище 

    У директорії проекту(Директорія Pipfile.lock і Pipfile) 
    ```
    pipenv shell
    ```
		
* Запустити WSGI сервер 
    ```
    Не потребує запуску. Стартує разом з app.py(встроєний модуль wsgiref.simple_server)
    ```
  
* Перевірити роботу
    ```
    http://127.0.0.1:5000/api/v1/hello-world-20
