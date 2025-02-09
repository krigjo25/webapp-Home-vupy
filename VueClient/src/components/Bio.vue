<template>
    <section id="about-kristoffer" class="info">
    
        <Carosel />
        <bio />
</section>
<Announcements />
</template>

<script>
    //  Importing components
    import Bio from '../components/bio_components/Bio.vue';
    import Carosel from '../components/bio_components/Carosel.vue'
    import Announcements from '../components/announce.vue'
    
    export default {
        name: 'Biography',
        components: 
        {
            Carosel,
            Bio,
            Announcements,
        },
    };
</script>