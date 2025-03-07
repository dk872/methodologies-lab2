# Linked List Implementation with Unit Tests

## Decription
This project implements a list based on Python's built-in lists and a singly linked circular list in Python without using built-in collections. They include fundamental operations such as appending, inserting, deleting, reversing, and searching within the list. The implementation is accompanied by a unit test suite to ensure reliability and correctness. GitHub Actions are configured to automatically run tests.

## Calculation of the variant number
Record book number - **3214**.

Variant number = 3214 mod 4 = **2**.


The initial implementation of a list is a *list based on built-in arrays/lists*.

The second implementation of a list is a *singly linked circular list*.

## Running the program
First, clone the repository and navigate into the project directory:
```
git clone https://github.com/dk872/methodologies-lab2
```
```
cd methodologies-lab2
```

- **On Linux:**
  - Make sure you have Python installed. You can check with:
    ```
    python3 --version
    ```
  - Run the script and see the result of executing the demo functions:
    ```
    python3 src/main.py
    ```

- **On Windows:**
  - Make sure Python is installed and added to the system PATH. You can check with:
    ```
    python --version
    ```
  - Run the script and see the result of executing the demo functions:
    ```
    python .\src\main.py
    ```

## Running the tests
This project has 28 different tests that verify the operation of methods for working with lists.

- **On Linux:**
  - Run the tests and see the result:
    ```
    python3 -m unittest discover src
    ```

- **On Windows:**
  - Run the tests and see the result:
    ```
    python -m unittest discover src
    ```

## Commit with failed tests
[link](https://github.com/dk872/methodologies-lab2/commit/4c5d334284eb43c87a5610f359315ea3d1526c55)

## Conclusions
This project demonstrates the implementations of a list based on built-in arrays/lists and circular linked list and highlights the importance of unit testing in maintaining software stability.

Unit tests play a crucial role in software development by:
  - **Ensuring code reliability**
  - **Facilitating refactoring**
  - **Improving Maintainability**

By incorporating unit tests, this project guarantees that changes to the list’s implementation do not introduce regressions. Therefore, I believe that working with unit tests was very useful for me, as it helped me to understand more deeply the principles of unit testing, structuring the code and ensuring its reliability. During refactoring, I was able to make sure that the changes did not break the existing functionality, and I also learned to quickly find and fix errors.

## Author info
Dmytro Kulyk, a student of group IM-32
