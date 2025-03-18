<template>
    <section id='bio'class="bio-container">
        <h2>{{ bio.current.author.name}}</h2>
        <h3>{{ bio.current.author.title }}</h3>
        <Navigation :class='bio.current.cls':data="bio.pages"/>
        <section class="bio-content">
            <div class='keywords'>
                <nav class="ext-bar flex-wrap-row-justify-space-evenly">
                    <a v-for="link in bio.current.links" :key="link.id" :href="link.url" :class="link.cls" target="_blank" >
                            <i :class="link.icon"></i>
                    </a>
                </nav>
                <h3>{{ bio.current.title  }}</h3>
                <h4 class="h4-link">{{ bio.current.headline }}</h4>
                <small class ='abt-author'>Born : {{bio.current.author.born}} ({{ bio.current.author.age }} years old) </small><br>
            </div>
            <small>Written by {{ bio.current.author.name }}. with {{bio.current.author. contributor}} for content enhancement and language optimization. Average reading time <b>{{ bio.current.readtime }} min</b><i class="bi bi-stopwatch"></i></small>       
            
            <p v-for="msg in bio.current.message">{{ msg }}</p>
        </section>
    </section>

    <!--Announcements /-->
    
</template>

<script setup>
//  Importing dependencies
import { onMounted, reactive } from 'vue';
import { ReadTime, CalculateAge, CalculateDate } from '@/services/utils/bioTools';
//  Importing components
import Navigation from '../misc_components/navigation.vue';
import { isDesktop } from '@/services/utils/rwd';

function profile()
{
    //  Importing the links
    const mail = import.meta.env.VITE_Mail;
    const youtube = import.meta.env.VITE_Youtube;
    const facebook = import.meta.env.VITE_Facebook;
    const instagram = import.meta.env.VITE_Instagram;

    bio.current = {
        cls: "bio-bar",
        title: "Kristoffer Gjøsund",
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
            ` Driven by philosophical questions since childhood, my curiosity has led me to seek
            an understanding of context instead of content. This inherent analytical thinking enables
            me to grasp complex challenges and discern underlying patterns, a skill that has been highly
            appreciated throughout my adult life.`,

            `This way of thinking also influences how I interact with others. I value deep conversations
            and genuine connections, I prefer to listen and understand rather than dominate the
            conversation. I strive for clear and contextual communication as i sense that true understanding
            arises from considering the surrounding circumstances, not merly from the spoken words. Therefore,
            my focus lies on listening before speaking.`,
        ],
        

        author:
        {
            name:"Kristoffer Gjøsund",
            contributor: "Google Gemini",
            get age() {return CalculateAge([1994, 2, 25])},
            get born() {return CalculateDate([1994, 2, 25, 15])},
        },
    };
};

function workProfile()
{
    // Importing the links
    const CV = import.meta.env.VITE_CV;
    const github = import.meta.env.VITE_GithubLink;
    const linkedin = import.meta.env.VITE_LinkedIn;
            
    bio.current = {
        cls: "bio-bar",
        get readtime() { return ReadTime(this.message)},
        title: "Professional Profile",
        
        headline: "Collaborative Development",

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
        ],

        message:[
            `Driven by a lifelong curiosity and a desire to understand the underlying context,
            I approach application development with a philosophical mindset, seeking to contribute
            to the world as a reflection of my personal journey.`,
            
            `My technical portfolio development has been driven by a deep desire to learn and
            create impactful solutions. I am committed to delivering high-quality, maintainable
            code, fueled by empathy for the end-user. I value open communication and knowledge
            sharing, employing comprehensive comments and documentation. My development philosophy
            emphasizes simplicity and ongoing learning, refining for performance with a strong emphasis
            on test frameworks to ensure reliability, user-friendly applications, and respect for the
            work of others.`,

            `I leverage AI tools such as Google Gemini as a powerful aid in expressing
            and refining my thoughts throughout the development process. Gemini assists me to explore 
            and articulate complex ideas, translate them into clear and concise language. This allows me
            to focus on the creative and strategic aspects of development, while Gemini assists in the
            technical articulation of my thought process.`,

            `Throughout my previous career, dedication and a strong work ethic have been the foundation
            of my professional approach. Colleagues acknowledge the value of my project contributions,
            and I actively cultivate collaborative team environments where individual strengths are
            recognized and leveraged.`
        ],
        
        author:
            {
                name:"Kristoffer Gjøsund",
                contributor: "Google Gemini",
                get age() {return CalculateAge([1994, 2, 25])},
                get born() {return CalculateDate([1994, 2, 25, 15])},

            },
        };
};

