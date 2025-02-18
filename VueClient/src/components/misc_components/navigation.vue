<template>
    <nav>
        <Btn  v-for="btn in data" :key="btn.id" :btn = btn @click="btn.function" />
    </nav>
</template>

<script setup>
//  Importing dependencies
import { defineProps, computed } from 'vue';

//  Importing components
import Btn from './button.vue'

const props = defineProps(
    {
        data:
        {
            type    : Array,
            required: true
        }
    }
)
const filter = computed(() => {
    get: () => {
        return this.data.filter(button => button.exist)
    }
    set: (value) => {
        return this.data.filter(button => button.exist)
    }
});
</script>