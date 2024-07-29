# API Daily Diet

Esta API foi desenvolvida como uma atividade prática do curso de Python da Rockeatseat.

A API é capaz de adicionar, pegar, atualizar e deletar refeições dentro de um banco SQLite.
Cada refeição tem um **id**, **nome**, **descrição**, **data e hora** que foi realizada e identificador se **está ou não na dieta**.

------

## Representação de tabela de refeições no banco de dados:

Variável | Tipo
:-------:| :---:
id | integer
name | varchar
description | varchar
date_time | datetime
on_diet | boolean

------

## Rotas da api:

- ### Adicionar refeição:
  1.  Caminho:  `/`
  2.  Metódo: **Post**

- ### Pegar todas as refeições:
  1.  Caminho:  `/`
  2.  Metódo: **Get**

- ### Pegar uma única refeição:
  1.  Caminho: `/<int:id>`
  2.  Metódo: **Get**

- ### Atualizar uma refeição:
  1.  Caminho: `/<int:id>`
  2.  Metódo: **Put**

- ### Deletar uma refeição:
  1.  Caminho: `/<int:id>`
  2.  Metódo: **Delete**

------

## JSON

```
{
  "name" : "",
  "description" : "",
  "date_time" : "%Y-%m-%d %H:%M:%S",
  "on_diet" : true or false
}
```
