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
        <b-field label="Select a date">
            <b-datepicker
                    placeholder="Click to select..."
                    v-model="dates"
                    range>
            </b-datepicker>
        </b-field>

        <form @submit.prevent="addFilter">
            <b-field grouped>

                <b-select v-model="filteredProperty">
                    <option value="company">Company</option>
                    <option value="location">Location</option>
                    <option value="title">Title</option>
                    <option value="description">Description</option>
                </b-select>
                <b-input placeholder="search" v-model="query" v-on:keyup.enter="submit"></b-input>
                <b-button type="'is-info" @click="addFilter">Filter</b-button>

            </b-field>
        </form>
        <table v-if="activeFilters.length">
            <tr style="width: 100px">
                <th colspan="3">Filters in use:</th>
            </tr>
            <tr v-for="(filter, index) in activeFilters" :key="index">
                <td>{{ filter.name }}:</td>
                <td>{{ filter.value }}</td>
                <td style="padding-left: 10px;">
                    <a @click.prevented=removeFilter(index)>
                        remove
                    </a>
                </td>
            </tr>
        </table>

        <b-table id="jobs-table"
                 :data="filtered"
                 :loading="loading"

                 :paginated="isPaginated"
                 :per-page="perPage"
                 :current-page.sync="currentPage"
                 :pagination-simple="isPaginationSimple"
                 :pagination-position="paginationPosition"

                 :default-sort-direction="defaultSortDirection"
                 default-sort="date_posted"

                 aria-next-label="Next page"
                 aria-previous-label="Previous page"
                 aria-page-label="Page"
                 aria-current-label="Current page"
        >
            <template slot-scope="props">
                <b-table-column field="date_posted" label="Date Posted" width="150" sortable centered>
                    {{ props.row.date_posted | moment }}
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
    import moment from 'moment'

    export default {
        name: "JobsTable",
        data() {
            return {
                data: [],
                loading: true,
                isPaginated: true,
                isPaginationSimple: true,
                paginationPosition: 'both',
                defaultSortDirection: 'desc',
                currentPage: 1,
                perPage: 10,

                // Parameters to query the table
                filteredProperty: 'company',
                query: '',
                activeFilters: [],
                dates: []

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
             * Converts the true/false boolean representation to ✓/✗
             * @param {String} val The boolean value for a field
             * */
            _checkify: function (val) {
                if (val === true) {
                    return "✓"
                } else {
                    return "✗"
                }
            },
            /**
             * Adds filters to the activeFilters array
             */
            addFilter: function () {
                this.activeFilters.push({
                    name: this.filteredProperty,
                    value: this.query
                })
                this.query = ''
            },
            /**
             * Removes filters from the activeFilters array
             * @param idx
             */
            removeFilter: function (idx) {
                this.activeFilters.splice(idx, 1)
            }
        },
        mounted() {
            this.getAllData()

        },
        computed: {
            /**
             * Filters the data array of objects based on date and filtering parameters
             * @returns {[]}
             */
            filtered() {
                let filtered = this.data

                // Filter objects by 'date_posted' field if a date range filter is selected
                if (this.dates.length > 0) {
                    filtered = filtered.filter(record => {
                        return moment(record['date_posted']).isBetween(this.dates[0], this.dates[1], null, '[]')
                    })
                }


                this.activeFilters.forEach(filter => {
                    filtered = filtered.filter(record => {
                        return filter.name === 'title'
                            ? new RegExp(filter.value, 'i').test(record[filter.name])
                            : record[filter.name] === filter.value
                    })
                })
                return filtered
            }
        },
        filters: {
            /**
             * Format the JSON date returned by the API into the specified format
             * @param date
             * @returns {string}
             */
            moment: function (date) {
                return moment(date).format('MM/DD/YY')
            }
        }
    };
</script>
