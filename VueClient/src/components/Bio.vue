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
        const mobile = 768;
        const tabletWidth = 1024;
        const desktop = 1024;
        const data = reactive({});

        //  Check if the window width is less than 768px
        console.log(window.innerWidth);
        
            // Mobiles
        if (window.innerWidth < tabletWidth)
        {
            data.cls = 'flex-column';

        }
        else
        {
            data.cls='flex-row';

        }
        return data.cls
    }

</script>