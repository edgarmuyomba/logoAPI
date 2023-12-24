# LogoAPI
This is an api designed to provide company logos. This was developed as a support API to complete the memory game react-exercise of [The Odin Project](https://www.theodinproject.com/lessons/node-path-react-new-memory-card).

It uses a combination of **TokenAuthentication** and **django-cors-headers** to ensure secure permission handling, authentication and authenticated requests.

## Endpoints
- `api/auth/` Returns a token used to authenticate requests
- `api/{company_name}/` Returns the logo of the specified company if its available
  ```
  [
    {
        id
        company
        imageUrl
        category
    }
  ]
  ```
- `api/categories/` Returns all the available categories
  ```
  [ ... ]
  ```
- `api/category/{category_name}/` Returns all the logos in the specified category
  ```
  [
    {
        id
        company
        imageUrl
        category
    },
    ...
  ]
  
  ```
- `api/random/{num}` Returns the specified number of random logos 
  ```
  [
    {
        id
        company
        imageUrl
        category
    },
    ...
  ]
  ```

## Setting up dev
1. Clone the repository into your desired directory
   ```bash
   git clone <url>
   ```
2. Enter the created folder `logoAPI` using the terminal
   ```bash
   cd logoAPI
   ```
3. Create and activate a virtual environment using python
   ```bash
   python -m venv <env> && env\scripts\activate
   ```
4. Install the necessary requirements
   ```bash
   pip install -r requirements.txt
   ```
5. Create a `.env` file in the base directory of the project and add a secret key 
6. Run the server
   ```bash
   python manage.py runserver
   ```

## Authetication
Ensure the create an account with the django admin. Currently only superuser accounts are supported. To obtain a token, follow the `api/auth/` endpoint and attach your **username** and **password** to the body of the request
```python
requests.get('http://localhost:8000/api/auth/', json={ "username": ' ... ', "password": ' ... '})
```
After obtaining the token, attach it to each request header.
```python
request.get(path, headers={ "Authorization": 'Token ...' })
```
## Django-Cors-headers
This ensures that only accepted http requests are made to the server.