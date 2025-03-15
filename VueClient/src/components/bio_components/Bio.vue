<template>
    <section id='bio'class="bio-container">
        <h2>{{ bio.current.author.name}}</h2>
        <h3>{{ bio.current.author.title }}</h3>
        <Navigation :class='bio.current.cls':data="bio.pages"/>
        <section class="bio-content">
            <div class='keywords'>
                <nav class="ext-bar flex-wrap-row-justify-space-evenly">
                    <a v-for="link in bio.current.links" :key="link.id" :href="link.url" :class="link.cls" target="_blank">
                            <i :class="link.icon"></i>
                    </a>
                </nav>
                <h3>{{ bio.current.title  }}</h3>
                <h4 class="h4-link">{{ bio.current.headline }}</h4>
                <small class ='abt-author'>Born : {{bio.current.author.born}} ({{ bio.current.author.age }} years old) </small><br>
            </div>
            <small>Written by {{ bio.current.author.name }}. Average reading time <b>{{ bio.current.readtime }} min</b><i class="bi bi-stopwatch"></i></small>       
            
            <p v-for="msg in bio.current.message">{{ msg }}</p>
        </section>
    </section>

    <!--Announcements /-->
    
</template>

<script setup>
//  Importing dependencies
import { onMounted, reactive, computed } from 'vue';
import { ReadTime, CalculateAge, CalculateDate } from '@/services/utils/bioTools';
//  Importing components
import Navigation from '../misc_components/navigation.vue';
import { isDesktop } from '@/services/utils/rwd';

function biography()
{
    //  Importing the links
    const mail = import.meta.env.VITE_Mail;
    const youtube = import.meta.env.VITE_Youtube;
    const facebook = import.meta.env.VITE_Facebook;
    const instagram = import.meta.env.VITE_Instagram;

    bio.current = {
        cls: "bio-bar",
        title: "Biography",
        get readtime() { return ReadTime(this.message)},
        headline: "Passionate Programmer And Fitness Enthusiast",                
        links:
        [
            {
                id  :0,
                exist: true,
                url :youtube,
                cls : "bio-link",
                icon:"bi bi-youtube",                        
            },
            {
                id  :1,
                exist: true,
                url :instagram,
                cls : "bio-link",
                icon:"bi bi-instagram",    
            },
            {
                id  :2,
                exist: true,
                url :facebook,
                cls : "bio-link",
                icon:"bi bi-facebook",   
            },
            {
                id  :3,
                url :mail,
                exist: true,
                cls : "bio-link",
                icon:"bi bi-mailbox",
            },                  
        ],

        message:
        [
            `My lifestyle embodies a balance of technological passion and dedication to wellness. 
            Free time is spent in pursuits that enrich both mind and body: software development, 
            meditation, and physical activity, all while embracing new challenges.`, 

            `I demonstrate a commitment to self-improvement by actively developing proficiency in Python libraries, 
            database management, piano, and philosophy. My proactive approach to growth includes utilizing a network 
            of developers and online resources.`,

            `Throughout my career, dedication and a strong work ethic have been consistently evident. 
            Colleagues appreciate my contributions to projects, and I excel at fostering supportive
            team environments and recognizing individual strengths.`,
        ],
        

        author:
        {
            name:"Kristoffer Gjøsund",
            get age() {return CalculateAge([1994, 2, 25])},
            get born() {return CalculateDate([1994, 2, 25, 15])},
        },
    };
};

function workProfile()
{
    // Importing the links
    const CV = import.meta.env.VITE_CV;
    const github = import.meta.env.VITE_Github;
    const linkedin = import.meta.env.VITE_LinkedIn;
            
    bio.current = {
        cls: "bio-bar",
        get readtime() { return ReadTime(this.message)},
        title: "Work Biography",
        
        headline: "Junior Software Developer",

        links:
        [
            {
                id  :0,
                exist: true,
                url :linkedin,
                cls :"bio-link",
                icon:"bi bi-linkedin",
            },
            {
                id  :1,
                exist: true,
                url :github,
                cls :"bio-link",
                icon:"bi bi-github",
            },
            {
                id  :2,
                url :CV,
                exist: true,
                cls :"bio-link",
                icon:"bi bi-file-person",
            },
        ],

        message:[
            `Early in my career as a junior developer, I've come to appreciate the power of organization.
            I'm committed to delivering high-quality, maintainable code because I want to build software
            that's both intuitive and efficient. I use comments and documentation to share my understanding
            of the code. My development philosophy is to begin with simplicity and then refine for performance.
            Most importantly, I've seen firsthand how test frameworks are essential for building reliable software.`,
        ],
        
        author:
            {
                name:"Kristoffer Gjøsund",
                get age() {return CalculateAge([1994, 2, 25])},
                get born() {return CalculateDate([1994, 2, 25, 15])},

            },
        };
};

