# Пактическая работа №2 - Модельно-ориентированный подход к проектированию (часть 2)

## План
1.	При помощи программы PlantUML либо любого редактора построить UML-диаграмму диаграммы последовательностей и развёртывания.
2.	Подготовить отчет с включением диаграмм. Загрузить в GIT. Прикрепить ссылку

## Вариант 13 - Электронная доска объявлений

### Диаграмма последовательности для действия "Place Advertisement":

 ![image](https://github.com/l-karian-l/Theory_and_methods_of_programming/blob/main/Pr2/SD1.png)

#### Листинг программы:

```
@startuml
actor User
participant "Electronic Bulletin Board" as Board
User -> Board: Place Advertisement
Board -> Board: Validate Advertisement Data
Board -> Board: Generate Unique ID
Board -> Board: Create Advertisement Object
Board --> User: Advertisement ID
@enduml
```

### Диаграмма последовательности для действия "Delete Advertisement":

![image](https://github.com/l-karian-l/Theory_and_methods_of_programming/blob/main/Pr2/SD2.png)

#### Листинг программы:

```
@startuml
actor User
participant "Electronic Bulletin Board" as Board
User -> Board: Delete Advertisement
Board -> Board: Find Advertisement by ID
Board -> Board: Delete Advertisement Object
Board --> User: Deletion Confirmation
@enduml

```
