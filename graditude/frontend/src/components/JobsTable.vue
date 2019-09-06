<template>
    <div id="JobsTable">
        <v-data-table
                dense
                calculate-widths
                fixed-header
                :headers="headers"
                :items="posts"
                :items-per-page="20"
                class="elevation-1"
                :loading="loading"
                loading-text="Loading job listings, please wait..."
        ></v-data-table>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "JobsTable",
        data() {
            return {
                headers: [
                    {
                        text: 'Title', value: 'title'
                    },
                    {
                        text: 'Company', value: 'company'
                    },
                    {
                        text: 'Description', value: 'description'
                    },
                    {
                        text: 'Date Posted', value: 'date_posted'
                    },
                    {
                        text: 'Link', value: 'link'
                    }
                ],
                posts: [],
                loading: true

            }
        },
        methods: {
            getAllPosts: function () {
                axios
                    .get('/jobs/api/v1/posts/')
                    .then(response => {
                        this.posts = response.data
                        this.loading = false

                    })
                    .catch(error => {
                        console.log(error)
                        this.errored = true
                    })
                    .finally(() => this.loading = false)
            }
        },
        mounted() {
            this.getAllPosts()

        }
    };
</script>
