<template>
    <a :href="link.url" target="_blank">
        <i :class="link.icon"></i>
    </a>
</template>
<script>

export default
{
    props: 
    {
        link:
        {
            type: String,
            required: true
        },
    },
    setup(props) 
    {
        const link = props.link;
        return { link }
    }
}
</script>