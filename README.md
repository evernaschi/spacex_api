
# Space-x API

API for creating tasks in [`Trello`][trello].  
A task may be:
1. An issue: This represents a business feature that needs implementation, they will provide a short title
and a description. All issues gets added to the “To Do” list as unassigned
1. A bug: This represents a problem that needs fixing. They will only provide a description, the title needs
to be randomized with the following pattern: bug-{word}-{number}. It doesn't matter that they repeat
internally. The bugs should be assigned to a random member of the board and have the “Bug” label.
1. A task: This represents some manual work that needs to be done. It will count with just a title and a
category (Maintenance, Research, or Test) each corresponding to a label in trello

## Setup

1. Install [`Python`][python_setup], [`pip`][pip_setup] and [`virtualenv`][venv_setup] if you do not already have them.

1. Clone this repository:

    ```
    git clone https://github.com/evernaschi/spacex_api.git
    ```

## How to run

1. Create a virtualenv.

    ```
    python3 -m venv env
    source env/bin/activate
    ```

1. Install the dependencies needed to run the app.

    ```
    pip install -r requirements.txt
    ```

1. Now sync your database:

    ```
    python manage.py migrate
    ```
 
1. Run the server:

    ```
    python manage.py runserver
    ```

## Examples:


    python manage.py runserver 3000
    curl -H "Content-Type: application/json" -d '{"type":"issue", "title":"Send Message", "description":"Let pilots"}' http://localhost:3000 
    http POST http://127.0.0.1:8000/ type="issue" title="Send Message" description="Let pilots"  


[trello]: https://trello.com/
[python_setup]: https://www.python.org/downloads/
[pip_setup]: https://pypi.org/project/pip/
[venv_setup]: https://pypi.org/project/virtualenv/
