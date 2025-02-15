<template>
    <nav>
        <Btn :class="btn.cls" v-for="btn in data" :key="btn.id" :btn = btn @click="btn.function" />
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
        data: 
        {
            type: Array,
            required: true
        },

    },
    computed: {
        filterbtn() {
            //return this.button.filter(button => button.exist)
        }
    }
};
</script>