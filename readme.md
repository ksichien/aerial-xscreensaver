# aerial-xscreensaver

This project contains scripts that can be used to set up XScreenSaver on GNU/Linux to use the latest Apple TV Aerial videos as a screensaver.

First, `aerial-downloader` will need to be executed. This script will download all of the latest Apple TV Aerial videos to a folder called 'Aerial' in the user's home folder.
It will also place a second script called `aerial-player` inside this folder.

This script should be renamed to `aerial` and copied to `/usr/lib/xscreensaver` so XScreenSaver Preferences can use it.

Afterwards, the `aerial` script needs to be referenced in the `programs` section of the `~/.xscreensaver` file:
```
programs:                                                                     \
                                aerial                                      \n\
                                maze -root                                  \n\
- GL:                           superquadrics -root                         \n\
                                attraction -root                            \n\
                                blitspin -root                              \n\
                                greynetic -root                             \n\
                                helix -root                                 \n\
                                hopalong -root                              \n\
                                imsmap -root                                \n\
-                               noseguy -root                               \n\
-                               pyro -root                                  \n\
                                qix -root                                   \n\
-                               rocks -root                                 \n\
                                rorschach -root                             \n\
                                decayscreen -root                           \n\
                                flame -root                                 \n\
                                halo -root                                  \n\
```
Now, the screensaver can be selected when `xscreensaver-demo` is run.

Note: `aerial-downloader` can be executed again at any time in the future to download new videos whenever they become available.
