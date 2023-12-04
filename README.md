# EasyRPN
An easy single page app for a RPN calculator. Using FastAPI and PostgreSQL.
Deployment via Docker

## Prerequisites

Git, Python 3, Pip, Docker, Docker Compose

## Installation

1. Clone this repository
```sh
git clone https://github.com/bennychoubros/EasyRPN.git
```
2. Go to folder
```sh
cd EasyRPN
```

3. Build the images

```sh
$ docker-compose up -d --build
```
4. Test it in your browser [http://localhost:8008/](http://localhost:8008/)

5. You can test the App with Pytest as well
```sh
$ docker exec -it easyrpn-backend-1 pytest -v 
```

## Documentation

All routes are available on `/docs` or `/redoc` paths with Swagger or ReDoc.

### Features

EasyRPN is an API for a RPN calculator.
- You can create a new operation and save it in DB
- You can retrieve all past operations saved in DB and download it in a csv file

### Warning

Proper Frontend for the API is not implemented yet.
If you wish to check out the existing design,
just try :
1. `cd frontend`
2. `npm start`
3. Check it in your browser on [http://localhost:3000/](http://localhost:3000/) ;).

## Security warning

If you use this project, it is recommended to modify the environment variables listed in `.env` sample file.

## TODO

1. Implement a Testing Database for Unit Testing

2. Implement a React Frontend

3. Implement Traefik and DockerFile_prod for deployment

## Contributions

Any feature requests and pull requests are welcome!

## License

The project is under [MIT license](https://choosealicense.com/licenses/mit/).
