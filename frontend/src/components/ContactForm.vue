<template>
    <form v-on:submit.prevent="onSubmit" method="POST">
        <div class="modal-card">
            <header class="modal-card-head">
                <div class="columns is-centered">
                    <div class="column is-half">
                        <figure class="image is-96x96 is-horizontal-center">
                            <img src="../assets/img/email.svg" alt/>
                        </figure>
                    </div>
                    <div class="column is-half">
                        <figure class="image is-96x96 is-horizontal-center">
                            <img src="../assets/img/love.svg" alt/>
                        </figure>
                    </div>
                </div>
            </header>
            <section class="modal-card-body">
                <b-field label="Name">
                    <b-input v-model="name" required></b-input>
                </b-field>
                <b-field label="Email">
                    <b-input
                            type="email" value="email" placeholder="Your email" v-model="email" required>
                    </b-input>
                </b-field>
                <b-field
                        label="Subject">
                    <b-select placeholder="Select a subject" expanded v-model="subject">
                        <option value="jobs">Job listing(s)</option>
                        <option value="other">Other</option>
                    </b-select>
                </b-field>
                <b-field label="Message"
                         :label-position="labelPosition">
                    <b-input maxlength="200" type="textarea" v-model="message"></b-input>
                </b-field>

            </section>
            <footer class="modal-card-foot">
                <button class="button" type="button" @click="$parent.close()">Close</button>
                <button class="button is-info">Send</button>
            </footer>
        </div>
    </form>


</template>

<script>
    export default {
        name: "ContactForm",
        data() {
            return {
                name: "",
                email: "",
                subject: "",
                message: ""
            }
        }
    }
</script>

<style scoped>

</style>
