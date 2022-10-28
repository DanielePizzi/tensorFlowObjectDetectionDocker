
# Tensorflow docker

## build

```bash
 docker build -t tsod .
```

## run

```bash
docker run -v $(pwd)/media:/app/media -it -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --user="$(id --user):$(id --group)" tsod:latest python video.py
```

from macos:
https://medium.com/@mreichelt/how-to-show-x11-windows-within-docker-on-mac-50759f4b65cb