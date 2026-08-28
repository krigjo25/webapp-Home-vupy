<template>
    <LayoutHeader />
    <section class="page-alert">
        <h2 v-if="error?.statusCode === 404" v-html="error.statusCode + ' - ' + notFoundError.title"></h2>
        <h2 v-else-if="error?.statusCode === 500" v-html="error.statusCode + ' - ' + internalError.title"></h2>
        <h2 v-else v-html="error?.statusCode + ' - ' + unkownError.title"></h2>
        <p>Gå tilbake til <NavigationButton :data="btn" :class="btn.cls"/></p>
    </section>
    <LayoutFooter />
</template>
<script setup lang="ts">

    //  --- import dependencies.
    import { computed } from 'vue';

    //  --- Import types
    import type { NuxtError } from '#app';
    import type { ButtonItem } from './types/navigation';

    const route = useRoute();

    // --- defineprops
    const props = defineProps({ error: Object as () => NuxtError });
    const error = props.error;

    //  --- handle error
    const btn:ButtonItem = {
        label: 'Portfolio',
        cls: ['button', 'primary-btn'],
        action: () => {clearError( { redirect: '/'} )}
    }

    const jokes = {
        notFound: [
            `Denne siden <q><strong>${route.path}</strong></q> er på kaffepause`,    
            `Denne siden <q><strong>${route.path}</strong></q> er frakoblet helg`,
            `Denne siden <q><strong>${route.path}</strong></q> har tatt tidelig helg`,
            `Denne siden <q><strong>${route.path}</strong></q> er sporløst forsvunnet`
        ],

        itenralServer: [`Woups, det sjedde noe krøll, når vi skulle hente informasjonen fra server`],
        unkownError: [`Denne gangen er det våres feil. Vi møtte veggen med en ukjent feilkode.`]
    }

    const randomErrorJoke = (data:string[]) => {return data[Math.floor(Math.random() * data.length)] };

    //  --- Error handling
    const notFoundError = computed(() => {  return {title: randomErrorJoke(jokes.notFound) }});
    const unkownError = computed(() => { return { title: randomErrorJoke(jokes.unkownError) }});
    const internalError = computed(() => { return { title: randomErrorJoke(jokes.unkownError) }});

</script>