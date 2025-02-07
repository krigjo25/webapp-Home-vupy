

<template>
    <header>
        <Header />
    </header>
    <main>
        <Bio />

    </main>
</template>
<script>

    import Header from '../components/Header.vue'
    import Bio from '../components/Bio.vue';

    export default {
        name: 'Home',
        components: 
        {
            Header, Bio
        },
    };
    


</script>