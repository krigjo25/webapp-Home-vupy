<template>
    <section id="spec-container" class="spec-wrapper flex-wrap-row">
        <div class="spec-class flex-wrap-row" v-for="edu in educations" :key="edu.id">
            <a :href="edu.link" target="_blank">
                <h3 class="h3-link">
                    <i class="bi bi-folder-symlink"></i> {{ edu.name }}
                </h3>
            </a>
            <p>{{edu.description}}</p>
            <Classes v-for="cls in edu.classes" :key="edu.id" :cls="cls" />
        </div>
    </section>
</template>
<script setup>

//  Importing components
import Classes from './education_components/Classes.vue';

//  Importing dependencies
import { reactive } from 'vue';

//  Initializing reactive objects
const educations = reactive([
        {
            id: 0,
            name: 'GetAcademy',
            link: 'https://getacademy.no',
            description: `
                GET Academy is a digital IT school that combats social
                exclusion by providing practical, industry-focused training
                to young IT enthusiasts, equipping them with both technical
                and life skills for successful IT careers`,
            
            
            classes: 
            [
                {
                    id: 0,
                    name: 'Junior Developer',
                    description: `
                        Entry-level position focused on learning & growth.
                        Collaboration and mentorship are essential. Expect
                        guidance from seniors and a focus on building
                        foundational skills. Continuous learning is crucial
                        due to the evolving tech landscape. Don't hesitate
                        to ask questions. It's a stepping stone to senior roles.`,
                    
                    diploma:
                    {
                        graduate: false,
                        warning : false,
                        link: '',
                        note:'',

                        icon: 
                        {
                            qualified: 'bi-award',
                            unqualified: 'bi-gear',
                        },
                    },
                    tech: [
                        {
                            id      : 0,
                            category: "ui-ux",
                            lang    : ['Frontend', 'Vue.js']
                        },
                        {
                            id      : 1,
                            category: "compiled",
                            lang    : ['C#']
                        },
                        {
                            id      : 2,
                            category: "workflow",
                            lang    : ['Git', 'Agile']

                        },
                    ]
                },
                
            ],
        },
        {
            id: 1,
            name: 'CS50 HarvardX',
            link: 'https://www.vpal.harvard.edu/harvardx/',
            description: 
                `Harvard's online platform provides free-to-audit
                courses taught by Harvard faculty across diverse
                subjects. Certificates are available for a fee.
                Courses require a 50-70% passing grade, emphasizing
                original work. Notably, CS50 focuses on algorithmic
                thinking and problem-solving through practical,
                real-world inspired assignments.`,

            classes: 
            [
                {
                    id: 0,
                    name: 'Computer Science for Python Programming',
                    description: `
                       This Certificate program offers practical Python
                       programming skills and core computer science
                       knowledge,serving as a focused, career-driven
                       alternative to a traditional computer science degree.`,
                    
                    diploma:
                    {
                        graduate: true,
                        warning : true,
                        link: 'https://courses.edx.org/certificates/cc7f7cb258a24538af14c876023cf932',
                        icon: 
                        {
                            qualified: 'bi bi-award ',
                            unqualified: 'bi bi-gear warning',
                        },
                        class:
                        {
                            warning: 'bi bi-exclamation-triangle',
                        },
                    },
                    tech: 
                    [
                        {
                            id: 0,
                            category: "ui-ux",
                            lang: ['Frontend', 'SASS/SCSS']
                        },
                        {
                          id: 1,
                          category: "compiled",
                          lang: ['C']
                        },
                        {
                          id: 2,
                          category: "workflow",
                          lang: ['Git']

                        },
                        {
                          id: 2,
                          category: "interpreted",
                          lang: ['Python', 'Flask', 'Django']

                        },
                    ]
                },
            ]
        }
      ]);

</script>