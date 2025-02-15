<template>
    <section id="specialization-container" class="spec-wrapper">
        <div class="specialization-class" v-for="edu in educations" :key="edu.id">
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
<script>

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
                GET Academy is an innovative digital IT school working to reduce social exclusion by providing young IT 
                enthusiasts with life-changing career opportunities. With a focus on safety, diversity, and growth, the
                school offers practical and strengths-based learning in close collaboration with industry. The school's
                unique educational model equips students with the tools they need to succeed both academically and
                personally, while also helping businesses fill critical skills gaps. In addition to IT education, the
                school teaches key competencies - skills and life tools that provide direction and meaning in an
                individual's life. Upon graduation, a GET developer will be a self-sufficient IT professional, trained
                in programming, creative thinking, and collaboration.`,
            
            
            classes: 
            [
                {
                    id: 0,
                    name: 'Junior Developer',
                    description: `
                        Frontend Development is the practice of producing HTML, CSS, and JavaScript for a website or Web
                        Application so that a user can see and interact with them directly. The challenge associated with
                        frontend development is that the tools and techniques used to create the front end of a website
                        change constantly and so the developer needs to constantly be aware of how the field is developing.
                        The effective frontend developer should be able to create a seamless user experience and a
                        responsive design.`,
                    
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
                `Harvard University's online learning platform which offers a variety
                of courses in a variety of subjects. The courses are taught by Harvard
                faculty and are open to anyone who is interested in learning. Its free to
                audit the courses, but there is a fee to get a certificate. The
                requirements to pass a course is to get between 50% and up to 70% of the
                course material correct. With out any Plagiarism. CS50 teaches students
                how to think algorithmically and solve problems efficiently. Problem sets
                inspired by real-world inspired problem sets.`,

            classes: 
            [
                {
                    id: 0,
                    name: 'Proffesional Certificate in Computer Science for Python Programming',
                    description: `
                        Professional Certificate in Computer Science for Python Programming
                        is a focused online learning program designed to equip you with
                        practical Python programming skills and a foundational
                        understanding of computer science principles.  Think of it as a
                        concentrated, career-oriented alternative to a full computer science degree.`,
                    
                    diploma:
                    {
                        graduate: true,
                        warning : true,
                        link: 'https://courses.edx.org/certificates/cc7f7cb258a24538af14c876023cf932',
                        notes: `The Courses are completed, but the fee to get the certificate is not paid.`,
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
export default {

  setup() {
    return { educations }
  },
    components: {
        Classes
    }
}
</script>