
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
                id: document.getElementById("bio"),
                name: "profile",
                time: null,
                message: null,
                message1: null,
                message2: null,
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