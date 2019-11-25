<template>
  <div id="ContactForm">
    <div class="container">
      <div class="item columns" style>
        <div class="column is-full">
          <nav class="level" style>
            <div class="level-item">
              <a
                class="button is-info is-outlined navbar-item bd-navbar-item"
                @click="isComponentModalActive = true"
              >Get in Touch</a>
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
    ContactForm
  },

  data() {
    return {
      isComponentModalActive: false,
      formProps: {
        email: "your@email.com"
      }
    };
  }
};
</script>

<style scoped>
#email-icon:hover {
  opacity: 0.7;
}
</style>
