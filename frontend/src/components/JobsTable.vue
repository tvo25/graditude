<template>
    <div id="JobsTable">
        <b-field grouped group-multiline>
            <b-select v-model="perPage" :disabled="!isPaginated">
                <option value="5">5 per page</option>
                <option value="10">10 per page</option>
                <option value="15">15 per page</option>
                <option value="20">20 per page</option>
            </b-select>
        </b-field>
        <b-table id="jobs-table"
                 :data="data"
                 :loading="loading"

                 :paginated="isPaginated"
                 :per-page="perPage"
                 :current-page.sync="currentPage"
                 :pagination-simple="isPaginationSimple"
                 :pagination-position="paginationPosition"

                 :default-sort-direction="defaultSortDirection"

                 aria-next-label="Next page"
                 aria-previous-label="Previous page"
                 aria-page-label="Page"
                 aria-current-label="Current page"
        >
            <template slot-scope="props">
                <b-table-column field="date_posted" label="Date Posted" width="125" sortable centered>
                    {{ props.row.date_posted ? new Date(props.row.date_posted).toLocaleDateString() : '' }}
                </b-table-column>

                <b-table-column field="title" label="Title" width="300" sortable>
                    {{ props.row.title }}
                </b-table-column>

                <b-table-column field="company" label="Company" width="150" sortable>
                    {{ props.row.company }}
                </b-table-column>
                <b-table-column field="location" label="Location" width="150" sortable>
                    {{ props.row.location }}
                </b-table-column>

                <b-table-column field="description" label="Description" width="400" sortable>
                    {{ props.row.description }}
                </b-table-column>

                <b-table-column field='link' label="Source" width="100">
                    <p v-html="_linkify(props.row.link)"></p>
                </b-table-column>

                <b-table-column field='sponsored' label="Sponsored" width="100">
                    <p v-html="_checkify(props.row.sponsored)"></p>
                </b-table-column>
            </template>

        </b-table>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "JobsTable",
        data() {
            return {
                data: [],
                loading: true,
                isPaginated: true,
                isPaginationSimple: true,
                paginationPosition: 'both',
                defaultSortDirection: 'asc',
                currentPage: 1,
                perPage: 10


            }
        },
        methods: {
            getAllData: function () {
                axios
                    .get('/api/v1/jobs/posts/')
                    .then(response => {
                        this.data = response.data
                        this.loading = false

                    })
                    .catch(error => {
                        this.data = []
                        this.errored = true
                        this.loading = false

                    })
                    .finally(() => this.loading = false)
            },
            /**
             * Converts the raw link text from the posts API to HTML
             * @param {String} text The raw link text
             * */
            _linkify: function (text) {
                return text.replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank">Link</a>');
            },

            /**
             * Converts the true/false boolean representation
             * to ✓/✗
             * @param {String} val The boolean value for a field
             * */
            _checkify: function (val) {
                if (val === true) {
                    return "✓"
                } else {
                    return "✗"
                }
            }
        },
        mounted() {
            this.getAllData()

        }
    };
</script>
