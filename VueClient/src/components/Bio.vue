<template>
    <section id="about-kristoffer" :class="'info ' + bio.cls ">
        <Carosel />
        <bio />
    </section>
</template>

<script setup>
    //  Importing   Dependencies
    import { reactive, computed } from 'vue';

    //  Importing components
    import Bio from './bio_components/Bio.vue';
    import Carosel from './bio_components/Carosel.vue';


    const bio = reactive({
        cls: computed(() => checkDeviceType()),
        id: 'about-kristoffer',
        
    });

    function checkDeviceType() {
    
        //  Initialize device breakpoints variables
        let mobile = 768;
        let tablet = 1024;
        let desktop = 1440;
        let data = {};

        //  Check if the window width is less than 768px
        console.log(window.innerWidth);
        
            // Mobiles
        if (window.innerWidth < mobile)
        {
            console.log('Mobile');
            data.cls = 'flex-column';

        }
        else
        {
            data.cls='flex-row';

        }
        return data.cls
    }

</script>