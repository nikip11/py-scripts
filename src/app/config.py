title="PyScripts"
summary="summary"
description="""
            ChimichangApp API helps you do awesome stuff. 🚀

            ## Items

            You can **read items**.

            ## Format Dates

            You will be able to:

            * **Create users** (_not implemented_).
            * **Read users** (_not implemented_).

            """
servers=[
        {"url": "https://stag.example.com", "description": "Staging environment"},
        {"url": "https://prod.example.com", "description": "Production environment"},
    ]
    
tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]