function autoBiography()
{
    bio.current = {
        cls: "bio-bar",
        title   : "An Autobiography",
        headline: "Journey of growth and self-discovery",
        get readtime() { return ReadTime(this.message)},
        
        message :
        [
            `My journey began subtly in my youth, influenced by my father and brother's involvement in the IT industry,
            I wasn't consciously aware of my future aspirations. My childhood was characterized by gaming and family time,
            a consequence of other children's unwillingness to spend time with me. The upside of this consequence, the
            challenge solving skill unconsciously increased.`,

            `Throughout my childhood I encountered numerous challenges that adversely affected my academic performance.
            This was a consequence of a combination of the school environment and my internal struggles at that time, which
            compounded the existing difficulties, which only served to worsen the situation.`,

            `In my teens, I started exploring basic front-end development, captivated by the idea of creating "cool" web-based
            applications. Simultaneously, I faced internal challenges that demanded attention, but I was unaware of and lacked
            access to the resources needed to address them. These internal challenges remained subconsciously suppressed until
            my late 20s, when a transformative event occurred. I frequently refer to this era as the "dark ages." Despite the
            perceived difficulties of my teenage years, they ultimately became a natural part of my personal growth.`,

            `In my early 20s, I consistently worked at a job that offered little personal fulfillment. It wasn't until I experienced
            a shift in mindset, a desire to be more productive, that I began to actively develop my skills. Work time was used to
            enhance critical thinking by listening to audiobooks. Lunch breaks became opportunities to improve my challenge-solving
            skills through Python and SQL projects at a bachelor's/master's level. After two years, a sudden urge to resign left me
            unemployed for six months. During this period, I concentrated on further strengthening my critical thinking and challenge-solving
            skills. By participating in CS50 Introduction to Python.`,

            `A beneficial side effect of this period of self-study was the substantial development of other previously underdeveloped and
            suppressed skills, with particular emphasis on emotional intelligence.`,

            `Consequently, I chose to work alongside my studies to support them. This position lasted until I began my studies at GetAcademy,
            finally pursuing the passion that had been suppressed since my teenage years.`,
        ],
        author:
        {
            name:"Kristoffer Gjøsund",
            contributor: "Google Gemini",
            get age() {return CalculateAge([1994, 2, 25])},
            get born() {return CalculateDate([1994, 2, 25, 15])},
        }, 
    };
};

function workoutLog()
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

function personalBlog()
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
                    contributor: "Google Gemini",
                    born: null,
                    age: null,

                },
        },
        pages: [
                {
                    id      : 0,
                    exist   : true,
                    cls     : "bio-btn",
                    name    : isDesktop() ? "Personal Philiosophy" : null,
                    function: profile,
                    icon    : "bi bi-info-circle-fill",
                },
                {
                    id      : 1,
                    exist   : true,
                    cls     : "bio-btn",
                    name    : isDesktop() ? "Professional Profile":  null,
                    function: workProfile,
                    icon    : "bi bi-person-workspace",
                },
                {
                    id      : 2,
                    exist   : true,
                    cls     : "bio-btn",
                    function: autoBiography,
                    name    : isDesktop() ? "Personal Background" : null,
                    icon    : "bi bi-activity",
                },
                {
                    id      : 4,
                    exist   : false,
                    cls     : "bio-btn",
                    name    : isDesktop() ? "My fitness Insights" : null,
                    function: workoutLog,
                    icon    : "bi bi-clock-history",
                },
                {
                    id      : 5,
                    exist   : false,
                    cls     : "bio-btn",
                    name    : isDesktop() ?  "My Personal Journey" : null,
                    function: personalBlog,
                    icon    : "bi bi-clock-history",
                },
            ],
    }
);

onMounted(() => {
    profile();
});
</script>