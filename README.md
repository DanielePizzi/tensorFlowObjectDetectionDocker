
# Tensorflow docker

## build

```bash
 docker build -t tsod .
```

## run

```bash
docker run -v $(pwd)/media:/app/media -it -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --user="$(id --user):$(id --group)" tsod:latest python video.py
```

## mac os RUN

### allow access from localhost

Install the latest XQuartz X11 server and run it
-Install the latest XQuartz X11 server and run it
-Activate the option ‘Allow connections from network clients’ in XQuartz settings
-Quit & restart XQuartz (to activate the setting)

xhost + 127.0.0.1

```bash
docker run -v $(pwd)/media:/app/media -it -e DISPLAY=host.docker.internal:0 -v /tmp/.X11-unix:/tmp/.X11-unix --user="$(id --user):$(id --group)" tsod:latest python video.py
```

from macos:
https://medium.com/@mreichelt/how-to-show-x11-windows-within-docker-on-mac-50759f4b65cb
