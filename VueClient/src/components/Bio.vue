<template>
    <section id="about-kristoffer" class="info">
    
        <Carosel />

        <bio />
</section>
</template>

<script>
    import Carosel from '../components/bio_components/Carosel.vue'
    import Bio from '../components/bio_components/Bio.vue';

    export default {
        name: 'Biography',
        components: 
        {
            Carosel, Bio
        },
    };
</script>