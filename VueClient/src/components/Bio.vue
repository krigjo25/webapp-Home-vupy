<template>
    <section :id="bio.id" :class="'info ' + bio.cls ">
        <Carosel />
        <bio />
    </section>
</template>

<script setup>
    //  Importing   Dependencies
    import { reactive} from 'vue';
    import { isMobile, isDesktop } from '../services/utils/rwd.js';
    import { biography, workProfile, Journey, WorkoutBlog, PersonalBlog } from '../services/utils/bio.js';

    //  Importing components
    import Bio from './bio_components/Bio.vue';
    import Carosel from './bio_components/Carosel.vue';

    const bio = reactive({
        cls:  'flex-wrap-row-justify-space-evenly flex-wrap-row-align-items-end',
        id: 'auto-bigoraphy',
        pages: [
                {
                    id      : 0,
                    exist   : true,
                    cls     : "bio-btn",
                    name    : isDesktop() ? null : "Biography",
                    function: biography,
                    icon    : "bi bi-info-circle-fill",
                },
                {
                    id      : 1,
                    exist   : true,
                    cls     : "bio-btn",
                    name    : isDesktop() ? null : "Work Biography",
                    function: workProfile,
                    icon    : "bi bi-person-workspace",
                },
                {
                    id      : 2,
                    exist   : true,
                    cls     : "bio-btn",
                    function: Journey,
                    name    : isDesktop() ? null : "Journey So Far",
                    icon    : "bi bi-activity",
                },
                {
                    id      : 3,
                    exist   : false,
                    cls     : "bio-btn",
                    name    : isDesktop() ? null : "Common Opinions",
                    function:"",
                    icon    : "bi bi-clock-history",
                },
                {
                    id      : 4,
                    exist   : false,
                    cls     : "bio-btn",
                    name    : isDesktop() ? null : "Workout Blog",
                    function: WorkoutBlog,
                    icon    : "bi bi-clock-history",
                },
                {
                    id      : 5,
                    exist   : false,
                    cls     : "bio-btn",
                    name    : isDesktop() ? null : "Personal Blog",
                    function: PersonalBlog,
                    icon    : "bi bi-clock-history",
                },
            ],
    });

</script>