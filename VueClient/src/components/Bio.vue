<template>
    <section id="about-kristoffer" class="info">
        <Carosel />
        <bio />
    </section>
</template>

<script>
    //  Importing components
    import Bio from '../components/bio_components/Bio.vue';
    import Carosel from '../components/bio_components/Carosel.vue';
    
    
    export default {
        name: 'Biography',
        components: 
        {
            Bio,
            Carosel,
            
        },
    };
</script>