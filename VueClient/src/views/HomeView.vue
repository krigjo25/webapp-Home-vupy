

<template>
    <header>
        <Header/>
    </header>
    <main>
        <Bio/>
        <Announcements/>
        <Education />
        <Experience />

    </main>
    <footer>

    </footer>
</template>
<script>
    
    //  Importing components
    import Bio from '../components/Bio.vue';
    import Header from '../components/Header.vue'
    import Education from '../components/Education.vue'
    import Experience from '../components/Experience.vue'
    import Announcements from '../components/Announcements.vue'


    export default {
        name: 'Home',
        components: 
        {
            Bio,
            Header,
            Education,
            Experience,
            Announcements,

        },
    };
    


</script>