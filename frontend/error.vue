<template>
    <LayoutHeader />
    <section class="page-error">
        <h2 v-if="error && error.status == 404">{{ notFoundError?.title }} </h2>
        <h2 v-else >{{ notFoundError?.title }} </h2>

        <p>Gå tilbake til <NavigationButton :data="btn" /></p>
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

    //  --- handle error
    const btn:ButtonItem = {
        label: 'Portfolio',
        action: () => {clearError( { redirect: '/'} )}
    }

    const jokes = {
        404: [
            `Denne siden ${route.path} er på kaffepause`,    
            `Denne siden ${route.path} har tatt tidelig helg`,
            `Denne siden ${route.path} er sporløst forsvunnet`
        ]
    }
    const errorTexts: Record<string, Record<string, string | undefined>> = reactive({
        notFound: { title: 'Siden du leter etter er ikke funnet.' },
        internalServer:  { title: 'Noe gikk galt ({{ error?.statusCode }}' }
    });

    const random404Joke = () => {
        const data = jokes[404];
        const randomIndex = Math.floor(Math.random() * data.length);
        return data[randomIndex];
    }

    //  --- Computed propteries
    const unkownError = computed(() => {const data = errorTexts.internalServer; return data} );
    const notFoundError = computed(() => { const data = errorTexts.notFound; data.title = random404Joke(); return data });

</script>