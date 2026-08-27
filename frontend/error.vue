<template>
    <LayoutHeader />
    <section class="page-alert">
        <template v-if="error?.status == 404">
            <h2>{{ notFoundError?.title }} </h2>
            <p v-html="notFoundError?.message"></p>
            <p>Gå tilbake til <NavigationButton :data="btn" class="orange-btn"/></p>
        </template>
        <template v-else>
            <h2>{{ unkownError?.title }} </h2>
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
        404: [
            `Denne siden '${route.path}' er på kaffepause`,    
            `Denne siden '${route.path}' er frakoblet helg`,
            `Denne siden '${route.path}' har tatt tidelig helg`,
            `Denne siden '${route.path}' er sporløst forsvunnet`
        ]
    }

    const errorTexts: Record<string, Record<string, string | undefined>> = reactive({
        notFound: { title: 'Siden du leter etter er ikke funnet.', message: 'Kunne ikke finne ønsket side' },
        internalServer:  { title: 'Noe gikk galt ({{ error?.statusCode }}' }
    });

    const random404Joke = () => {
        const data = jokes[404];
        const randomIndex = Math.floor(Math.random() * data.length);
        return data[randomIndex];
    }

    //  --- Computed propteries
    const unkownError = computed(() => {const data = errorTexts.internalServer; return data} );
    const notFoundError = computed(() => { const data = errorTexts.notFound; data.title = random404Joke(); data.message = error?.statusText; return data });

</script>