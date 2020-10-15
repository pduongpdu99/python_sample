# Django review
----

### What
- Web Framework (Python + core)


### How do
- MVT - Model View Template
	+ Model <- Class, Object, Function, Library <- request
	+ View -> Display
	+ template <- Any "Biểu diễn" 
		+ Pure: general (chung) -> also reusable

### Advantage
- Linh hoạt
- Đơn giản
- Hạn chế re-code
- Supported by py libs

### Install
* Condition: Python, path environment variable (py) | pip (terminal)

- Use terminal:
	
 đặt django
```
py -m pip install django[==<version>]

```
Notice: [==version] - [default] last version | [custome] early version

Bắt đầu một project với Django
```
django-admin startproject <name_project>
```
Bắt đầu một app trong project
```
cd <name_project>
django-admin startapp <name_app>

```

Run: (the position at name_project)
```
py manage.py runserver
	
```

Tạo một DB:
```
py manage.py migrate
```
