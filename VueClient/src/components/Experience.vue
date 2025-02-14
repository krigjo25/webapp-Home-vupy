<template>
    <section id="fullstack">
        <h2>Portefolio</h2>
        <div class="fullstack-container">
            <div class="pp" v-for="repo in portefolio" :key="repo.id">
                <div class="pro-nav">
                    <!--Link :href="url.repo_url" v-if="url.repo_url"/-->
                    <div class="tech-container flex-row">
                        <span class="flex-reversed-row">
                            <i><time :value="repo.date">{{ repo.date }}</time></i>
                        </span>
                        <h3>{{ repo.name }}</h3>
                        <span>{{ repo.description }}</span>
                        <div class="flex-row">
                            <!--Tech :tech="repo.tech" v-if="repo.tech"/-->
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
//  Importing dependencies
import axios from 'axios';

//  Importing components
import Link from './misc_components/link.vue';

export default {
    name: 'Experience',
    data() {
        return {
            portefolio: []
        }
    },
    methods: {
        async fetchRepos()
        {
            const path = import.meta.env.VITE_Github_local;

            await axios.get(path)
            .then((res) => {
                this.portefolio = res.data.github;
                console.log(res.data.status);
            })
            .catch((err) => {
                console.log(err);
            });
        }
    },
    components: {
        Link
    },
    async created() {
        await this.fetchRepos();
    }
}
</script>