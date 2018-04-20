# fob-all-the-things

This code is the server-side API that powers much of AMT’s keyfob access systems.

Want to contribute? Here’s how to dive in with the code:

## 1. Install Docker

You can get it at https://www.docker.com/community-edition#/download. 


## 2. Clone the repository
Check out code from this repository:

```git clone https://www.github.com/AceMonsterToys/fob-all-the-things```

cd into the directory you just cloned (referred to this as /pathtoapp from here, but if you’re not sure where that is you can run `pwd` now to find out).


## 3. Start up the container
Using Docker helps develop on a consistent environment. Regardless of what platform you’re on, you can develop on an environment that has been set up exactly the same way the app will be deployed.

For the FATT API, we’ll be using a Python 3 Flask environment. You can run it like so, replacing /pathtoapp with the checkout location of the repository from above:

```docker run --name fatt-api-server --restart=always \
    -p 8000:80 \
    -v /pathtoapp:/app \
    -d jazzdd/alpine-flask:python3
```

(You may need to login with a Docker Hub account.) Docker will download dependencies it might need and fire up a container. 

### Common docker commands 

* "docker ps -a" will show you all of your local containers (the ```-a``` flag makes the output include container that aren't running.)
* "docker start" will start a container that has been created.
* "docker stop" will gradually to stop a container that has been created (a nice SIGTERM signal before sending a SIGKILL to the container's process)
* "docker kill" will immediately try to stop the process by sending a SIGKILL signal.
* "docker rm" will remove a container that already exists.

## 4. Visit the app:

http://localhost:8000

