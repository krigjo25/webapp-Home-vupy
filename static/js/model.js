
// Model
let html;
let caroseltimer;

const model =
{
    apps:[
            {
                app: "carosel",
                name: "carosel",
                path: "static/img/carosel/",
                source: "20240903_165612.jpg",
                caption: "Guy Smiling", 
                alt: "220240903_165612.jpg",
                id: document.getElementById("carosel"),
            },
            {
                app: "bio",
                links: [
                    {
                        icon: "bi bi-github",
                        name: "profile",
                    },
                    {
                        icon: "bi bi-github",
                        name: "journey",
                    },
                ],
                id: document.getElementById("bio"),
                name: "profile",
                time: null,
                title: ["Kristoffer Gjøsund"],
                message: `
                    My ideal lifestyle involves a balance between the passion 
                    of technology and wellness. I dedicate my free time to coding,
                    meditation, and physical activity and I am always looking for
                    new challenges / adventures.`,
                
                message1:`
                    As an Application Engineer i prefer to organize my code with comments, 
                to give out a greater understanding of the code which is
                written, I also prefer to organize my code with a
                documentation for a greater understanding of the project.
                My process of development includes a lot of simplicity at
                first, then I optimize the code for a better performance.
                Through my journey as a developer, I have learned that the
                best way to ensure the quality for the code is through test
                frameworks.`,
                message2:``,
            },
            {
                app:"specialization",
                id: document.getElementById("expertise"),
                schools: 
                [
                    {
                        school: "GetAcademy",
                        description: "Skolen for fremtiden",
                        link: "https://getacademy.no/",
                        classes: [
                            {
                                name: "Start IT",
                                description: "Front-end software development",
                                tech:
                                [
                                    {
                                        name:"HTML"
                                    },
                                    {
                                        name:"CSS"
                                    },
                                    {
                                        name:"JavaScript"
                                    },
                                    {
                                        name:"MVC"
                                    },
                                    {
                                        name:"Agil practices"
                                    },
                                ],
                            },
                            {
                                name: "IT Development",
                                diploma: "",
                                description: "MVC software development",
                                tech: 
                                [
                                    "Agile practices",
                                    "Customer relations",
                                    "",
                                ],
                            },
                            {
                                name: "C# and .NET",
                                diploma: "",
                                description: "Backend software development",
                                tech: 
                                [
                                    "MVC .NET",
                                    "Database Management",
                                    "API",
                                ],
                            },
                        ]
                    },
                    {
                        school: "HavardX",
                        description: "Skolen for fremtiden",
                        classes: [
                            /*{
                                name: "Introduction to Computer Science",
                                link: "",
                                diploma: "https://courses.edx.org/certificates/2c5d4f0e9c5d4f4a8c6b3b5b3d9c4c4a",
                                description: "This is a professional certificate demostrates the experise in CS. Developing a comprehensive understanding of the fundamentals In",
                                tech:
                                [
                                    {
                                        name:"python",
                                        keywords:
                                        [
                                            "Data Structures",
                                            "Algorithms",
                                            "SQL",
                                            "API",
                                            "Django / Flask",

                                        ],
                                    },
                                    {
                                        name:"Database Management",
                                        keywords:
                                        [
                                            "SQL",
                                        ],
                                    },
                                   {
                                    name:"c",
                                    keywords:
                                    [
                                        "Data Structures",
                                        "Algorithms",
                                    ],
                                }, 
                                {
                                    name:" front-end",
                                    keywords:
                                    [
                                        "HTML",
                                        "CSS",
                                        "JavaScript",
                                    ],
                                }
                                ],
                            },*/
                            {
                                name: "CS50P",
                                diploma: "https://courses.edx.org/certificates/cc7f7cb258a24538af14c876023cf932",
                                description: "Introduction to Computer Science With Python. In depth to Python technology in CS",
                                tech: 
                                [
                                    "Web development using Flask",
                                    "Flask",
                                    "API",
                                ],

                            },

                            {
                                name: "CS50Web",
                                description: "Computer Science Web Development. In depth to Python technology in Web engineering",
                                tech: 
                                [
                                    "Web development using Django",
                                    "API",
                                ],

                            },
                        ]
                    },
                ]
            },

        ],
    sources:
        [
            {
                src:"20240903_165612.jpg",
                caption:"Guy Smiling",
                alt:"20240903_165612.jpg"
            },
        ],
};