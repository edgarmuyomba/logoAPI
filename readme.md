# LogoAPI
This is an api designed to provide company logos. This was developed as a support API to complete the memory game react-exercise of [The Odin Project](https://www.theodinproject.com).

It uses a combination of **TokenAuthentication** and **django-cors-headers** to ensure secure permission handling, authentication and authenticated requests.

## Endpoints
- `api/auth/` Returns a token used to authenticate requests
- `api/{company_name}/` Returns the logo of the specified company if its available
  ```bash
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
  ```bash
  [ ... ]
  ```
- `api/category/{category_name}/` Returns all the logos in the specified category
  ```bash
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
  ```bash
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

## Authetication
Ensure the create an account with the django admin. Currently only superuser accounts are supported. To obtain a token, follow the `api/auth/` endpoint and attach your **username** and **password** to the body of the request
```python
requests.get('http://localhost:8000/api/auth/', json={ "username": ' ... ', "password": ' ... '})
```
After obtaining the token, attach it to each request header.
```python
request.get(path, headers={ "Authorization": 'Token ...' })
```
