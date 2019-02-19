apriltag
========

Small modifications/additions to  http://april.eecs.umich.edu/media/apriltag/apriltag-2015-03-18.tgz

Added a new quad detector and a few various speedups.

***Please note:*** I am not the maintainer of the pypi package listed at https://pypi.org/project/apriltag/ – GitHub issues filed here reporting problems with that package will be summarily closed. Sorry, I don't have time to support someone else's unofficial package.

Dependencies
============

  - OpenCV (optional)

Building(On Only Window)
========
You should build on mingw64.

    cd /path/to/apriltag
    cd core
    mingw64-make.exe

If you directly want to use the library and important binaries to your system directories, you can find related binary files in the folder below.

    /prebuild

Running
=======

You can run `aprilag_opencv_demo` to do stuff, run with `-h` to get help.

So for example, you can run

    ./apriltag_opencv_demo -B    ../images/mapping_feb_2014/*.JPG
    ./apriltag_opencv_demo -B -c ../images/mapping_feb_2014/*.JPG

to benchmark the new code against the old code.

Python
======
You can run `python aprilag in opencv env` to do stuff.(it need opencv, numpy)

    cd ./prebuild
    python testApriltag.py
