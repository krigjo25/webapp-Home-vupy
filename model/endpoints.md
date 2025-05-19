#   Visual representation of classes and
```mermaid
---
title: API Classes
---

 classDiagram

    Announcements .. UtilityTools.Announcements"
    
    note for Github "Responsible for fetching data from Github API, 
    Utilizing APILogger to log interactions and error"
    
    note for PhotoLibrary "Responsible for fetching Photos, 
    Utilizing APILogger to log interactions and error"
    
    note for Announcements "Responsible for fetching data from UtilityTools.Announcements, 
    Utilizing APILogger to log interactions and error"


    class Github{
        APILogger
        def get()
    }
    class PhotoLibrary {
        APILogger
        def get()
    }

    class Announcements {
        APILogger
        def get()
    }
```