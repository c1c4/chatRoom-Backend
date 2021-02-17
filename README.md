Before start the application makes sure you have a Postgres or a docker installed on your computer.

If you have docker use this command: **docker run --rm --name db_chatroom -p 5432:5432 -e POSTGRES_PASSWORD=your_password -d postgres**.

Your string connection need to look like "postgresql://postgres:your_password@localhost:5432/postgres"

You can create a virtual environment and after that on your terminal inside de project use: **pip install -r requirement.txt** to install the dependencies.

After that go to alembic.ini search for sqlalchemy.url = driver://user:pass@localhost/dbname
and change to your string connection like **sqlalchemy.url = postgresql://postgres:your_password@localhost:5432/postgres**
You can use: **alembic revision --autogenerate -m "v0"** to generate your migration based on you models
or just **alembic revision -m "v0"** to create a empty migration file.
With the migrations created you can use the **alembic upgrade head**.
When you finish don't forget to undo the changes on alembic.ini.

This project is made to use together with these two projects `https://github.com/c1c4/ChatRoom` and `https://github.com/c1c4/BotChatRoom`
