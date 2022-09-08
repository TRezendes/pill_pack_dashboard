# Pill-pack Dashboard
 ## A utility for monitoring production status when using Parata Pass and QS/1
 
 `PATH_TO_WATCH` should be set to the folder into which fill list `.dat` files are exported.
 
 The app expects a file called `facilities.csv` located in the `static` folder. The file should be of the structure:
 
    export_name.dat,display_name,facility_name
    export_name.dat,display_name,facility_name
    export_name.dat,display_name,facility_name
    
Where `export_name.dat` must match the name of the fill list file that is exported by PrimeCare. There are no constraints on `display_name` and `facility_name`; they are the names that display on the Dashboard.

---

![GitHub](https://img.shields.io/github/license/TRezendes/pill_pack_dashboard)
