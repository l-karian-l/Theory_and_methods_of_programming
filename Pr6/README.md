# Практическая работа №6 - Заместитель, Компоновщик, Инверсия управления

## План 
1. Реализовать на любом объектно-ориентированном языке программирования

### Заместитель

**Заместитель** – это структурный паттерн проектирования, который позволяет подставлять вместо реальных объектов специальные объекты-заменители. Эти объекты перехватывают вызовы к оригинальному объекту, 
позволяя сделать что-то до или после передачи вызова оригиналу

#### Листинг программы: смотри `Vice.py`

В данном примере у нас есть классы Image, RealImage и ImageProxy. 
Класс Image определяет интерфейс для отображения изображения, RealImage 
реализует этот интерфейс и выполняет загрузку и отображение реального 
изображения. ImageProxy выступает в роли заместителя (прокси) для 
RealImage и откладывает загрузку и создание объекта RealImage до момента 
вызова метода display().

При создании объекта ImageProxy указывается имя файла изображения. 
При вызове метода display() на объекте ImageProxy, прокси проверяет, есть 
ли уже созданный объект RealImage для данного файла. Если объект не создан, то происходит его создание и загрузка изображения. Затем вызывается 
метод display() у объекта RealImage, который отображает изображение.

Таким образом, паттерн "Заместитель" позволяет отложить выполнение 
дорогостоящих операций до момента, когда они действительно необходимы, 
и предоставляет прокси-объект с аналогичным интерфейсом для управления 
доступом к реальному объекту.

### Компоновщик

**Компоновщик** – это структурный паттерн, который позволяет сгруппировать множество объектов в древовидную структуру, а затем работать с 
ней так, как будто это единичный объект. 

#### Листинг программы: смотри `Linker.py`

В этом примере мы создаем иерархию документа с помощью разделов 
и элементов контента. Разделы могут содержать как другие разделы, так и 
элементы контента. Мы добавляем элементы контента в соответствующие 
разделы, а затем добавляем разделы в главный раздел document.

Затем мы обходим всю иерархию, начиная с главного раздела, и для 
каждого компонента вызываем метод display_info(), который выводит информацию о каждом компоненте. В результате мы получаем вывод, который 
отображает иерархию документа с его разделами и элементами контента.

### Инверсия управления

#### Листинг программы: смотри `Inversion_of_control.py`

В этом примере у нас есть классы Service и Client. Класс Service определяет
интерфейс для выполнения операции, а ServiceImplementation реализует этот интерфейс.
Класс Client принимает объект service через конструктор и вызывает его метод perform_operation() для выполнения работы. 
В данном случае контроль над созданием и передачей объекта ServiceImplementation осуществляется внешним кодом, а не внутри класса Client, что демонстрирует инверсию контроля.