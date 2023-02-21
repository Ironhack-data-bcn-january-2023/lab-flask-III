![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

## Introduction

On this lab, you will continue working on the API you created on the previous lab. On this lab, you will create a connection to a MySQL database.

The goal is to have this workflow:

Browser endpoints < function defined under endpoint < function that queries < function that establishes connection

This way, we will manage to run SQL queries by just passing one word/one endpoint.

### Iteration 1

Copy the API you created. It should look like this:

```bash
your-code/
    main.ipynb
.gitignore
README.md

small-api/
    main.py
    config/
        sql_connection.py
    tools/
        sql_queries.py
```
- Make sure you also have a `.env`
- From your terminal, run: `python main.py`
- In that terminal, you'll get feedback of your prints and the errors.
- After the server is up and running you'll be able to go into your browser and access the endpoints you defined.

### Iteration 2

You now have an API that runs queries based on parameters. Now, we will seed a database. We do this through POST methods.

Post methods can only be done through python. Open a jupyter notebook and have two cells: one for importing requests and another one to do the requests.post:

```python
requests.post("http://127.0.0.1:9000/insert-into-employees", params = params)
```

1. Create a route with the endpoint: `"/insert-into-employees"`
2. Define a function in `tools/sql_queries.py` that that will receive as arguments whatever you want to insert.
3. Call that function under another one below your route.
4. From python, create a dictionary named params where each key you're passing is the name of the column and each value will be your inserted value. Then:

```python
requests.post("http://127.0.0.1:9000/insert-into-employees", params = params)
```

### Iteration 3

Create and parametrize as many endpoints as you find useful. Is there some aggregations you can do?

### Iteration 4

1. Choose a database: a csv of your liking
2. Upload that database to [free sql database](https://www.freesqldatabase.com/)
3. Establish a connection to your database through Workbench to your db on the cloud
4. You can now upload your table, either manually or through python. If manually doesn't work, do it through python
6. To do it through python, you will need mysql alchemy and a connection string: `f"mysql+pymysql://{user}:{password}@sql7.freesqldatabase.com/{name}"`

### BONUS

Deploy your API to [heroku](https://devcenter.heroku.com/articles/git). This will allow you to have your API up and running on a remote address.

## Submission

Upon completion, add your deliverables to git. Then commit git and push your branch to the remote.
