# Практическая работа №1 - Модельно-ориентированный подход к проектированию (часть 1)

## План 

1. При помощи программы PlantUML либо любого редактора построить UML-диаграмму вариантов использования, диаграмму классов проектируемой информационной системы в соответствии с вариантом задания, а также диаграмму последовательности для наиболее часто используемых прецедентов.
При построении диаграммы классов нужно добиться достаточной детализации информационной системы.
Убедитесь в том, что использовали отношения dependency, aggregation/c¬omposition, generalization, описали размещение классов по пакетам проекта.
2. Подготовить отчет с включением диаграмм.

## Вариант 12 - Система автоматического тестирования

### Диаграмма вариантов использования:

![image](https://github.com/l-karian-l/Theory_and_methods_of_programming/blob/main/Pr1/USD.png)

#### Листинг программы:

```
@startuml
left to right direction
skinparam actor {
  BackgroundColor LightBlue
}

actor User
actor Admin

rectangle "Automated Testing System" {
  User --> (Run Tests)
  User --> (View Test Results)
  User --> (Generate Reports)

  Admin --> (Manage Test Cases)
  Admin --> (Manage Test Environments)

  (Manage Test Cases) --> (Create Test Case)
  (Manage Test Cases) --> (Update Test Case)
  (Manage Test Cases) --> (Delete Test Case)

  (Manage Test Environments) --> (Add Environment)
  (Manage Test Environments) --> (Delete Environment)
  (Manage Test Environments) --> (Modify Environment Settings)
}

@enduml

```

### Диаграмма классов:

![image](https://github.com/l-karian-l/Theory_and_methods_of_programming/blob/main/Pr1/CD.png)

#### Листинг программы:

```
@startuml

class AutomatedTestingSystem {
  +RunTests()
  +ViewTestResults()
  +GenerateReports()
}

class User {
  +username: String
  +password: String
}

class Admin {
  +username: String
  +password: String
}

class TestManager {
  +CreateTestCase(testCaseData: TestData)
  +UpdateTestCase(testCaseData: TestData)
  +DeleteTestCase(testCaseId: String)
}

class EnvironmentManager {
  +AddEnvironment(environmentData: EnvironmentData)
  +DeleteEnvironment(environmentId: String)
  +ModifyEnvironmentSettings(environmentId: String, settingsData: SettingsData)
}

AutomatedTestingSystem "1" *-- "1..*" User
AutomatedTestingSystem "1" *-- "1..*" Admin
AutomatedTestingSystem "1" *-- TestManager
AutomatedTestingSystem "1" *-- EnvironmentManager

@enduml

```

### Диаграмма последовательности:

![image](https://github.com/l-karian-l/Theory_and_methods_of_programming/blob/main/Pr1/SD.png)

```
@startuml
actor User
participant "Automated Testing System" as TestingSystem
participant "Test Manager" as TestManager
participant "Environment Manager" as EnvManager

User -> TestingSystem: Run Tests
TestingSystem -> TestManager: Create Test Case
TestManager --> TestingSystem: Test Case Created
TestingSystem -> EnvManager: Add Environment
EnvManager --> TestingSystem: Environment Added
TestingSystem -> TestManager: Update Test Case
TestManager --> TestingSystem: Test Case Updated
TestingSystem -> TestManager: Delete Test Case
TestManager --> TestingSystem: Test Case Deleted
TestingSystem -> TestingSystem: Execute Tests
TestingSystem -> TestingSystem: Collect Test Results
TestingSystem -> TestingSystem: Generate Reports
TestingSystem --> User: Reports Generated

@enduml

```


## Полезные ссылки

1. 	http://www.omg.org/mda/
2.	OMG UML Specification http://www.omg.org/spec/UML/ 
3.	OMG XMI Specification http://www.omg.org/spec/XMI/ 
4.	Статья об MDA - https://www.osp.ru/os/2003/09/183391/ 
5.	Статьи о UML Refactoring https://www.researchgate.net/publication/311856689_Model_and_Criteria_for_the_Automated_Refactoring_of_the_UML_Class_Diagrams 

