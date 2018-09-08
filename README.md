# fob-all-the-things

This code is the server-side API that powers much of AMT’s keyfob access systems.

Want to contribute? Here’s how to dive in with the code:

## Quick Startup Steps

### 1. Install Docker

You can get it at https://www.docker.com/community-edition#/download. 


### 2. Clone the repository
Check out code from this repository:

```git clone https://www.github.com/AceMonsterToys/fob-all-the-things```

Navigate into the directory you just cloned (referred to this as /pathtoapp from here, but if you’re not sure where that is you can run `pwd` now to find out).

### 3. Setup the configuration

Copy config.json.example to config.json. Edit config.json, and in the app section, change the value for `port` to 80.

### 4. Start up the container
Using Docker helps develop on a consistent environment. Regardless of what platform you’re on, you can develop on an environment that has been set up exactly the same way the app will be deployed.

For the FATT API, we’ll be using a Python 3 Flask environment. You can run it like so, replacing /pathtoapp with the checkout location of the repository from above:

```docker run --name fatt-api-server --restart=always \
    -p 8000:80 \
    -v /pathtoapp:/app \
    -d jazzdd/alpine-flask:python3 \
    -d
```

(You may need to login with a Docker Hub account.) Docker will download dependencies it might need and fire up a container. 

The last `-d` flag will open the flask app in debugging mode, so the app will reload whenever changes are saved.

#### Common docker commands 

In general, you can think of the docker container as the python process itself, but with a few extra bells and whistles. If you need to manually restart the process, you can run `docker restart [CONTAINER_ID]`. To stop the process, just stop the container.

Spinning containers up and down often does mean that your container's filesystem is ephemeral; if you want changes to the container environment or filesystem to be permanent, make sure that's done outside of the container itself.

* `docker ps -a` will show you all of your local containers and their container IDs (the `-a` flag makes the output include container that aren't running.)
* `docker start CONTAINER_ID` will start a container that has been created.
* `docker stop CONTAINER_ID` will gradually to stop a container that has been created (a nice SIGTERM signal before sending a SIGKILL to the container's process)
* `docker kill CONTAINER_ID` will immediately try to stop the process by sending a SIGKILL signal.
* `docker rm CONTAINER_ID` will remove a container that already exists.
* `docker logs -f CONTAINER_ID` will open a stream of log output for the container's main process (the flask app)
* `docker exec CONTAINER_ID [command]` will run [command] in the container and show you the output.

### 5. Access the app:

http://localhost:8000