function Journey()
{
    bio.current = {
        cls: "bio-bar",
        title   : "Journey",
        headline: "The Journey So Far",
        get readtime() { return ReadTime(this.message)},
        
        message :
        [
            `My coding journey started in my teens with HTML and CSS, and the SitePoint community sparked my passion
            for software engineering,  leading me to explore JavaScript. It was in JavaScript that I found my calling
            in back-end development. I specialized in Python and database management, gaining practical experience through
            Discord projects. To expand my full-stack knowledge, I attended Get Academy vocational school while completing
            Harvard University's CS50. I am excited to apply my skills to complex projects and continue my growth as a
            developer. As a Get Academy student, I am committed to continuous learning and seek a challenging part-time
            role that offers industry mentorship and the opportunity to apply my academic knowledge.`,

            `I am drawn to teams that foster continuous learning, mentorship, and Agile practices. My ideal career path
            involves advancing to a Senior Data Scientist position within a dynamic and collaborative environment.`
        ],
        author:
        {
            name:"Kristoffer Gjøsund",
            get age() {return CalculateAge([1994, 2, 25])},
            get born() {return CalculateDate([1994, 2, 25, 15])},
        }, 
    };
};

function WorkoutBlog()
{
    bio.current = {
        title: "Workout Blog",
        headline: "Workout Blog",
        get readtime() { return ReadTime(this.message)},

        links: [],
        message: [],

        author:
        {
            name:"Kristoffer Gjøsund",
            get age() {return CalculateAge([1994, 2, 25])},
            get born() {return CalculateDate([1994, 2, 25, 15])},
        }, 
    };
};

function PersonalBlog()
{
    bio = {
        title: "Workout Blog",
        headline: "Workout Blog",
        get readtime() { return ReadTime(this.message)},

        links: [],
        message: [],

        author:
        {
            name:"Kristoffer Gjøsund",
            get age() {return CalculateAge([1994, 2, 25])},
            get born() {return CalculateDate([1994, 2, 25, 15])},
        }, 
    };
};

const bio = reactive(
    {
        current:
        {
            readtime: null,
            title: null,
            headline:null,

            links:[],
            message:[],
            
            author:
                {
                    name:null,
                    born: null,
                    age: null,

                },
        },
        pages: [
                {
                    id      : 0,
                    exist   : true,
                    cls     : "bio-btn",
                    name    : isDesktop() ? "Biography" : null,
                    function: biography,
                    icon    : "bi bi-info-circle-fill",
                },
                {
                    id      : 1,
                    exist   : true,
                    cls     : "bio-btn",
                    name    : isDesktop() ? "Work Biography":  null,
                    function: workProfile,
                    icon    : "bi bi-person-workspace",
                },
                {
                    id      : 2,
                    exist   : true,
                    cls     : "bio-btn",
                    function: Journey,
                    name    : isDesktop() ? "Journey So Far" : null,
                    icon    : "bi bi-activity",
                },
                {
                    id      : 3,
                    exist   : false,
                    cls     : "bio-btn",
                    name    : isDesktop() ? "Common Opinions" : null,
                    function:"",
                    icon    : "bi bi-clock-history",
                },
                {
                    id      : 4,
                    exist   : false,
                    cls     : "bio-btn",
                    name    : isDesktop() ? "Workout Blog" : null,
                    function: WorkoutBlog,
                    icon    : "bi bi-clock-history",
                },
                {
                    id      : 5,
                    exist   : false,
                    cls     : "bio-btn",
                    name    : isDesktop() ?  "Personal Blog" : null,
                    function: PersonalBlog,
                    icon    : "bi bi-clock-history",
                },
            ],
    }
);

onMounted(() => {
    biography();
});
</script>