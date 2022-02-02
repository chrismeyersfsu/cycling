# Quickstart

```
./rouvy_gpx_transform.py <dir_with_gpx_files_downloaded_from_rouvy>
```

Files named `filename_rlv_ready.gpx` can now be imported into RLV studio and an RLV file generated.

Now you have a set of files `<gpx, mp4, rlv>` that can be used in Golden Cheetah to ride!

# TODO

I am unsure about the `*5` in the script. A value of 5 presumes the values in the Rouvy `.gpx` files are gathered every 5 seconds `<name>time_here</name>`stamp. I roughly determined the rate to be 5 by importing the conversion into RLV Studio and looking at the calculated speed values and figured they were reasonable.
