<template>
  <div id="home">
    <NavigationBar></NavigationBar>
    <!-- Hero-->
    <section class="hero is-medium">
      <div class="hero-body">
        <div class="container">
          <div class="columns is-vcentered" data-aos="fade-left">
            <div class="column is-half has-text-right">
              <figure class="image is-horizontal-center">
                <img src="../assets/img/logo.png" alt />
              </figure>
              <h2 class="subtitle">Graditude is Job 1.</h2>
            </div>
            <div class="column is-half"></div>
          </div>
        </div>
      </div>
    </section>
    <!-- End of Hero -->

    <!-- Communication -->
    <section id="communication" class="section">
      <div class="container">
        <div class="columns">
          <div class="column is-full has-text-centered" data-aos="fade-left" data-aos-delay="300">
            <p class="is-size-2">Land your next job, starting now.</p>
            <p>Are you a new graduate software engineer? Well, you've come to the right place.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="columns is-centered">
          <div class="column is-one-third has-text-centered" data-aos="zoom-in">
            <figure class="image is-128x128 is-horizontal-center">
              <img src="../assets/img/teamwork.svg" alt />
            </figure>
            <p class="promo-caption">Stay Motivated</p>
            <p class="light center">
              Job hunting for new graduates can be tough. Graditude's mission is to
              encourage the growth of the next generation of professionals.
            </p>
          </div>
          <div class="column is-one-third has-text-centered" data-aos="zoom-in">
            <figure class="image is-128x128 is-horizontal-center">
              <img src="../assets/img/cloud-computing.svg" alt />
            </figure>
            <p class="promo-caption">Searching, made simple</p>
            <p class="light center">
              Browse a simple, centralized database curated using Indeed. Graditude's listings are updated
              twice an hour, every hour.
            </p>
          </div>
          <div class="column is-one-third has-text-centered" data-aos="zoom-in">
            <figure class="image is-128x128 is-horizontal-center">
              <img src="../assets/img/yoga.svg" alt />
            </figure>
            <p class="promo-caption">Ad-free, stress-free</p>
            <p class="light center">
              Graditude makes job-hunting stress-free by filtering out ads
              and displaying posts tabularly. The fewer clicks are made, the more
              efficient searching becomes.
            </p>
          </div>
        </div>
      </div>
    </section>
    <section>
      <div class="container">
        <div class="columns is-centered" data-aos="fade-left" data-aos-delay="300">
          <div class="column is-one-quarter has-text-centered">
            <a href class="button is-info">Ready to elevate your search?</a>
          </div>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <div class="column">
          <JobsTable></JobsTable>
        </div>
      </div>
    </section>
    <!-- Footer -->
    <footer class="section">
      <Contact></Contact>
    </footer>
  </div>
</template>

<script>
import JobsTable from "../components/JobsTable";
import NavigationBar from "../components/NavigationBar";
import Contact from "../components/Contact";

export default {
  name: "home",
  components: {
    JobsTable: JobsTable,
    NavigationBar: NavigationBar,
    Contact: Contact
  }
};
</script>

<style>
.hero .hero-body {
  background: rgb(255, 255, 255);
  background: linear-gradient(
    180deg,
    rgba(255, 255, 255, 1) 0%,
    rgba(28, 93, 132, 0.06993090204831931) 100%
  );
}

.is-horizontal-center {
  margin-left: auto;
  margin-right: auto;
}

.promo-caption {
  font-weight: bold;
  margin-top: 20px;
}

#communication {
  margin-top: 0%;
}
</style>
