# Neo_Courses_Api
This is a simple REST API project. Created via Django. Includes information about different courses.

# Courses API Root (http://127.0.0.1:8000/)

This resource does not have any attributes/ Instead it offers the initial API affordances.
It recommends to follow existing links.

## Retrieve the Entry Point [GET]

+ Response 200 (application/json)

  {
    "admin"
    "courses"
    "courses/<int:pk>/"
  }
  
## Courses [GET]

The list of existing courses.

+ Response 200 (/courses/)
  [
    {
        "id": 1,
        "category": {
            "id": 2,
            "name": "Programming",
            "imgpath": "imgpath"
        },
        "name": "Python",
        "contacts": [
            {
                "id": 1,
                "value": "0555 123 456"
            }
        ]
    },
    {
        "id": 3,
        "category": {
            "id": 2,
            "name": "Programming",
            "imgpath": "imgpath"
        },
        "name": "C#",
        "contacts": [
            {
                "id": 2,
                "value": "0555 569 785"
            }
        ]
    },
    {
        "id": 4,
        "category": {
            "id": 2,
            "name": "Programming",
            "imgpath": "imgpath"
        },
        "name": "JS",
        "contacts": []
    },
    {
        "id": 5,
        "category": {
            "id": 2,
            "name": "Programming",
            "imgpath": "imgpath"
        },
        "name": "C#",
        "contacts": []
    },
    {
        "id": 6,
        "category": {
            "id": 5,
            "name": "Driving",
            "imgpath": "img"
        },
        "name": "AB",
        "contacts": [
            {
                "id": 3,
                "value": "profile"
            }
        ]
    }
]

## Course [/courses/{course_id}/]

A course object has the following attributes.

-name
-description
-category
-logo
-address
-contacts

+ Parameters
  + course_id (required, number, '1')

### View a course detail [GET]
+ Response 200 (/courses/{course_id})
  {
    "id": 1,
    "name": "Python",
    "description": "What is Python? Executive Summary\r\nPython is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.",
    "logo": "LOGO",
    "category": "Programming",
    "contacts": [
        {
            "id": 1,
            "value": "0555 123 456"
        }
    ],
    "address": [
        {
            "id": 1,
            "latitude": "48.888200",
            "longtitude": "2.168510",
            "address": "21 Av. Edouard Belin, 92500 Rueil-Malmaison, Franc"
        }
    ]
}

### Delete a course [DELETE]
 To delete course send delete on page of course


