<template>
    <section id="specialization-container" class="spec-wrapper">
        <div class="specialization-class" v-for="education in educations" :key="education.id">
            <a :href="education.link" target="_blank">
                <h3 class="h3-link">
                    <i class="bi bi-folder-symlink"></i> {{ education.name }}
                </h3>
            </a>
            <p>{{education.description}}</p>
            <Classes />
        </div>
    </section>
</template>
<script>

//  Importing components
import Classes from './education_components/Classes.vue';

export default {

  name: 'GET',
  data() {
    return {
      educations: [
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
        },

        {
            id: 1,
            name: 'CS50 HarvardX',
            link: 'https://www.vpal.harvard.edu/harvardx/',
            description: 
            `Harvard University's online learning platform which offers a variety of courses in a variety of subjects.
            The courses are taught by Harvard faculty and are open to anyone who is interested in learning. Its free to
            audit the courses, but there is a fee to get a certificate. The requirements to pass a course is to get
            between 50% and up to 70% of the course material correct. With out any Plagiarism.`,
        }
      ]
    }
  },
    components: {
        Classes
    }
}
</script>