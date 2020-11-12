# decathlon_project

<p>This project is made for recruitment process for Decathlon and uses Django REST FRAMEWORK</p>

<h1>Instalation process</h1>

<p>Please folow this instalation guide for this project</p>
<p>1. Clone this repository and go to decathlon folder </p>

```
git clone https://github.com/steven0seagal/decathlon_project.git
cd decathlon_project
```
<p>2. Start new virtual environment and activate </p>

```
python3 -m venv venv
source venv/bin/activate
```

<p>3. Install libraries from requirements </p>

```
pip3 install -r requirements.txt
```

<p>4. Go to movies folder and migrate data</p>

```
cd movies
python3 manage.py migrate
```
<p>5. Run server</p>

```
python3 manage.py runserver
```

<h1>Usage</h1>
<p>Below are listed all functionalities of this project and how to call them via curl command it is better to download first few movie data to understand all commands</p>

<p>Download data from server and save to object</p>

```
curl -X POST -H 'Content-Type: application/json' -d '{"title":"shrek"}' http://localhost:8000/movies/
```
<p>Recieve all data from database</p>

```
 curl -X GET -H 'Content-Type: application/json' http://localhost:8000/movies/
```

<p>Recieve data from database order by some field (example year) default ascending if descending put "-year"</p>

```
 curl -X GET -H 'Content-Type: application/json' -d '{"order_by":"year"}' http://localhost:8000/movies/
```

<p>Recieve data from database filter by some field and field value</p>

```
curl -X GET -H 'Content-Type: application/json' -d '{"filter_field":"genre", "filter_value":"Romance"}' http://localhost:8000/movies/
```
<p>Recieve data from database filter and order</p>

```
curl -X GET -H 'Content-Type: application/json' -d '{"filter_field":"genre", "filter_value":"Romance","order_by":"year"}' http://localhost:8000/movies/
```

<p>Download data from server and save to object</p>

```
curl -X POST -H 'Content-Type: application/json' -d '{"title":"shrek"}' http://localhost:8000/movies/
```

<p>Delete movie by its id (in this case id = 10)</p>

```
curl -X DELETE -H 'Content-Type: application/json'  http://localhost:8000/movies/10
```

<p>Update one selected field in one selected movie (in this case id = 11 and field to update is year) by downloading reference data from other server</p>

```
curl -X PUT -H 'Content-Type: application/json' -d '{"field":"year"}' http://localhost:8000/movies/11/
```

<p>Get all comments from whole database</p>

```
curl -X GET -H 'Content-Type: application/json' http://localhost:8000/comments/
```

<p>Get comments from only one movie by movie id (in this case id = 4)</p>

```
curl -X GET -H 'Content-Type: application/json' -d '{"id":"4"}' http://localhost:8000/comments/ 
```
<p>Post one comment to selected movie by its id (in this case id = 4, comment = 'test comment') </p>

```
curl -X POST -H 'Content-Type: application/json' -d '{"id":"4", "comment":"test comment"}' http://localhost:8000/comments/ 
```

<p>Get top three movies based on comments number, with defined movie range (in this case script will select movies between 1993 and 2020) </p>

```
curl -X GET -H 'Content-Type: application/json' -d '{"from":"1990", "to":"2020"}' http://localhost:8000/top/ 
```