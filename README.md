
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

1. In the app directory, create a file whose name is .env, and put inside it:
    ```
    SECRET_KEY = '....your secret key ....'
    TRELLO_KEY = '0109e2ca4440a60b57cbf0a51c10d600'
    TRELLO_TOKEN = '5dd9d5beb8299ca4c6a75e3bb06c66defbd606d106d84223f80e97fe896c889c'
    ```
    You can use a website like this https://djecrety.ir/ for generating your SECRET_KEY.
    You can use my Trello key and token for this time.

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

1. After creating a Task, you can see the results in [`My Board`][trello_board]

## Examples:


    python manage.py runserver 3000
    curl -H "Content-Type: application/json" -d '{"type":"issue", "title":"Send Message", "description":"Let pilots"}' http://localhost:3000 
    http POST http://127.0.0.1:8000/ type="issue" title="Send Message" description="Let pilots"  


[trello]: https://trello.com/
[python_setup]: https://www.python.org/downloads/
[pip_setup]: https://pypi.org/project/pip/
[venv_setup]: https://pypi.org/project/virtualenv/
[trello_board]: https://trello.com/invite/b/ZLrw4NBB/417bb91362d67f90abe0a2de86790081/spacex
