<template>
    <LayoutHeader />
    <section class="page-alert">
        <h2 v-if="error?.statusCode === 404" v-html="notFoundError"></h2>
        <h2 v-else-if="error?.statusCode === 500" v-html="error.statusCode + ' - ' + internalError"></h2>
        <h2 v-else v-html="error?.statusCode + ' - ' + unkownError"></h2>
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

    //  --- Custom error message
    const path = `${error?.statusCode} - Siden <q><strong>${route.path}</strong></q>`;
    const notFound:string[] = [
        `${path} er frakoblet.`,        
        `${path} er på kaffepause.`,    
        `${path} har tatt tidelig helg.`,
        `${path} er sporløst forsvunnet.`
        ];
    const unkown:string[] = [`Denne gangen er det våres feil. Vi møtte veggen med en ukjent feilkode.`];
    const internalServer:string[] = [`Woups, det sjedde noe krøll, når vi skulle hente informasjonen fra server`];

    const randomErrorJoke = (data:string[]) => {return data[Math.floor(Math.random() * data.length)] };

    const unkownError = computed(() => randomErrorJoke(unkown) );
    const notFoundError = computed(() =>  randomErrorJoke(notFound) );
    const internalError = computed(() => randomErrorJoke(internalServer));

</script>