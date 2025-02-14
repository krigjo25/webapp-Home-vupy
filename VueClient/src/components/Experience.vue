<template>
    <section id="fullstack">
        <h2>Portefolio</h2>
        <form>
            <legend>Filter by</legend>
            <select>
                <option value ="">Fullstack</option>
                <option value ="">Frontend</option>
                <option value ="">Backend</option>
            </select>
            <select>
                <option value ="">Console</option>
                <option value ="">Webapp</option>
            </select>
            <select>
                <option value ="">C</option>
                <option value ="">C#</option>
                <option value ="">py</option>
            </select>
        </form>
        <div class="fullstack-container">
            <div class="pp" v-for="repo in pfolio" :key="repo.id">
                <div class="pro-nav">
                    <Link :ref="url" v-for=" url in repo.url" v-if="url"/>
                    <div class="tech-container flex-row">
                        <span class="flex-reversed-row">
                            <i><time :value="repo.date">{{ repo.date }}</time></i>
                        </span>
                        <h3>{{ repo.name }}</h3>
                        <span>{{ repo.description }}</span>
                        <div class="flex-row">
                            <tech :tech="lang" v-for="lang in repo.lang" v-if="lang"/>
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
import tech from './education_components/tech.vue';

export default {

    data() {
        return {
            pfolio: null
        }
    },
    methods: {
        async fetchRepos()
        {
            const path = import.meta.env.VITE_Github_local;

            await axios.get(path)
            .then((res) => {
                this.pfolio = res.data.github;
                console.log(this.pfolio);
            })
            .catch((err) => {
                console.log(err);
            });
        }
    },
    components: {
        Link,
        tech
    },
    async created() {
        await this.fetchRepos();
    }
}
</script>