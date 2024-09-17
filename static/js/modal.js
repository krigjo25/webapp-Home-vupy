//  Modal -> Initializing data
let html;
let caroseltimer;

const apps = ["carosel", "bio"];

const sources = [
    {src:"20240610_095646.jpg", caption:"Working out in progress", alt:"20240610_095646.jpg"}, 
    {src:"20240517_150950.jpg", caption:"Norwegian National day", alt:"20240610_095646.jpg"}, 
    {src:"20240722_115404.jpg", caption:"tester", alt:"20240610_095646.jpg"}]

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