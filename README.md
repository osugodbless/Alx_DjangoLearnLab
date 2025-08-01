# Introduction to Django Project

This repository contains the implementation of the **Introduction to Django** project as part of the ALX Backend Web Development program. The project focuses on building foundational skills in Django by working with models, the ORM, and the admin interface.

---

## 📌 Project Objectives

- Set up a Django development environment and start a new project.
- Define a `Book` model with fields: `title`, `author`, and `publication_year`.
- Perform and document basic CRUD operations via the Django shell.
- Register and customize the model in the Django admin interface.

---

## ⚙️  Tech Stack

- Python 3.12
- Django
- MySQL

---

## Highlights

- Django installed and project initialized (`LibraryProject`)
- App created (`bookshelf`) and model defined (`Book`)
- Migrations created and applied
- CRUD operations implemented and documented
- Admin interface customized for the `Book` model

---

## 🗂️ Documentation

All shell commands and outputs related to Create, Retrieve, Update, and Delete operations are documented [here](./Introduction_to_Django/LibraryProject/bookshelf/) as:

- `CRUD_operations.md`
- `create.md`
- `retrieve.md`
- `update.md`
- `delete.md`

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/osugodbless/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/Introduction_to_Django/LibraryProject
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run migrations:
    ```bash
    python3 manage.py migrate
    ```

4. Start the server:
    ```bash
    python3 manage.py runserver
    ```

5. Visit http://127.0.0.1:8000/book in your browser

**Note:** The model has also been registered in Django admin site. To access the admin panel, make sure you create a superuser first using the `python3 manage.py createsuperuser` command. Then, navigate to [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and log in with your superuser credentials.
