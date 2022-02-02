# Quickstart

```
./rouvy_gpx_transform.py <dir_with_gpx_files_downloaded_from_rouvy>
```

Files named `filename_rlv_ready.gpx` can now be imported into RLV studio and an RLV file generated.

Now you have a set of files `<gpx, mp4, rlv>` that can be used in Golden Cheetah to ride!

# TODO

I am unsure about the `*5` in the script. This is to convert whatever units the `<name>time_here</name>` is gathered at to a proper timestamp. I roughly determined 5 by importing the conversion into RLV Studio and looking at the calculated speed values and figured they were reasonable.
