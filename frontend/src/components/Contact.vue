<template>
    <div id="ContactForm">
        <div class="container">
            <div class="item columns" style>
                <div class="column is-full">
                    <nav class="level" style>
                        <div class="level-item">
                            <p>
                                Comments or questions?
                                <a @click="isComponentModalActive = true">Contact us!</a>
                            </p>

                        </div>
                        <b-modal :active.sync="isComponentModalActive" has-modal-card trap-focus>
                            <ContactForm v-bind="formProps"></ContactForm>
                        </b-modal>

                    </nav>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import ContactForm from "./ContactForm";

    export default {
        name: "Contact",
        components: {
            ContactForm,
        },
        data() {
            return {
                isComponentModalActive: false,
                formProps: {
                    email: "your@email.com",
                }
            };
        }
    };
</script>

<style scoped>
    #email-icon:hover {
        opacity: .7;

    }
</style>
