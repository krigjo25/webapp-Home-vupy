<template>
    <button>
        <a :href="btn.url" v-if="btn.url" target="blank">
            <i :class="btn.icon"></i> 
            {{btn.name}}
        </a>
        <i :class="btn.icon" v-else></i> 
            {{btn.name}}
            </button>
</template>
<script>
export default {
    props: {
        btn: {
            type: Object,
            required: true
        }
    },
};
</script>