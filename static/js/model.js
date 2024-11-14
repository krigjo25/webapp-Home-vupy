
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
                    /*{
                        icon: "bi bi-github",
                        name: "Newest Blog post",
                    },*/

                ],
                id: document.getElementById("bio"),
                name: "profile",
                time: 0,
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
                app: "specialization",
                id: document.getElementById("expertise"),
                schools: 
                [
                    {
                        school: "Get Academy",

                        description: `
                            GET Academy is an innovative digital IT school working to reduce social exclusion by 
                            providing young IT enthusiasts with life-changing career opportunities. With a focus on safety,
                            diversity, and growth, the school offers practical and strengths-based learning in close
                            collaboration with industry. The school's unique educational model equips students with the tools
                            they need to succeed both academically and personally, while also helping businesses fill critical
                            skills gaps.
                            
                            In addition to IT education, the school teaches key competencies - skills and life tools that
                            provide direction and meaning in an individual's life. Upon graduation, a GET developer will be a
                            self-sufficient IT professional, trained in programming, creative thinking, and collaboration.`,
                        link: "https://getacademy.no/",
                        classes:
                        [
                            {
                                name: "Fullstack Engineer",
                                //diploma: "https://getacademy.no/",
                                //description: "This is a professional certificate demostrates the experise in Fullstack Development. Developing a comprehensive understanding of the fundamentals In",
                                description: "This education is a fullstack developer education, which includes the following technologies",
                                tech:
                                [
                                    "API",
                                    "HTML",
                                    "CSS",
                                    "MVC",
                                    "MVC .NET",
                                    "JavaScript",
                                    "Agile practices",
                                    "Customer relations",
                                    "Database Management",
                                ],
                            },

                        ]
                    },
                    {
                        school: "HavardX",
                        link: "https://vpal.harvard.edu/harvardx/",
                        description: "Harvard University's online learning platform",
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
                                description: "This is a professional certificate demostrates the experise in CS. Developing a comprehensive understanding of the fundamentals In",
                                tech: 
                                [
                                    "Django",
                                    "Flask",
                                    "API",
                                ],

                            },
                        ]
                    },
                ]
            },
            {
                app:"footer",
                id: document.getElementById("footer-apps"),
            }

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