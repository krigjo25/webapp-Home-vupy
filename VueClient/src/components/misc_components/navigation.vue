<template>
    <nav :class="cls">
        <Btn :class="btn.cls" v-for="btn in filterlinks" :key="btn.id" :btn = btn @click="btn.function" />
    </nav>
</template>

<script>

//  Importing components
import Btn from './button.vue'
export default {
    components: {
        Btn
    },
    props: {
        button: {
            type: Array,
            required: true
        },
        cls: {
            type: String,
            required: true
        }
    },
    computed: {
        fliterlinks() {
            return this.button.filter(btn=> btn.url)
        }
    }
};
</script>