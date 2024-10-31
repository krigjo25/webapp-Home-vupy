//  Modal -> Initializing data
let html;
let caroseltimer;

const apps = ["carosel", "bio"];

let sources = [
    {src:"20240517_081250.jpg", caption:"Working out in progress", alt:"20240517_081250.jpg"}, 
    {src:"20240610_095646.jpg", caption:"Norwegian National day", alt:"20240610_095646.jpg"}, 
    {src:"20240705_095904.jpg", caption:"tester", alt:"20240705_095904.jpg"},
    {src:"20240903_165612.jpg", caption:"tester", alt:"20240903_165612.jpg"},
    {src:"IMG-20240512-WA0005.jpeg", caption:"tester", alt:"IMG-20240512-WA0005.jpeg"},
    {src:"Screenshot_20240702_145919_Hevy.jpg", caption:"tester", alt:"Screenshot_20240702_145919_Hevy.jpg"},]

const app = [
    {
        app:document.getElementById("carosel"), 
        path:"static/img/carosel/", 
        source:"static/img/carosel/20240610_095646.jpg", 
        caption:"Working out in progress", 
        alt:"20240610_095646.jpg",}]


const bio = [    {
    app:document.getElementById("bio"),
    title:"",
    time:0,
    msg:"",
    msg1:"",
    msg2:"",}]