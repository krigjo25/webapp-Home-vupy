<template>
    <LayoutHeader />
    <section class="page-alert">
        <template v-if="error?.status == 404">
            <h2>{{error.statusCode}} - {{ notFoundError?.title }} </h2>
            <p v-html="notFoundError?.message"></p>
            <p>Gå tilbake til <NavigationButton :data="btn" class="orange-btn"/></p>
        </template>
        <template v-if="error?.status == 500">
            <h2>{{error?.statusCode}} -{{ unkownError?.title }} </h2>
            <p v-html="notFoundError?.message"></p>
            <p>Gå tilbake til <NavigationButton :data="btn" class="orange-btn"/></p>
        </template>
        <template v-else>
            <h2>{{error?.statusCode}} -{{ unkownError?.title }} </h2>
            <p v-html="notFoundError?.message"></p>
            <p>Gå tilbake til <NavigationButton :data="btn" class="orange-btn"/></p>
        </template>
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
        action: () => {clearError( { redirect: '/'} )}
    }

    const jokes = {
        notFound: [
            `Denne siden '${route.path}' er på kaffepause`,    
            `Denne siden '${route.path}' er frakoblet helg`,
            `Denne siden '${route.path}' har tatt tidelig helg`,
            `Denne siden '${route.path}' er sporløst forsvunnet`
        ],
        itenralServer: [`Woups, det sjedde noe krøll, når vi skulle hente informasjonen fra server`],
        unkownError: [`Denne gangen er det våres feil. Vi møtte veggen med en ukjent feilkode.`]
    }

    const randomErrorJoke = (data:string[]) => {return data[Math.floor(Math.random() * data.length)] };

    //  --- Error handling
    const notFoundError = computed(() => {  return {title: randomErrorJoke(jokes.notFound), message: error?.statusMessage }});
    const unkownError = computed(() => { return { title: randomErrorJoke(jokes.unkownError), message: error?.statusMessage }});
    const internalError = computed(() => { return { title: randomErrorJoke(jokes.unkownError), message: error?.statusMessage }});

</script>