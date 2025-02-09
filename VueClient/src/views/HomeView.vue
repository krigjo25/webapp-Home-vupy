

<template>
    <header>
        <Header />
    </header>
    <main>
        <Bio />
        <education />
        <experience />

    </main>
    <footer>

    </footer>
</template>
<script>
    
    //  Importing components
    import Bio from '../components/Bio.vue';
    import Header from '../components/Header.vue'
    import education from '../components/Education.vue'
    import experience from '../components/Experience.vue'


    export default {
        name: 'Home',
        components: 
        {
            Bio,
            Header,
            education,
            experience,

        },
    };
    


</script>