
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
                    {
                        icon: "bi bi-github",
                        name: "about",
                    }
                ],
                id: document.getElementById("bio"),
                name: "profile",
                time: null,
                title: ["Kristoffer Gjøsund", "Professional profile"],
                message: `
                    My ideal lifestyle involves a balance between the passion 
                    of technology and wellness. I dedicate my free time to coding,
                    meditation, and physical activity and I am always looking for
                    new challenges / adventures.`,
                
                message1:`
                    As Developer i prefer to organize my code with comments, 
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

        ],
    sources:
        [
            {
                src:"20240517_081250.jpg", 
                caption:"National Day 2024",
                alt:"20240517_081250.jpg"
            }, 
            {
                src:"20240610_095646.jpg", 
                caption:"Woring out in the gym",
                alt:"20240610_095646.jpg"
            }, 
            {
                src:"20240705_095904.jpg",
                caption:"Having fun at the work",
                alt:"20240705_095904.jpg"
            },
            {
                src:"20240903_165612.jpg",
                caption:"4",
                alt:"20240903_165612.jpg"
            },
            {
                src:"IMG-20240512-WA0005.jpeg", 
                caption:"5", 
                alt:"IMG-20240512-WA0005.jpeg"},
            {
                src:"Screenshot_20240702_145919_Hevy.jpg",
                caption:"6",
                alt:"Screenshot_20240702_145919_Hevy.jpg"
            },
        ],
};