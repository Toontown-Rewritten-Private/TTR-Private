# This is the PRC configuration file for a published TTR client. Note that only
# this file and Panda3D's Confauto.prc are included. Any relevant directives in
# Config.prc should be reproduced here.

# Client settings
window-title Toontown Rewritten [OFFLINE]
server-version ttroff-beta-v2.12.2
sync-video #f
want-dev #f
preload-avatars #t
texture-anisotropic-degree 16
want-speedhack-fix #t
load-display pandagl


# New Addons!
want-WASD #t
tt-framerate #t
want-new-toonhall #t
want-max-font #t


# Resource settings
model-path /
model-cache-models #f
model-cache-textures #f
vfs-mount phase_3.mf /
vfs-mount phase_3.5.mf /
vfs-mount phase_4.mf /
vfs-mount phase_5.mf /
vfs-mount phase_5.5.mf /
vfs-mount phase_6.mf /
vfs-mount phase_7.mf /
vfs-mount phase_8.mf /
vfs-mount phase_9.mf /
vfs-mount phase_10.mf /
vfs-mount phase_11.mf /
vfs-mount phase_12.mf /
vfs-mount phase_13.mf /
default-model-extension .bam


# DC Files
#dc-file config/ttroff.dc Automatically wrapped into the code.


# Server settings
want-rpc-server #f
rpc-server-endpoint http://localhost:8080/
eventlog-host 127.0.0.1
want-cheesy-expirations #t
- Mongo Settings
mongodb-url mongodb://127.0.0.1/astron


# Beta Modifications
# Temporary modifications for unimplemented features go here.
want-pets #t
want-news-tab #f
want-news-page #f
want-accessories #f
want-parties #t
want-gardening #t
want-gifting #f
want-skip-button #t
# This is a temporary 'fix' for DistributedSmoothNodes... probably not the permanent solution to our problem, but it works for now.
smooth-lag 0.4
want-keep-alive #f


# Developer Modifications
# A few fun things for our developer build. These shouldn't go in public_client.
estate-day-night #f
want-instant-parties #t
show-total-population #f
want-toontorial #f


# Chat stuff
want-whitelist #t
want-blacklist-sequence #f
force-avatar-understandable #f
force-player-understandable #f


# Holidays and Events
force-holiday-decorations 6
want-arg-manager #t
want-mega-invasions #f
mega-invasion-cog-type tm


# Working (Custom) Addons!
want-toonfest #t
want-doomsday #f
election-difficulty 1