# rumal_back
Code for Rumal Backend that will interface with Thug Daemon

## Purpose & Design
Rumal is based on a model that ensures that the backend (where the analysis will be done) and the frontend (client facing side and the social network) remain decoupled. Keeping this in mind the Backend comprises of a Django Project with models for Tasks that interacts with the Thug Daemon. The Daemon reads and writes to the models of the Django Project. The Django Project includes a RESTful API that communicates with the frontend to take tasks and allow fetching of results by frontend when required. Historical Data is moved to the frontend and is not maintained on the backend.

### API
The API has two end points one for submitting Tasks and the other fo retriving Results. The APIs have been built very closely around the APIs in the orignal Rumal draft. Infact the APIs for fetching analysis are the same as their purpouse was exactly same. The API for submitting tasks has been modified to remove User and Sharing info which are irreleevant to the backend. Also an additional key is added for frontend_id which allows frontend to later fetch the results. Only API Authentication is support as users will never interact with the backend directly.

### Install

Like Rumāl's orignal draft the backend needs to make sure you are using a supported Thug version, to avoid any incompatibilities in arguments and behaviours. To do so, Thug will be run inside a Docker container.

System-wide requirements:
* Python 2.7+
* Docker
* MongoDB

Python module requirments:
* Django 1.9.1
* pymongo 2.6
* django-tastypie 0.13.1
* hexdump 3.2
* python-dateutil 2.4.2
* python-magic 0.4.6
* python-mimeparse 0.1.4
* pytz 2015.4
* six 1.9.0
* wheel 0.24.0
* tldextract 1.6

#### Docker
You need to install Docker on your host to be able to run Rumal's backend. Please refer to Docker's own [installation guide](https://docs.docker.com/installation/).

#### MongoDB
MongoDB should be configured and running on your **host**. It should also be reachable by the container running Thug: to achieve this, you should modify your `/etc/mongodb.conf` file finding the following line:

    bind_ip = 127.0.0.1

You can remove or comment it if you want MongoDB to be listening on all interfaces; else, if you want it to run only on localhost and on the internal docker0 interface, change it to read:

    bind_ip = 127.0.0.1,172.17.42.1

Please replace `172.17.42.1` with whatever address your docker0 interface is set to (you can get it by running `ifconfig docker0`).

#### Django
**Please consider using VirtualEnv from now on, especially if you already have other projects running on Django versions other than 1.9**. Installing VirtualEnv is extremely easy:

    $ sudo pip install virtualenv

Actually, you only need sudo if you're installing `virtualenv` globally (which I suggest you to do). Now, `cd` to Rumāl's backend root directory to create and activate your virtual environment:

    $ cd rumal_back
    $ virtualenv venv
    $ source venv/bin/activate

That's all. The first command will create a folder named `venv`, with a copy of the Python executable, pip and some other tools; the second command will activate the virtual environment for you. From now on, every time you run `pip install`, the requested modules will be installed locally, without touching your global Python environment.
When you're done with Rumāl, just run `deactivate` to exit from `venv`. Please also consider using [Autoenv](https://github.com/kennethreitz/autoenv) to automatically activate your virtual environment every time you enter the folder (and to automatically deactivate it when you leave).

Now, you can install Rumāl's own dependencies by running the following command from the root directory. **WARNING: Rumāl's backend requires specific versions of some libraries such as Django 1.9. If you've got other projects running on the same box, please consider using VirtualEnv (see above) if you didn't already!**

    $ pip install -r requirements.txt

Now you can setup the database (which, for now, uses SQLite as the backend) and create your superuser by running (from Rumāl's root directory):

    $ python manage.py migrate
    $ python manage.py createsuperuser

## Running Rumal's backend

First of all, you will need to run the backend daemon. **IMPORTANT: please make sure that the user you run the backend daemon with can run Docker images** (e.g. run it as `root` or add it to the `docker` group or create a `sudoers` entry to allow it to run `/usr/bin/docker without password`, whatever).

    $ python manage.py run_thug

Then, in another console, you can run the web APIs:

    $ python manage.py runserver

Or, if you want your server to be reachable from the external network:

    $ python manage.py runserver 0.0.0.0:8000

Now you can connect to the APIs by pointing your browser to http://127.0.0.1:8000/ (or to whatever IP/port you chose).
