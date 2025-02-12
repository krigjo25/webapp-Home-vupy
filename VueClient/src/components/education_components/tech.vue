<template>
    <div class="tech-wrapper"  v-for="name in tech.names" :key="name">

        <div :class="'relative tech-' + tech.category">
            <span class="tech-label">
                <span>{{ name }}</span>
            </span>
        </div>
    </div>
</template>
<script>

export default
{
    props: {
        tech: {
            type: Object,
            required: true
        }
          
    },
}
</script>