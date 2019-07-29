# Tradutor de Inteiro para Numero Extenso

Projeto escrito utilizando a linguagem Python3 com o Framework Django 2.2. O intuito deste era participar do Teste de Seleção
da Fundação CERTI.

O limite de intervalo para tradução é [-999999, 999999].

## Instruções para rodar este projeto

### Utilizando o Docker
1° Faça um clone deste repositório:
```
$ git clone https://github.com/bsgabrielsilva/tradutor_inteiro.git
```
2° Em seguida, abra seu terminal dentro da pasta tradutor_inteiro e rode o docker-compose:
```
$ sudo docker-compose up
```
3° Se tudo ocorrer bem, abra seu navegador e digite http://localhost:8000

### Rodando em seu ambiente nativo
#### Requisitos:
- Python 3.6
- pip e setuptools


1° Faça um clone deste repositório:
```
$ git clone https://github.com/bsgabrielsilva/tradutor_inteiro.git
```
2° Em seguida, abra seu terminal e navegue até o diretório onde se encontra o arquivo requirements.txt
e execute o seguinte comando:
```
$ pip install -r requirements.txt
```
3° Se o passo 2° obtiver exito, navegue até o diretório que se encontra o manage.py e execute:
```
$ python manage.py runserver 0.0.0.0:8000
```
4° Se tudo ocorrer bem, abra seu navegador e digite http://localhost:8000

### EXTRAS

Para executar os testes, use o comando:
```
$ python manage.py test app
```
Além disso, boa parte das exceções que poderiam acontecer foram mapeadas, espero que não apareça nenhuma durante o uso :( 
#### Informações importantes
Para usar o aplicativo, você possui duas opções:

- Você pode usar o navegador e acessar a url http://localhost:8000 e no final inserir /(valorInteiro), ex: http://localhost:8000/111
- Você pode usar o curl também para isso: $ curl http://localhost:8000/111

Em ambos os casos, será retornado um objeto json com a resposta:
```
{'extenso': 'cento e onze' }
```

## Considerações finais
Muito obrigado pela oportunidade de participar da seleção! 

## Licença
MIT
