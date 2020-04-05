Docker run:

```shell
docker run -ti -d --name mcserver \
-e MEMORYSIZE='50G' \
-v /home/docker-user/mcserver:/data:rw \
-p 25565:25565 \
-p 25575:25575 \
-p 80:8123 \
marctv/minecraft-papermc-server:latest
```

PORT `8123` is used for dynmap, exposed by container on `80`.

Don't know about `25575`, command comes from: [hub.docker.com/r/marctv/minecraft-papermc-server](https://hub.docker.com/r/marctv/minecraft-papermc-server)


Nice article about reducing server lag: [www.spigotmc.org/wiki/reducing-lag/](https://www.spigotmc.org/wiki/reducing-lag/)