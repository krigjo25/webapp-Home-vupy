

<template>
    <header class="flex-wrap-row">
        <Header/>
    </header>
    <main>
        <Bio/>
        <Announcements/>
        <Education />
        <Experience />

    </main>
    <footer>
        <Footer/>
    </footer>
</template>
<script setup>
    
    //  Importing components
    import Bio from '../components/Bio.vue';
    import Footer from '../components/Footer.vue';
    import Header from '../components/Header.vue';
    import Education from '../components/Education.vue';
    import Experience from '../components/Experience.vue';
    import Announcements from '../components/Announcements.vue';
    

</script>