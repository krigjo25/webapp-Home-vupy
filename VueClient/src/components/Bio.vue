<template>
    <section id="about-kristoffer" :class="'info ' + bio.cls ">
        <Carosel />
        <bio />
    </section>
</template>

<script setup>
    //  Importing   Dependencies
    import { ref, onMounted, onUnmounted, reactive, computed } from 'vue';

    //  Importing components
    import Bio from './bio_components/Bio.vue';
    import Carosel from './bio_components/Carosel.vue';


    const bio = reactive({
        cls: computed(() => checkDeviceType().cls),
        id: 'about-kristoffer',
        
    });

    function checkDeviceType() {
    
        //  Initialize device type variables
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
        else if (window.innerWidth < tablet && window.innerWidth > mobile)
        {
            console.log('Tablet');
            data.cls = 'flex-row';
        }
        else if (window.innerWidth < desktop)
        {
            console.log('Desktop');
            data.cls = 'flex-row';
        }
        else
        {
            bio.cls = 'flex-row';

        }
        return data
    }

</script>