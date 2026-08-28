<template> 
    <ArticlePage :data="posts"/>
</template>

<script lang="ts" setup>

    //  --- Import dependencies & types
    import { useRoute } from 'vue-router';
    import { fetchCollection } from '#imports';
    import { mapBlogData } from '~/composables/maps/mapBlogPost';

    import type { SeoOptions } from '~/types/utils';
    import type { PostItem } from '~/types/documents';
    import type { DevPostsCollectionItem } from '@nuxt/content';

    //  --- Meta Information
    definePageMeta( { order: 3, description: `Viser en enkelt loggoppføring i sin helhet. Hver artikkel har sin egen unike nettadresse basert på tittelen.` });
     //  --- Route & slug logic
    const route = useRoute();
    const slug = route.params.slug;

    //  --- Dev Data Logic
    const devPath = 'devPosts';
    const devCache = 'devCache';
    const devPosts = await fetchCollection<DevPostsCollectionItem, ReturnType<typeof mapBlogData>>(devPath, devCache, mapBlogData);
    

    
    const posts = computed<PostItem >(() => 
    {
        const data = devPosts.value;
        const currentSlug = String(slug);

        const findBlog = (collection: PostItem[]) => { if (!data) return {}; return collection.find(blog => String(blog.path) === currentSlug) || null };

        return findBlog(data);
    });

    //  --- Error Handling
    if (!posts.value) throw createError({statusCode: 404, statusMessage: `Artikkelen <q><strong>${slug}</strong></q> ble ikke funnet.`, fatal: true})

    //  --- Dynamic SEO Meta & Schema
    const seoData: SeoOptions = 
    { 
        image: posts.value?.meta?.image ?? posts.value?.image,
        urlPath: `https://krigjo25.no/logs/records/${slug}`, 
        title: posts.value ? posts.value.meta?.title : undefined, 
        description: posts.value.meta?.title || posts.value.title ? `${posts.value.title} - Tekniske Logger` : undefined
    };

    useCustomSeo(seoData);

</script>