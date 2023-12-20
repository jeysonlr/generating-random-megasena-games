### Para iniciar a aplicação, basta ter Docker e docker-compose instalado em sua máquina.

## Execute o seguinte comando para iniciar a aplicação

```
$ docker compose up -d --build
```

## Para parar a aplicação

```
$ docker compose down
```

## Caso não tenha docker-compose instalado, apenas Docker

```
$ docker build -t flask-random-sequences .

$ docker run -p 5000:5000 flask-random-sequences
```

## Caso queira executar sem o uso de Docker, certifique-se de ter python instalado e pip
```
$ pip install flask

$ python3 app.py
```
