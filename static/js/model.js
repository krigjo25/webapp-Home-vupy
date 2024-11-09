
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
                classes: 
                [
                    {
                        school: "GetAcademy",
                        description: "Skolen for fremtiden",
                        link: "https://getacademy.no/",
                        courses: [
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
                                course: "IT Development",
                                description: "MVC software development",
                                skills: 
                                [
                                    "Agile practices",
                                    "Customer relations",
                                    "",
                                ],
                            },
                            {
                                name: "C# and .NET",
                                description: "Backend software development",
                                skills: 
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
                        courses: [
                            {
                                course: "CS50x",
                                description: "Introduction to Computer Science ",
                                skills: 
                                [
                                    "Python",
                                    "Database Management",
                                    "c", 
                                    "Algorithms",
                                ],
                                course: "CS50Web",
                            },
                            {
                                course: "CS50P",
                                description: "Introduction to Computer Science With Python",
                                skills: 
                                [
                                    "Web development using Flask",
                                    "Flask",
                                    "API",
                                ],

                            },
                            {
                                course: "CS50Web",
                                description: "Computer Science Web Development",
                                skills: 
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
                caption:"4",
                alt:"20240903_165612.jpg"
            },
        ],
};