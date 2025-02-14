<template>
    <a :href="ref" target="_blank">
        <i class="bi bi-link"></i>
    </a>
</template>
<script>

export default
{
    props: 
    {
        ref:
        {
            type: String,
            required: true
        }
    },
}
</script>